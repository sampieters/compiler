from ASTVisitor import *
from ASTNode import *
from utils import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.LLVM = ""
        self.counter = Counter()

    def visitDeclaration(self, node):
        self.LLVM += '%' + str(self.counter) + " = alloca "
        self.counter.incr()
        check = node.children[0].type
        if "const" in check:
            print("extra line for const type after the specification of the type (store ...)")
            check = check.replace("const", "")
        check = check.replace("unsigned", "")
        check = check.replace("signed", "")

        self.LLVM += typeToLLVM(check) + "\n"

    def visitDefinition(self, node):
        self.LLVM += "store "
        #Literal Node
        self.LLVM += node.children[1].type + ' ' + str(node.children[1].value) + ", " + "lookinhash \n"

    def visitAssignment(self, node):
        self.LLVM += "store "
        # Literal Node
        self.LLVM += node.children[1].type + ' ' + str(node.children[1].value) + ", " + "lookinhash \n"

    def visitUnaryOperation(self, node):
        # TODO: NOG TESTEN
        # nogfunctie voor loading maybe
        self.LLVM += '%' + str(self.counter) + " = "
        temp = unaryOpToLLVM(node.operation)
        self.LLVM += temp[0] + " lookinhash ," + temp[1] + "\n"

    def visitBinaryOperation(self, node):
        self.LLVM += '%' + str(self.counter) + " = " + BinaryOpToLLVM(node.operation) + ' '
        for child in node.children:
            if isinstance(child, LiteralNode):
                self.LLVM += "easy to determine"
            else:
                self.LLVM += "lookinhash"
            if child != node.children[-1]:
                self.LLVM += ', '

        self.LLVM += "\n"
