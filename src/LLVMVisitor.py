from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.LLVM = ""
        self.table = SymbolTable()
        self.counter = Counter()

    def storeVariable(self, node, value):
        _type = typeToLLVM(node.type)

        instruction = "store "
        if isinstance(value, IdentifierNode):
            value = self.table.get_symbol(value.name)
            self.loadVariable(value)
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + " %" + value.temp_adress
        elif isinstance(value, BinaryOperationNode) or isinstance(value, UnaryOperationNode):
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + " %" + value.register
        elif isinstance(value, LiteralNode):
            _type2 = typeToLLVM(value.type)
            instruction += _type2[0] + ' ' + str(value.value)
        instruction += ", " + _type[0] + "* " + node.original_adress + ", " + _type[1] + "\n"
        self.LLVM += instruction

    def loadVariable(self, node, value=None):
        """
        if value is None:
            Loads a variable from the symbol table into a new address, so it can be reused
        otherwise:
            Loads value (node with a type) into a variable from the symbol table
        """
        _type = typeToLLVM(node.type)
        load_addr = self.counter.incr()
        instruction = '%' + load_addr + " = load " + _type[0] + ", " + _type[0] + "* " + \
                      self.table.get_symbol(str(node)).original_adress + ", " + _type[1] + "\n"
        if isinstance(node, IdentifierNode):
            node.temp_adress = load_addr
        elif isinstance(node, BinaryOperationNode) or isinstance(node, UnaryOperationNode):
            node.register = load_addr

        self.LLVM += instruction


    def visitDeclaration(self, node):
        adress = '%' + self.counter.print_and_incr()
        node.children[0].original_adress = adress

        self.LLVM += adress + " = alloca "
        self.table.add_symbol(node.children[0])
        check = node.children[0].type
        if "const" in check:
            print("extra line for const type after the specification of the type (store ...)")
            check = check.replace("const", "")
        check = check.replace("unsigned", "")
        check = check.replace("signed", "")

        temp = typeToLLVM(check)
        self.LLVM += temp[0] + ", " + temp[1] + "\n"

    def visitDefinition(self, node):
        self.storeVariable(node.children[0].children[0], node.children[1])

    def visitAssignment(self, node):
        self.storeVariable(self.table.get_symbol(node.children[0].name), node.children[1])

    def visitUnaryOperation(self, node):
        if isinstance(node.children[0], IdentifierNode):
            temp_node = self.table.get_symbol(node.children[0].name)
            self.loadVariable(temp_node)
        node.register = str(self.counter)

        temp = unaryOpToLLVM(node.operation)
        _type = typeToLLVM(node.children[0].type)
        if node.operation == '-':
            self.LLVM += '%' + self.counter.print_and_incr() + " = "
            if isinstance(node.children[0], IdentifierNode):
                self.LLVM += temp[0] + ' ' + _type[0] + " " + temp[1] + ", %" + \
                             str(self.table.get_symbol(node.children[0].name).temp_adress) + "\n"
            elif isinstance(node.children[0], LiteralNode):
                #TODO: CONFUSED (weet niet wat eerste parameter is voor store variable)
                self.storeVariable(node, node.children[0])
            elif isinstance(node.children[0], BinaryOperationNode) or isinstance(node.children[0], UnaryOperationNode):
                self.LLVM += temp[0] + ' ' + _type[0] + " " + temp[1] + ", %" + str(node.children[0].register) + "\n"
        elif node.operation == "++x" or node.operation == "--x":
            print("TODO")
        elif node.operation == "x++" or node.operation == "x--":
            print("TODO")
        elif node.operation == "!":
            # Don't need to check Literal Node because is solved in Optimisation Visitor
            temp_type = typeToLLVM(node.children[0].type)
            if isinstance(node.children[0], BinaryOperationNode):
                self.LLVM += '%' + self.counter.print_and_incr() + " = icmp ne " + temp_type[0] + " %" + node.children[0].register + ", 0\n" \
                             '%' + self.counter.print_and_incr() + " = xor i1 %" + str(self.counter.counter - 2) + ", true\n" \
                             '%' + self.counter.print_and_incr() + " = zext i1 %" + str(self.counter.counter - 2) + " to i32\n"
                if temp_type[0] == "i64":
                    '%' + self.counter.print_and_incr() + " = sext i32 %" + str(self.counter.counter - 2) + " to i64\n"
                #TODO: Nog iets doen voor i32 om te zetten naar type



    def visitBinaryOperation(self, node):
        for child in node.children:
            if isinstance(child, IdentifierNode):
                temp_node = self.table.get_symbol(child.name)
                self.loadVariable(temp_node)

        node.register = str(self.counter)
        self.LLVM += '%' + self.counter.print_and_incr() + " = " + BinaryOpToLLVM(node.operation) + ' '
        for child in node.children:
            if isinstance(child, LiteralNode):
                self.LLVM += str(child.value)
            else:
                self.LLVM += typeToLLVM(child.type)[0] + " %" + str(self.table.get_symbol(child.name).temp_adress)
            if child != node.children[-1]:
                self.LLVM += ', '
        self.LLVM += "\n"
