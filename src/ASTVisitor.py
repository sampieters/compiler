
class ASTVisitor:
    def visit(self, tree):
        tree.accept(self)

    def visitProg(self, node):
        # print("Visiting Prog Node")
        pass

    def visitLiteral(self, node):
        # print("Visiting Literal Node")
        pass

    def visitIdentifier(self, node):
        # print("Visiting Identifier Node")
        pass

    def visitDefinition(self, node):
        # print("Visiting Definition Node")
        pass

    def visitUnaryOperation(self, node):
        # print("Visiting Unary Operation Node")
        pass

    def visitBinaryOperation(self, node):
        # print("Visiting Binary Operation Node")
        pass

    def visitAssignment(self, node):
        # print("Visiting Assignment Node")
        pass

    def visitDeclaration(self, node):
        # print("Visiting Declaration Node")
        pass
