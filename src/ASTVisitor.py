
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

    def visitFunctionDefinition(self, node):
        # print("Visiting Function Definition Node")
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

    def visitFunctionDeclaration(self, node):
        # print("Visiting Function Declaration Node")
        pass

    def visitScope(self, node):
        # print("Visiting Scope Node")
        pass

    def visitWhile(self, node):
        # print("Visiting While Node")
        pass

    def visitBranch(self, node):
        # print("Visiting Branch Node")
        pass

    def visitIf(self, node):
        # print("Visiting If Node")
        pass

    def visitElif(self, node):
        # print("Visiting Elif Node")
        pass

    def visitElse(self, node):
        # print("Visiting Else Node")
        pass

    def visitBreak(self, node):
        # print("Visiting Break Node")
        pass

    def visitContinue(self, node):
        # print("Visiting Continue Node")
        pass

    def visitFunctionCall(self, node):
        # print("Visiting Function Call Node")
        pass