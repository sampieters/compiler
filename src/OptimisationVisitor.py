from ASTVisitor import ASTVisitor
from ASTNode import *
from utils import *

class OptimisationVisitor(ASTVisitor):
    def exitUnaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.exitUnaryOpBoolean(node)
        else:
            self.exitUnaryOp(node)

    def exitUnaryOp(self, node):
        if isinstance(node.children[0], LiteralNode) and node.operation not in ["[]", "x++", "++x", "x--", "--x"]:
            node.fold(node.children[0].type)     

    def exitUnaryOpBoolean(self, node):
        if isinstance(node.children[0], LiteralNode):
            node.fold("i32")

    def exitBinaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.exitBinaryOpBoolean(node)
        else:
            self.exitBinaryOp(node)

    def exitBinaryOp(self, node):
        if isinstance(node.children[0], LiteralNode) and isinstance(node.children[1], LiteralNode):
            node.fold(getBinaryType(node.children[0].type, node.children[1].type))

    def exitBinaryOpBoolean(self, node):
        if isinstance(node.children[0], LiteralNode) and isinstance(node.children[1], LiteralNode):
            node.fold("i32")