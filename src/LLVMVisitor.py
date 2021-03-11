from .ASTVisitor import *
from .ASTNode import *
from .utils import *


class LLVMVisitor(ASTVisitor):
    def __init__(self):
        self.LLVM = ""

    def visitBinaryOperation(self, node):
        self.LLVM += "add "

        great_type = getAccType(node.children[0].type, node.children[1].type)
        self.LLVM += typeToLLVM(great_type) + " "

        if isinstance(node.children[0], IdentifierNode):
            self.LLVM += "%" + node.children[0].name
        elif isinstance(node.children[0], LiteralNode):
            self.LLVM += node.children[0].value
        else:
            print("Binary or unary operation")

        self.LLVM += ", "

        if isinstance(node.children[1], IdentifierNode):
            self.LLVM += node.children[1].name
        elif isinstance(node.children[1], LiteralNode):
            self.LLVM += node.children[1].value
        else:
            print("Binary or unary operation")


