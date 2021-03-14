from ASTVisitor import *
from ASTNode import *
from utils import *
from SymbolTable import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.LLVM = ""
        self.table = SymbolTable()
        self.counter = Counter()

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
        self.LLVM += "store "
        #Literal Node
        temp = typeToLLVM(node.children[1].type)
        temp_node = self.table.get_symbol(node.children[0].children[0].name)

        # Eerste temp[0] moet wss het type zijn van de literal maar die moet zwz gelijk zijn aan het type van de identifier
        self.LLVM += temp[0] + ' ' + str(node.children[1].value) + ", " + temp[0] + "* " + temp_node.original_adress + \
                     ", " + temp[1] + "\n"

    def visitAssignment(self, node):
        self.LLVM += "store "
        # Literal Node
        self.LLVM += node.children[1].type + ' ' + str(node.children[1].value) + ", " + "lookinhash \n"

    def visitUnaryOperation(self, node):
        if isinstance(node.children[0], IdentifierNode):
            temp_node = self.table.get_symbol(child.name)
            self.LLVM += '%' + self.counter.print_and_incr() + " = load " + temp_node.type + ", " + \
                         temp_node.type + "* " + temp_node.original_adress + ", align X\n"


        self.LLVM += '%' + self.counter.print_and_incr() + " = "
        temp = unaryOpToLLVM(node.operation)
        self.LLVM += temp[0] + " lookinhash ," + temp[1] + "\n"

    def visitBinaryOperation(self, node):
        for child in node.children:
            if isinstance(child, IdentifierNode):
                temp_node = self.table.get_symbol(child.name)
                self.LLVM += '%' + self.counter.print_and_incr() + " = load " + temp_node.type + ", " + \
                             temp_node.type + "* " + temp_node.original_adress + ", align X\n"

        self.LLVM += '%' + self.counter.print_and_incr() + " = " + BinaryOpToLLVM(node.operation) + ' '
        for child in node.children:
            if isinstance(child, LiteralNode):
                self.LLVM += "easy to determine"
            else:
                self.LLVM += "lookinhash"
            if child != node.children[-1]:
                self.LLVM += ', '

        self.LLVM += "\n"
