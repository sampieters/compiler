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
            value = self.table.get_symbol(value.name)
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
            node = self.table.get_symbol(node.name)
            instruction += ", " + node.type + "* " + node.original_address + ", align " + node.alignment()
        # Otherwise, store into the temporary address of the node
        else:
            instruction += ", " + node.type + "* " + node.temp_address + ", align " + node.alignment()
        self.LLVM.append("  " + instruction)

    def loadVariable(self, node):
        """Loads a variable into a new temporary address"""
        node = self.table.get_symbol(str(node))

        # Change the temporary address of the variable to the new address, load the original address into it
        load_addr = self.counter.incr()
        node.temp_address = load_addr
        instruction = '%' + load_addr + " = load " + node.type + ", " + node.type + "* " + \
                      node.original_address + ", align " + node.alignment
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
            instruction = "%" + self.counter.incr() + " = " + getConversionFunction(node1, node2) + node1.type + " %" + str(self.counter.counter - 2) + " to " + node2.type
        
        # TODO: node van identifier nog gelijkstellen aan nieuwe node
        node.temp_address = str(self.counter.counter-1)
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
        self.convertType(self.table.get_symbol(node.children[0].name), node.children[1])
        self.storeVariable(self.table.get_symbol(node.children[0].name), node.children[1])

    def exitUnaryOperation(self, node):
        """Transform unary operation node to LLVM"""
        child = node.children[0]
        # If the unary operation is performed on a variable, load it into a new temporary address
        if isinstance(child, IdentifierNode):
            var = self.table.get_symbol(child.name)
            self.loadVariable(var)
        node.temp_address = str(self.counter)
        # Get the LLVM equivalents of the type and operation
        temp = unaryOpToLLVM(node.operation)
        # If the unary operation is -
        if node.operation == '-':
            instruction = '%' + self.counter.incr() + " = "
            if isinstance(child, IdentifierNode):
                instruction += temp[0] + ' ' + child.type + " " + temp[1] + ", %" + \
                             str(self.table.get_symbol(child.name).temp_address)
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
                temp_node = self.table.get_symbol(child.name)
                if temp_node is None:
                    print("help")
                self.loadVariable(temp_node)
        # Perform the binary operation
        self.performBinaryOp(node)

    def enterWhile(self, node):
        self.LLVM.append("  br label %" + str(self.counter.counter))
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def enterIf(self, node):
        # TODO: Een load zou hie moeten gebeuren al maar gebeurd niet -> zelfde probleem als de while
        self.LLVM.append("  br i1 %" + str(self.counter.counter - 1) + ", label %" + str(self.counter.counter) + ", label %WHUT")
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def exitIf(self, node):
        # TODO: Ecit wekrt zelfs niet
        self.LLVM.append("END IF")

    def enterElse(self, node):
        self.LLVM.append("  br label %" + str(self.counter.counter))
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def exitElse(self, node):
        # WERKT WEL -> WAAROM IF NIET??
        self.LLVM.append("  br label %" + str(self.counter.counter))
        self.LLVM.append("")
        self.LLVM.append(self.counter.incr() + ':')

    def enterFunctionDeclaration(self, node):
        # TODO: Kweet ni wa deze lijn doet
        print("wooow")
        self.LLVM.append("; Function Attrs: noinline nounwind optnone ssp uwtable")
        self.LLVM.append("define " + node.return_type + " @" + "NAME" + "(" + "ARGUMENTS" + ") #0 {")

    def exitFunctionDeclaration(self, node):
        self.LLVM.append("}")

    def enterFunctionCall(self, node):
        self.LLVM.append("  %" + self.counter.incr() + " call " + "RETUNRTYPE" + " @" + "FUNCTIONNAME" + "()")

    def enterScope(self, node):
        if isinstance(node.parent, WhileNode):
            # NOG EEN LIJN HIER MAAR DIT IS ALLES IN WHILE (...) -> Zou normaal al moeten werken
            self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " + "PREV_TYPE" + " %" + "PREV" + ", 0")
            #TODO:: WHUT NOG INVULLEN
            self.LLVM.append("  br i1 %" + str(self.counter.counter - 1) + ", label %" + str(self.counter.counter) + ", label %WHUT")
            self.LLVM.append("")
            self.LLVM.append(self.counter.incr() + ':')

    def exitScope(self, node):
        if isinstance(node.parent, WhileNode):
            self.LLVM.append("  br label %" + str(self.counter.counter))
            self.LLVM.append("")
            self.LLVM.append(self.counter.incr() + ':')

    def performBinaryOp(self, bin_op):
        """Perform a binary operation given a binary operation node"""
        # Store the result of the binary operation in a new address
        bin_op.temp_address = self.counter.incr()
        # Convert the children to LLVM, depending on their node types
        children_LLVM = []
        for child in bin_op.children:
            if isinstance(child, LiteralNode):
                children_LLVM.append(child.getValue())
            else:
                children_LLVM.append(child.type + " %" + str(self.table.get_symbol(child.name).temp_address))
        # Construct the LLVM instruction
        instruction = '%' + bin_op.temp_address + " = " + BinaryOpToLLVM(bin_op.operation) + ' ' + ", ".join(children_LLVM)
        self.LLVM.append("  " + instruction)
