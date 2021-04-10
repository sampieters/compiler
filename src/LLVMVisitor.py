from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.LLVM = []
        self.table = SymbolTable()
        self.counter = Counter()

    def storeVariable(self, node, value):
        """Stores value (node with a type) into a variable from the symbol table"""
        instruction = "store "
        # If we want to store a variable
        if isinstance(value, IdentifierNode):
            value = self.getSymbol(value)
            # Load the variable into a new temporary address before storing it
            self.loadVariable(value)
            instruction += value.type + " %" + value.temp_address
        # If we want to store the result of an operation
        elif isinstance(value, BinaryOperationNode) or isinstance(value, UnaryOperationNode):
            instruction += value.type + " %" + value.temp_address
        # If we want to store a literal
        elif isinstance(value, LiteralNode):
            instruction += value.type + ' ' + value.getValue()
        
        # If the node is a variable, get the node from the symbol table and store into the original address
        if isinstance(node, IdentifierNode):
            node = self.getSymbol(node)
            instruction += ", " + node.type + "* " + node.original_address + ", align " + node.alignment()
        # Otherwise, store into the temporary address of the node
        else:
            instruction += ", " + node.type + "* " + node.temp_address + ", align " + node.alignment()
        self.LLVM.append("  " + instruction)

    def loadVariable(self, node):
        """Loads a variable into a new temporary address"""
        node = self.getSymbol(node)

        # Change the temporary address of the variable to the new address, load the original address into it
        load_addr = self.counter.incr()
        node.temp_address = load_addr
        instruction = '%' + load_addr + " = load " + node.type + ", " + node.type + "* " + \
                      node.original_address + ", align " + node.alignment()
        self.LLVM.append("  " + instruction)

    def convertType(self, node1, node2):
        # type1 identifier_1 = something;
        # type2 identifier_2 = identifier_1; <-- This in this function is converted to llvm
        # node parameter needs to have type 1 in it
        if node1.type.endswith("*"):
            self.typeToRightType(node1, IdentifierNode(None, None, "i64"))
            instruction = "%" + self.counter.incr() + " = inttoptr i64 %" + str(self.counter.counter-1) + " to " + node1.type
        else:
            function = getConversionFunction(node1, node2)
            if not function:
                return
            instruction = "%" + self.counter.incr() + " = " + getConversionFunction(node1, node2) + " " + node1.type + " %" + str(self.counter.counter - 2) + " to " + node2.type
        
        # TODO: node van identifier nog gelijkstellen aan nieuwe node
        node1.temp_address = str(self.counter.counter-1)
        self.LLVM.append("  " + instruction)

    def exitDeclaration(self, node):
        """Transform declaration node to LLVM"""
        # Set the original address for the new variable, add it to the symbol table
        identifier = node.children[0]

        address = '%' + self.counter.incr()
        identifier.original_address = address
        self.table.add_symbol(identifier)

        # Convert the declaration to LLVM
        instruction = address + " = alloca "

        instruction += identifier.type + ", align " + identifier.alignment()
        self.LLVM.append("  " + instruction)

    def exitDefinition(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the definition into the variable on the left, the rest is handled by declaration
        self.convertType(node.children[0].children[0], node.children[1])
        self.storeVariable(node.children[0].children[0], node.children[1])

    def exitAssignment(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the assignment into the variable on the left
        self.convertType(self.getSymbol(node.children[0]), node.children[1])
        self.storeVariable(node.children[0], node.children[1])

    def exitUnaryOperation(self, node):
        """Transform unary operation node to LLVM"""
        child = node.children[0]
        # If the unary operation is performed on a variable, load it into a new temporary address
        if isinstance(child, IdentifierNode):
            var = self.getSymbol(child)
            self.loadVariable(var.name)
        node.temp_address = str(self.counter)
        # Get the LLVM equivalents of the type and operation
        temp = unaryOpToLLVM(node.operation)
        # If the unary operation is -
        if node.operation == '-':
            instruction = '%' + self.counter.incr() + " = "
            if isinstance(child, IdentifierNode):
                instruction += temp[0] + ' ' + child.type + " " + temp[1] + ", %" + \
                             str(self.getSymbol(child).temp_address)
            elif isinstance(child, LiteralNode):
                # CONFUSED (weet niet wat eerste parameter is voor store variable)
                self.storeVariable(node, child)
            elif isinstance(child, BinaryOperationNode) or isinstance(child, UnaryOperationNode):
                instruction += temp[0] + ' ' + child.type + " " + temp[1] + ", %" + str(child.temp_address)
            self.LLVM.append("  " + instruction)
        # If the operation is a prefix ++ or --
        elif node.operation == "++x" or node.operation == "--x":
            # This nodes address should be the address the addition is stored in
            node.temp_address = str(self.counter)
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(child)
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "int", -1))            
            bin_op.type = child.type
            bin_op.temp_address = str(self.counter)
            # Perform the binary operation
            self.performBinaryOp(bin_op)
            # Store the result of the operation to the original variable
            self.storeVariable(child, bin_op)
        elif node.operation == "x++" or node.operation == "x--":
            # This nodes address should be the address of the node before the addition
            node.temp_address = str(self.counter.counter - 1)
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(child)
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "int", -1))
            bin_op.type = child.type
            bin_op.temp_address = str(self.counter)
            # Perform the binary operation
            self.performBinaryOp(bin_op)
            # Store the result of the operation to the original variable
            self.storeVariable(child, bin_op)
        # If the operation is !
        elif node.operation == "!":
            #TODO: Don't need to check Literal Node because is solved in Optimisation Visitor, but might want to implement this later
            if isinstance(child, BinaryOperationNode):
                # TODO: split up in separate functions?
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " + child.type + " %" + child.temp_address + ", 0")
                self.LLVM.append("  %" + self.counter.incr() + " = xor i1 %" + str(self.counter.counter - 2) + ", true")
                self.LLVM.append("  %" + self.counter.incr() + " = zext i1 %" + str(self.counter.counter - 2) + " to i32")
                if child.type == "i64":
                    self.LLVM.append("  %" + self.counter.incr() + " = sext i32 %" + str(self.counter.counter - 2) + " to i64")
                #TODO: Nog iets doen voor i32 om te zetten naar type

    def exitBinaryOperation(self, node):
        """Convert binary operation node to LLVM"""
        # For each child that is a variable, load the variable into a new temporary address
        for child in node.children:
            if isinstance(child, IdentifierNode):
                var = self.getSymbol(child)
                self.loadVariable(var)
        # Store the result of the binary operation in a new address
        node.temp_address = self.counter.incr()
        # Convert the children to LLVM, depending on their node types
        children_LLVM = []
        for child in node.children:
            if isinstance(child, LiteralNode):
                children_LLVM.append(child.getValue())
            else:
                children_LLVM.append(child.type + " %" + str(self.getSymbol(child).temp_address))
        # Construct the LLVM instruction
        instruction = '%' + node.temp_address + " = " + self.binaryOpToLLVM(node) + ' ' + ", ".join(children_LLVM)
        self.LLVM.append("  " + instruction)

    def enterWhile(self, node):
        self.LLVM.append("  br label %" + str(self.counter.counter))
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def exitIf(self, node):
        #TODO: Nog preds zoals bij while
        self.LLVM.append(
            "  br i1 %" + str(self.counter.counter - 1) + ", label %" + str(self.counter.counter) + ", label %WHUT")
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')
        self.LLVM.append("  br label %" + str(self.counter.counter))

    def enterElif(self, node):
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def enterElse(self, node):
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def exitElse(self, node):
        self.LLVM.append("  br label %" + str(self.counter.counter))

    def exitBranch(self, node):
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def enterFunctionDefinition(self, node):
        self.LLVM.append("")
        # TODO: Kweet ni wa deze lijn doet
        self.LLVM.append("; Function Attrs: noinline nounwind optnone ssp uwtable")
        instruction = "define " + node.children[0].children[0].type + " @" + node.children[0].children[0].name + "("
        if len(node.children[0].children[0].arg_types) != 0:
            for arg in node.children[0].children[0].arg_types[:-1]:
                instruction += arg + " %" + self.counter.incr() + ", "
            instruction += node.children[0].children[0].arg_types[-1] + " %" + self.counter.incr()
        instruction += ") #0 {"
        self.LLVM.append(instruction)

    def exitFunctionDefinition(self, node):
        self.LLVM.append("}")

    def enterFunctionCall(self, node):
        instruction = "  %" + self.counter.incr() + " call " + node.children[0].type + " @" + node.children[0].name + "("
        # TODO: Nog een FOR LOOP doen
        instruction += ")"
        self.LLVM.append(instruction)

    def enterScope(self, node):
        #TODO:: WHUT NOG INVULLEN + preds ook nog doen + 0 moet nog verandert worden door de 0 van het juiste type
        #9:                                                ; preds = %3
        self.table.enter_scope()
        if isinstance(node.parent, WhileNode):
            if isinstance(node.parent.children[0], IdentifierNode):
                condition = self.getSymbol(node.parent.children[0])
                self.loadVariable(condition)
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " +
                                condition.type + " %" + condition.temp_address + ", 0")
            elif isinstance(node.parent.children[0], LiteralNode):
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " + node.parent.children[0].type + " " + str(node.parent.children[0].value) + ", 0")
            self.LLVM.append("  br i1 %" + str(self.counter.counter - 1) + ", label %" + str(self.counter.counter) + ", label %WHUT")
            self.LLVM.append("")
            self.LLVM.append(self.counter.incr() + ':')

    def exitScope(self, node):
        if isinstance(node.parent, WhileNode):
            self.LLVM.append("  br label %" + str(self.counter.counter))
            self.LLVM.append("")
            self.LLVM.append(self.counter.incr() + ':')
        self.table.exit_scope()

    def unaryOpToLLVM(self, node):
        try:
            operation = UNARY_OPS_LLVM[node.operation]
        except KeyError:
            raise Exception(f"Invalid unary operation '{node.operation}'")
        return operation

    def binaryOpToLLVM(self, node):
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        ret_val = ""
        try:
            operation = BINARY_OPS_LLVM[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")
        _type = getBinaryType(node.children[0].type, node.children[1].type)

        # STEP 1: check f or i (example: icmp or fcmp || add or fadd
        if _type.startswith("i"):
            if operation[0].startswith("cmp"):
                ret_val += "i"
        else:
            ret_val += "f"
        if operation[0] == "div" or operation[0] == "rem":
            if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                ret_val += "u"
            else:
                ret_val += "s"

        # STEP 2: The actual operation
        ret_val += operation[0]

        # STEP 3: Check if signed or unsigned
        if operation[0] != "div" or operation[0] != "rem":
            ret_val += " "
            if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                if not operation[0].startswith("cmp"):
                    ret_val += "nuw"
                elif operation[1] != "eq" and operation[1] != "ne":
                    ret_val += "u"
            else:
                if not operation[0].startswith("cmp"):
                    ret_val += "nsw"
                elif operation[1] != "eq" and operation[1] != "ne":
                    ret_val += "s"

            if len(operation) == 2:
                ret_val += operation[1]
        return ret_val

    def getSymbol(self, node):
        if isinstance(node, IdentifierNode):
            return self.table.get_symbol(node.name)
        else:
            return node
