from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.before_LLVM = []
        self.LLVM = []
        self.after_LLVM = []
        self.loop_stack = []
        self.stat_stack = []
        self.table = SymbolTable()
        self.counter = Counter()
        self.str_counter = Counter()

    def storeVariable(self, node, value, load=True):
        """Stores value (node with a type) into a variable from the symbol table"""
        instruction = "store "
        node = self.getSymbol(node)
        value = self.getSymbol(value)

        # If we want to store a variable
        if load and node.type == value.type:
            # Load the variable into a new temporary address before storing it, unless it is an argument of a function
            self.loadVariable(value)

        instruction += node.type + " " + value.getValue()
        instruction += ", " + node.type + "* " 
        instruction += node.getValue(original=True) 
        instruction += ", align " + node.alignment()

        self.LLVM.append("  " + instruction)

    def loadVariable(self, node):
        """Loads a variable into a new temporary address"""
        # Types where there has to be no loads
        if not (isinstance(node, IdentifierNode) or (isinstance(node, UnaryOperationNode) and (node.operation == "*" or node.operation == "[]")) or isinstance(node, FunctionNode)):
            return
        node = self.getSymbol(node)

        # Change the temporary address of the variable to the new address, load the original address into it
        load_addr = self.counter.incr()
        instruction = '%' + load_addr + " = load " + node.type + ", " + node.type + "* " + \
                      node.getValue(original=True) + ", align " + node.alignment()
        node.temp_address = load_addr
        self.LLVM.append("  " + instruction)

    def convertType(self, node1, node2):
        # type1 identifier_1 = something;
        # type2 identifier_2 = identifier_1; <-- This in this function is converted to llvm
        # node parameter needs to have type 1 in it
        # Convert node1 type to node2 type
        node1 = self.getSymbol(node1)
        node2 = self.getSymbol(node2)
        # If the node being converted is a literal, modify the literal so no conversion is needed
        if isinstance(node1, LiteralNode):
            if node1.type == "i8" and isinstance(node1.value,str):
                node1.value = ord(node1.value)
            # If the literal is an integer that has to be converted to decimal, use scientific notation
            if node2.type in DECIMAL_TYPES:
                node1.value = "{:e}".format(float(node1.value))
            # If the literal is a decimal that has to be converted to integer, floor the value
            elif node2.type in INTEGER_TYPES:
                node1.value = int(float(node1.value))
            elif node1.value == 0 and node2.type.startswith("["):
                node1.value = "zeroinitializer"
            node1.type = node2.type
            return

        if node1.type == node2.type:
            return
        # If converting a boolean, start by converting to i32
        if node1.type == "i1":
            self.LLVM.append("  %" + self.counter.incr() + " = zext i1 %" + str(self.counter.counter-2) + " to i32")
            node1.type = "i32"
        # If converting to a pointer, start by converting to i64, then use inttoptr
        if node2.type.endswith("*"):
            self.convertType(node1, IdentifierNode(None, None, "i64"))
            instruction = "%" + self.counter.incr() + " = inttoptr i64 %" + str(self.counter.counter-1) + " to " + node2.type
        else:
            function = getConversionFunction(node1, node2)
            self.loadVariable(node1)
            instruction = "%" + self.counter.incr() + " = " + function + " " + node1.type + " " + node1.getValue() + " to " + node2.type
        node1.temp_address = self.counter.counter - 1
        self.LLVM.append("  " + instruction)

    def exitProg(self, node):
        to_remove = []
        end_block = False
        # Check for return in program if return then branch
        for idx, line in enumerate(self.LLVM):
            if "<label>" in line or line == "}":
                end_block = False
            elif not end_block and ("br label" in line or "br i1" in line or "ret " in line):
                end_block = True
                continue
            if end_block and line != "":
                to_remove.append(idx)
        self.counter.reset()
        for idx in to_remove:
            self.LLVM.pop(idx - int(self.counter.incr()))
        self.before_LLVM.extend(self.LLVM)
        self.before_LLVM.extend(self.after_LLVM)
        self.LLVM = self.before_LLVM

    def enterLiteral(self, node):
        # string linteral is the only literal with @ and no address (special type in LLVM)
        if "string" in node.type_semantics:
            string = node.value
            node.value = "@.str." + self.str_counter.incr()
            self.before_LLVM.append(node.value + " = private unnamed_addr constant [" +
                                    str(node.str_length) + " x i8] c\"" + string + "\", align 1")
        else:
            self.convertType(node, node)

    def exitDeclaration(self, node):
        """Transform declaration node to LLVM"""
        # Set the original address for the new variable, add it to the symbol table
        identifier = node.children[0]
        if not isinstance(node.parent.parent, ArgListNode):
            self.table.add_symbol(identifier)
        # If the declaration is in the global scope then it needs to be treated differently
        if "global" in identifier.type_semantics:
            instruction = identifier.getValue(original=True) + " = "
            value = None
            # If there is no assignement then assign a default value to it
            if not isinstance(node.parent, DefinitionNode):
                # If default assignement, set common before global
                instruction += "common "
                lit = LiteralNode(0, "i32", -1)
                self.convertType(lit, identifier)
                value = lit.value
            else:
                lit = LiteralNode(node.parent.children[1].value, node.parent.children[1].type, -1)
                self.convertType(lit, identifier)
                value = lit.value
            instruction += "global " + identifier.type + " " + str(value) + ", align " + identifier.alignment()
            self.LLVM.append(instruction)
        else:
            # If it is not global, then assign to address
            address = self.counter.incr()
            # Convert the declaration to LLVM
            instruction = "%" + address + " = alloca "
            for dim in identifier.dimensions:
                instruction += f"[{dim} x "
            instruction += identifier.type
            instruction += "]" * len(identifier.dimensions)
            instruction += ", align " + identifier.alignment()
            self.LLVM.append("  " + instruction)

            # If there is no original address yet (the identifier is not an argument of a function)
            identifier.original_address = address
            if isinstance(identifier.parent.parent, ArgListNode):
                self.storeVariable(identifier, identifier, False)

    def exitDefinition(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the definition into the variable on the left, the rest is handled by declaration
        if not "global" in node.children[0].children[0].type_semantics:
            self.convertType(node.children[1], node.children[0].children[0])
            self.storeVariable(node.children[0].children[0], node.children[1])

    def exitAssignment(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the assignment into the variable on the left
        self.convertType(node.children[1], node.children[0])
        self.storeVariable(node.children[0], node.children[1])

    def exitUnaryOperation(self, node):
        """Transform unary operation node to LLVM"""
        child = self.getSymbol(node.children[0])
        # Get the LLVM equivalents of the type and operation
        temp = self.unaryOpToLLVM(node)
        # If the unary operation is -
        if node.operation == '-':
            # If the unary operation is performed on a variable, load it into a new temporary address
            self.loadVariable(child)
            node.temp_address = self.counter.counter
            instruction = '%' + self.counter.incr() + " = "
            if isinstance(child, LiteralNode):
                self.storeVariable(node, child)
            elif isinstance(child, BinaryOperationNode) or isinstance(child, UnaryOperationNode) or isinstance(child, IdentifierNode):
                if child.type.startswith("i"):
                    instruction += temp[0] + ' ' + child.type + " " + temp[1] + ", " + child.getValue()
                else:
                    # Special instruction for floats and doubles
                    instruction += "fneg " + child.type + " " + child.getValue()
            self.LLVM.append("  " + instruction)
        # If the operation is a prefix ++ or --
        elif node.operation == "++x" or node.operation == "--x":
            # This nodes address should be the address the addition is stored in
            node.temp_address = self.counter.counter
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(child)
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "i32", -1))
            bin_op.type = child.type
            bin_op.temp_address = self.counter.counter
            # Perform the binary operation
            self.exitBinaryOperation(bin_op)
            # Store the result of the operation to the original variable
            self.storeVariable(child, bin_op)
        elif node.operation == "x++" or node.operation == "x--":
            # This nodes address should be the address of the node before the addition
            node.temp_address = self.counter.counter - 1
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(child)
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "i32", -1))
            bin_op.type = child.type
            bin_op.temp_address = self.counter.counter
            # Perform the binary operation
            self.exitBinaryOperation(bin_op)

            # Store the result of the operation to the original variable
            self.storeVariable(child, bin_op)
        # If the operation is !
        elif node.operation == "!":
            self.loadVariable(child)
            node.temp_address = self.counter.counter
            if not isinstance(child, LiteralNode):
                literal = LiteralNode(0, child.type, None)
                self.convertType(literal, literal)
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " + child.type + " " + child.getValue() + ", " + literal.getValue())
                self.LLVM.append("  %" + self.counter.incr() + " = xor i1 %" + str(self.counter.counter - 2) + ", true")
                # self.convertType(node, IdentifierNode(None, None, "i32"))
                node.temp_address = self.counter.counter-1
        elif node.operation == "&":
            # Convert the type to a pointer, copy the original address of the identifier node
            node.type = node.children[0].type + "*"
            node.temp_address = self.getSymbol(node.children[0]).original_address
        elif node.operation == "*":
            # Since type is already generated in SemanticalErrorVisitor, simply take the original address of the identifier node
            identifier = self.getSymbol(node.children[0])
            self.loadVariable(identifier)
            node.original_address = identifier.temp_address
        elif node.operation == "[]":
            identifier = self.getSymbol(node.children[0])
            value = self.getSymbol(node.children[1])
            self.convertType(value, IdentifierNode(None, -1, "i64"))
            node.type = "".join(identifier.type.split()[2:])[:-1]
            node.original_address = self.counter.incr()
            self.LLVM.append(f"  {node.getValue(original=True)} = getelementptr inbounds {identifier.type}, {identifier.type}* {identifier.getValue(original=True)}, i64 0, i64 {value.getValue()}")

    def enterContinue(self, node):
        # branch to the LLVM branch of the While condition
        self.LLVM.append("  br label %" + str(getParent(node, WhileNode).start_address))

    def enterBreak(self, node):
        # break to a yet to be declared branch, this branch is the end of the scope
        self.LLVM.append("  br label %{BREAK}")
        self.loop_stack.append(len(self.LLVM) - 1)

    def exitBinaryOperation(self, node):
        """Convert binary operation node to LLVM"""
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])
        # For each child that is a variable, load the variable into a new temporary address
        for child in [child1, child2]:
            self.loadVariable(child)
        # Store the result of the binary operation in a new address
        node.temp_address = int(self.counter.incr())
        # Convert the children to LLVM, depending on their node types
        children_LLVM = []
        the_type = getBinaryType(child1.type, child2.type)
        for child in [child1, child2]:
            # Convert the child to the binary operation type, so that both children have the same type
            self.convertType(child, IdentifierNode(None, None, the_type))
            children_LLVM.append(child.getValue())
        # Construct the LLVM instruction
        instruction = f"{node.getValue()} = {self.binaryOpToLLVM(node)} {the_type} {', '.join(children_LLVM)}"
        self.LLVM.append("  " + instruction)

    def enterWhile(self, node):
        # branch to the condition that has to be met for the while
        self.LLVM.append("  br label %" + str(self.counter.counter))
        self.LLVM.append("")
        node.start_address = self.counter.counter
        self.LLVM.append(f"; <label>:{self.counter.incr()}:")
        self.loop_stack.append(len(self.LLVM) - 1)

    def enterElif(self, node):
        # branch to the condition that has to be met for the elif
        self.LLVM.append("")
        self.LLVM.append(f"; <label>:{self.counter.incr()}:")

    def enterElse(self, node):
        node.start_address = self.counter.counter-1

    def enterFunctionDefinition(self, node):
        # Define a function in LLVM with the define instruction
        self.LLVM.append("")
        function = node.children[0].children[0]
        instruction = "define " + function.type + " " + function.getValue() + "("
        # generate all the parameters for the function
        children_LLVM = []
        for child in function.children[0].children:
            child = child.children[0]
            child.temp_address = self.counter.incr()
            children_LLVM.append(child.type)
        instruction += ", ".join(children_LLVM)
        instruction += ") {"
        self.LLVM.append(instruction)

        function.original_address = self.counter.incr()

        # If the function's return type is not void, then there needs to be a return (always)
        if function.type != "void":
            ret_address = self.counter.incr()
            function.original_address = ret_address
            # Convert the declaration to LLVM
            instruction = function.getValue(original=True) + " = alloca " + function.type
            instruction += ", align " + function.alignment()
            self.LLVM.append("  " + instruction)

    def exitFunctionDefinition(self, node):
        # End Function definition
        self.LLVM.append("}")
        self.counter.reset()

    def exitFunctionDeclaration(self, node):
        # add the function to the symbol table
        function = node.children[0]
        self.table.add_symbol(function)

    def exitFunctionCall(self, node):
        # Get the function with the right addresses from the table
        function = self.getSymbol(node.children[0])

        children_LLVM = []
        # Special cases 'printf' and 'scanf'
        if function.name == "printf" or function.name == "scanf":
            if f"declare i32 @{function.name}(i8*, ...)" not in self.after_LLVM:
                self.after_LLVM.append(f"declare i32 @{function.name}(i8*, ...)")
            for child in node.children[1].children:
                child = self.getSymbol(child)
                if "string" not in child.type_semantics and not child.type.endswith("i8]"):
                    self.loadVariable(child)
                if child.type.endswith("i8]"):
                    addr = self.counter.incr()
                    self.LLVM.append(f"  %{addr} = getelementptr inbounds {child.type}, {child.type}* {child.getValue(original=True)}, i64 0, i64 0")
                    children_LLVM.append(f"i8* %{addr}")
                elif child.type == "float":
                    self.convertType(child, IdentifierNode(None, None, "double"))
                    children_LLVM.append("double " + child.getValue())
                else:
                    children_LLVM.append(child.type + " " + child.getValue())
        else:
            for child, arg_child in zip(node.children[1].children, function.children[0].children):
                child = self.getSymbol(child)
                arg_child = arg_child.children[0]
                self.convertType(child, arg_child)
                self.loadVariable(child)
                children_LLVM.append(child.type + " " + child.getValue())

        instruction = "  "
        if not function.type == "void":
            node.temp_address = self.counter.incr()
            instruction += node.getValue() + " = "
        instruction += "call " + function.type + " " + function.getValue() + "("
        instruction += ", ".join(children_LLVM)
        instruction += ")"
        self.LLVM.append(instruction)

    def enterScope(self, node):
        # Cases split when entering a scope (while, if, else, ...)
        self.table.enter_scope()
        if isinstance(node.parent, WhileNode):
            condition = self.getSymbol(node.parent.children[0])
            self.loadVariable(condition)
            if isinstance(node.parent.children[0], IdentifierNode):
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " +
                                condition.type + " " + condition.getValue() + ", 0")
            elif isinstance(node.parent.children[0], LiteralNode):
                self.LLVM.append("  %" + self.counter.incr() + " = icmp ne " + node.parent.children[0].type + " " + str(node.parent.children[0].value) + ", 0")
            self.LLVM.append("  br i1 %" + str(self.counter.counter - 1) + ", label %" + str(self.counter.counter) + ", label %{LABEL}")
            instruction_index = self.loop_stack.pop()
            self.LLVM[instruction_index] = self.LLVM[instruction_index].replace("{LABEL}", str(self.counter.counter))
            self.loop_stack.append(len(self.LLVM)-1)
            self.LLVM.append("")
            self.LLVM.append(f"; <label>:{self.counter.incr()}:")
        elif isinstance(node.parent, IfNode):
            to_fill = None
            if isinstance(node.parent.children[0], LiteralNode):
                if node.parent.children[0].value == 0:
                    to_fill = "0"
                else:
                    to_fill = "1"
            elif isinstance(node.parent.children[0], IdentifierNode):
                self.loadVariable(node.parent.children[0])
                identifier = self.getSymbol(node.parent.children[0])
                new_node = BinaryOperationNode("!=", -1)
                new_node.add_child(identifier)
                new_node.add_child(LiteralNode(0, "i32", -1))
                self.convertType(new_node.children[1], new_node.children[0])
                self.LLVM.append("  %" + self.counter.incr() + " = " + self.binaryOpToLLVM(new_node) + ' ' +
                                 identifier.type + ' ' + new_node.children[0].getValue() + ", " +
                                 new_node.children[1].getValue())
                to_fill = '%' + str(self.counter.counter - 1)
            else:
                to_fill = '%' + str(self.counter.counter - 1)
            self.LLVM.append("  br i1 " + to_fill + ", label %" + str(self.counter.counter) + ", label %{LABEL}")
            self.stat_stack.append(len(self.LLVM) - 1)
            self.LLVM.append("")
            node.parent.start_address = self.counter.counter
            self.LLVM.append(f"; <label>:{self.counter.incr()}:")

    def exitScope(self, node):
        if isinstance(node.parent, WhileNode):
            self.LLVM.append("  br label %" + str(node.parent.start_address))
            self.LLVM.append("")
            index = self.loop_stack.pop()
            while "{BREAK}" in self.LLVM[index]:
                self.LLVM[index] = self.LLVM[index].replace("{BREAK}", str(self.counter.counter))
                index = self.loop_stack.pop()
            self.LLVM[index] = self.LLVM[index].replace("{LABEL}", str(self.counter.counter))
            self.LLVM.append(f"; <label>:{self.counter.incr()}:")
        elif isinstance(node.parent, IfNode):
            possible_index = None
            if isinstance(node.parent.parent.children[-1], ElseNode):
                self.LLVM.append("  br label %{LABEL}")
                possible_index = len(self.LLVM) - 1
            else:
                self.LLVM.append("  br label %" + str(self.counter.counter))
            self.LLVM.append("")
            index = self.stat_stack.pop()
            self.LLVM[index] = self.LLVM[index].replace("{LABEL}", str(self.counter.counter))
            if possible_index is not None:
                self.stat_stack.append(possible_index)
            self.LLVM.append(f"; <label>:{self.counter.incr()}:")
        elif isinstance(node.parent, ElseNode):
            self.LLVM.append("  br label %" + str(self.counter.counter))
            self.LLVM.append("")
            index = self.stat_stack.pop()
            self.LLVM[index] = self.LLVM[index].replace("{LABEL}", str(self.counter.counter))
            self.LLVM.append(f"; <label>:{self.counter.incr()}:")
        self.table.exit_scope()

    def exitReturn(self, node):
        function = getParent(node, FunctionDefinitionNode).children[0].children[0]
        if not isinstance(node.parent.parent, FunctionDefinitionNode):
            if function.type != "void":
                self.storeVariable(function, node.children[0])
        else:
            instruction = "  ret "
            if not node.children:
                instruction += "void"
            else:
                ret_val = self.getSymbol(node.children[0])
                self.loadVariable(function)
                instruction += ret_val.type + " %" + function.temp_address
            self.LLVM.append(instruction)

    def unaryOpToLLVM(self, node):
        child = self.getSymbol(node.children[0])

        try:
            operation = UNARY_OPS_LLVM[node.operation]
        except KeyError:
            raise Exception(f"Invalid unary operation '{node.operation}'")

        # Check if signed or unsigned
        if "unsigned" in child.type_semantics:
            if operation[0] == "sub":
                operation[0] += " nuw"
        else:
            if operation[0] == "sub":
                operation[0] += " nsw"
        return operation

    def binaryOpToLLVM(self, node):
        child1 = self.getSymbol(node.children[0])
        child2 = self.getSymbol(node.children[1])

        the_type = getBinaryType(child1.type, child2.type)

        ret_val = ""
        try:
            operation = BINARY_OPS_LLVM[node.operation]
        except KeyError:
            raise Exception(f"Invalid binary operation '{node.operation}'")

        # STEP 1: check f or i (example: icmp or fcmp || add or fadd)
        if the_type.startswith("i"):
            if operation[0] == "cmp":
                ret_val += "i"
            elif operation[0] == "div" or operation[0] == "rem":
                if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                    ret_val += "u"
                else:
                    ret_val += "s"
        else:
            ret_val += "f"

        # STEP 2: The actual operation
        ret_val += operation[0]

        extra = ""
        # STEP 3: Check if signed or unsigned
        if operation[0] != "div" and operation[0] != "rem":
            if "unsigned" in child1.type_semantics or "unsigned" in child2.type_semantics:
                if the_type.startswith("i"):
                    if not operation[0] == "cmp":
                        extra += "nuw"
                    elif operation[1] != "eq" and operation[1] != "ne":
                        extra += "u"
                else:
                    if operation[0] == "cmp":
                        if operation[1] != "ne":
                            extra += "o"
                        else:
                            extra += "u"
            else:
                if the_type.startswith("i"):
                    if not operation[0] == "cmp":
                        extra += "nsw"
                    elif operation[1] != "eq" and operation[1] != "ne":
                        extra += "s"
                else:
                    if operation[0] == "cmp":
                        if operation[1] != "ne":
                            extra += "o"
                        else:
                            extra += "u"
        # If the operation exist of multiple parts (icmp ne)
        if len(operation) == 2:
            extra += operation[1]

        if extra:
            ret_val += " " + extra

        return ret_val

    def getSymbol(self, node):
        if (isinstance(node, IdentifierNode) or isinstance(node, FunctionNode)) and not node.name in [None, "printf", "scanf"]:
            return self.table.get_symbol(node.name)
        else:
            return node
