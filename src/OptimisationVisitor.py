from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor
from ASTVisitor import ASTVisitor
from ASTNode import *
from utils import *

class OptimisationVisitor(ASTVisitor):
    def visitUnaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.visitUnaryOpBoolean(node)
        else:
            self.visitUnaryOp(node)

    def visitUnaryOp(self, node):
        if isinstance(node.children[0], LiteralNode):
            node.fold(node.children[0].type)     

    def visitUnaryOpBoolean(self, node):
        if isinstance(node.children[0], LiteralNode):
            node.fold("int")

    def visitBinaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.visitBinaryOpBoolean(node)
        else:
            self.visitBinaryOp(node)

    def visitBinaryOp(self, node):
        if isinstance(node.children[0], LiteralNode) and isinstance(node.children[1], LiteralNode):
            node.fold(getBinaryType(node.children[0].type, node.children[1].type))

    def visitBinaryOpBoolean(self, node):
        if isinstance(node.children[0], LiteralNode) and isinstance(node.children[1], LiteralNode):
            node.fold("int")