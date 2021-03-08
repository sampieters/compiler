from ASTNode import *

class ASTVisitor:
    def visit(self, tree):
        tree.accept(self)

    def visitProg(self, node):
        print("Visiting Prog Node")
        return node.accept(self)

    def visitLiteral(self, node):
        print("Visiting Literal Node")
        return node.accept(self)

    def visitIdentifier(self, node):
        print("Visiting Identifier Node")
        return node.accept(self)

    def visitDefinition(self, node):
        print("Visiting Definition Node")
        return node.accept(self)

    def visitUnaryOperation(self, node):
        print("Visiting Unary Operation Node")
        return node.accept(self)

    def visitBinaryOperation(self, node):
        print("Visiting Binary Operation Node")
        return node.accept(self)

    def visitAssignment(self, node):
        print("Visiting Assignment Node")
        return node.accept(self)

    def visitDeclaration(self, node):
        print("Visiting Declaration Node")
        return node.accept(self)