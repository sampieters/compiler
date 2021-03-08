from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor
from ASTVisitor import ASTVisitor
from ASTNode import *

class OptimisationVisitor(ASTVisitor):
    def visitUnaryOperation(self, node):
        if isinstance(node.children[0], LiteralNode):
            node.fold()
            
    def visitBinaryOperation(self, node):
        if isinstance(node.children[0], LiteralNode) and isinstance(node.children[1], LiteralNode):
            node.fold()
