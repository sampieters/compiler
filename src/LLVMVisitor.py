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
        _type = typeToLLVM(node.type)

        instruction = "store "
        # If we want to store a variable
        if isinstance(value, IdentifierNode):
            value = self.table.get_symbol(value.name)
            # Load the variable into a new temporary address before storing it
            self.loadVariable(value)
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + " %" + value.temp_address
        # If we want to store the result of an operation
        elif isinstance(value, BinaryOperationNode) or isinstance(value, UnaryOperationNode):
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + " %" + value.temp_address
        # If we want to store a literal
        elif isinstance(value, LiteralNode):
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + ' ' + value.getValue()
        
        # If the node is a variable, get the node from the symbol table and store into the original address
        if isinstance(node, IdentifierNode):
            node = self.table.get_symbol(str(node))
            instruction += ", " + _type[0] + "* " + node.original_address + ", " + _type[1]
        # Otherwise, store into the temporary address of the node
        else:
            instruction += ", " + _type[0] + "* " + node.temp_address + ", " + _type[1]
        self.LLVM.append(instruction)

    def loadVariable(self, node):
        """Loads a variable into a new temporary address"""
        node = self.table.get_symbol(str(node))
        _type = typeToLLVM(node.type)

        # Change the temporary address of the variable to the new address, load the original address into it
        load_addr = self.counter.incr()
        node.temp_address = load_addr
        instruction = '%' + load_addr + " = load " + _type[0] + ", " + _type[0] + "* " + \
                      node.original_address + ", " + _type[1]
        self.LLVM.append(instruction)

    def typeToRightType(self, node, type1, type2):
        # TODO: type1 or 2 is inside node so one paramter can go
        #
        # How it works:
        #
        # type1 identifier_1 = something;
        # type2 identifier_2 = identifier_1; <-- This in this function is converted to llvm
        self.loadVariable(node)
        # node parameter needs to have type 1 in it
        if type1 == "int":
            if type2 == "float":
                #      "%4 STOND HIER                                counter of load
                text = "%" + self.counter.incr + " = sitofp i32 %" + str(self.counter-1) + " to float \
                        store float %" + str(self.counter) + ", float* %2, align 4"
            elif type2 == "double":
                text = "%" + self.counter.incr + " = sitofp i32 %" + str(self.counter-1) + "3 to double \
                       store double %" + str(self.counter) + ", double* %2, align 8"
            elif type2 == "char":
                text = "%" + self.counter.incr + " = trunc i32 %" + str(self.counter-1) + " to i8 \
                        store i8 %" + str(self.counter) + ", i8* %2, align 1"
            elif type2 == "long int":
                instruction = "%" self.counter.incr() + " = sext i32 %" + str(self.counter.counter-1) + " to i64" 

        elif type1 == "char":
            if type2 == "int":
                text = "%" + self.counter.incr + " = sext i8 %" + str(self.counter-1) + " to i32 \
                        store i32 %" + str(self.counter) + ", i32* %2, align 4"
            elif type2 == "float":
                text = "%" + self.counter.incr + " = sitofp i8 %" + str(self.counter-1) + " to float \
                        store float %" + str(self.counter) + ", float* %2, align 4"
            elif type2 == "double":
                text = "%" + self.counter.incr + " = sitofp i8 %" + str(self.counter-1) + " to double \
                        store double %" + str(self.counter) + ", double* %2, align 8"

        elif type1 == "float":
            if type2 == "int":
                text = "%" + self.counter.incr + " = fptosi float %" + str(self.counter-1) + " to i32 \
                        store i32 %" + str(self.counter) + ", i32* %2, align 4"
            elif type2 == "char":
                text = "%" + self.counter.incr + " = fptosi float %" + str(self.counter-1) + " to i8 \
                        store i8 %" + str(self.counter) + ", i8* %2, align 1"
            elif type2 == "double":
                text = "%" + self.counter.incr + " = fpext float %" + str(self.counter-1) + " to double \
                        store double %" + str(self.counter) + ", double* %2, align 8"

        elif type1 == "double":
            if type2 == "int":
                text = "%" + self.counter.incr + " = fptosi double %" + str(self.counter-1) + " to i32 \
                        store i32 %" + str(self.counter) + ", i32* %2, align 4"
            elif type2 == "char":
                text = "%" + self.counter.incr + " = fptosi double %" + str(self.counter-1) + " to i8 \
                        store i8 %" + str(self.counter) + ", i8* %2, align 1"
            elif type2 == "float":
                text = "%" + self.counter.incr + " = fptrunc double %" + str(self.counter-1) + " to float \
                        store float %" + str(self.counter) + ", float* %2, align 4"

        elif type1.endswith("*"):
            self.typeToRightType(node, type1, "long int")
            instruction = "%" + self.counter.incr() + " = inttoptr i64" + str(self.counter.counter-1) + " to " + type1
        
        # TODO: node van identifier nog gelijkstellen aan nieuwe node
        self.storeVariable()

    def visitDeclaration(self, node):
        """Transform declaration node to LLVM"""
        # Set the original address for the new variable, add it to the symbol table
        address = '%' + self.counter.incr()
        node.children[0].original_address = address
        self.table.add_symbol(node.children[0])

        # Convert the declaration to LLVM
        instruction = address + " = alloca "
        check = node.children[0].type

        temp = typeToLLVM(check)
        instruction += temp[0] + ", " + temp[1]
        self.LLVM.append(instruction)

    def visitDefinition(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the definition into the variable on the left, the rest is handled by declaration
        self.storeVariable(node.children[0].children[0], node.children[1])

    def visitAssignment(self, node):
        """Transform definition node to LLVM"""
        # Simply store the right side of the assignment into the variable on the left
        self.storeVariable(self.table.get_symbol(node.children[0].name), node.children[1])

    def visitUnaryOperation(self, node):
        """Transform unary operation node to LLVM"""
        # If the unary operation is performed on a variable, load it into a new temporary address
        if isinstance(node.children[0], IdentifierNode):
            var = self.table.get_symbol(node.children[0].name)
            self.loadVariable(var)
        node.temp_address = str(self.counter)
        # Get the LLVM equivalents of the type and operation
        temp = unaryOpToLLVM(node.operation)
        _type = typeToLLVM(node.children[0].type)
        # If the unary operation is -
        if node.operation == '-':
            instruction = '%' + self.counter.incr() + " = "
            if isinstance(node.children[0], IdentifierNode):
                instruction += temp[0] + ' ' + _type[0] + " " + temp[1] + ", %" + \
                             str(self.table.get_symbol(node.children[0].name).temp_address)
            elif isinstance(node.children[0], LiteralNode):
                # CONFUSED (weet niet wat eerste parameter is voor store variable)
                self.storeVariable(node, node.children[0])
            elif isinstance(node.children[0], BinaryOperationNode) or isinstance(node.children[0], UnaryOperationNode):
                instruction += temp[0] + ' ' + _type[0] + " " + temp[1] + ", %" + str(node.children[0].temp_address)
            self.LLVM.append(instruction)
        # If the operation is a prefix ++ or --
        elif node.operation == "++x" or node.operation == "--x":
            # This nodes address should be the address the addition is stored in
            node.temp_address = str(self.counter)
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(node.children[0])
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "int", -1))            
            bin_op.type = node.children[0].type
            bin_op.temp_address = str(self.counter)
            # Perform the binary operation
            self.performBinaryOp(bin_op)
            # Store the result of the operation to the original variable
            self.storeVariable(node.children[0], bin_op)
        elif node.operation == "x++" or node.operation == "x--":
            # This nodes address should be the address of the node before the addition
            node.temp_address = str(self.counter.counter - 1)
            # Convert this operation to a binary operation node
            bin_op = BinaryOperationNode("+", -1)
            bin_op.add_child(node.children[0])
            bin_op.add_child(LiteralNode(eval(node.operation[1] + "1"), "int", -1))
            bin_op.type = node.children[0].type
            bin_op.temp_address = str(self.counter)
            # Perform the binary operation
            self.performBinaryOp(bin_op)
            # Store the result of the operation to the original variable
            self.storeVariable(node.children[0], bin_op)
        # If the operation is !
        elif node.operation == "!":
            #TODO: Don't need to check Literal Node because is solved in Optimisation Visitor, but might want to implement this later
            temp_type = typeToLLVM(node.children[0].type)
            if isinstance(node.children[0], BinaryOperationNode):
                # TODO: split up in separate functions?
                self.LLVM.append('%' + self.counter.incr() + " = icmp ne " + temp_type[0] + " %" + node.children[0].temp_address + ", 0")
                self.LLVM.append('%' + self.counter.incr() + " = xor i1 %" + str(self.counter.counter - 2) + ", true")
                self.LLVM.append('%' + self.counter.incr() + " = zext i1 %" + str(self.counter.counter - 2) + " to i32")
                if temp_type[0] == "i64":
                    self.LLVM.append('%' + self.counter.incr() + " = sext i32 %" + str(self.counter.counter - 2) + " to i64")
                #TODO: Nog iets doen voor i32 om te zetten naar type



    def visitBinaryOperation(self, node):
        """Convert binary operation node to LLVM"""
        # For each child that is a variable, load the variable into a new temporary address
        for child in node.children:
            if isinstance(child, IdentifierNode):
                temp_node = self.table.get_symbol(child.name)
                self.loadVariable(temp_node)
        # Perform the binary operation
        self.performBinaryOp(node)

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
                children_LLVM.append(typeToLLVM(child.type)[0] + " %" + str(self.table.get_symbol(child.name).temp_address))
        # Construct the LLVM instruction
        instruction = '%' + bin_op.temp_address + " = " + BinaryOpToLLVM(bin_op.operation) + ' ' + ", ".join(children_LLVM)
        self.LLVM.append(instruction)