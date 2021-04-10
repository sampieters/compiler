
class ASTVisitor:
    def visit(self, tree):
        tree.accept(self)

    def enterProg(self, node):
        # print("Entering Prog Node")
        pass

    def exitProg(self, node):
        # print("Exiting Prog Node")
        pass

    def enterLiteral(self, node):
        # print("Entering Literal Node")
        pass

    def exitLiteral(self, node):
        # print("Exiting Literal Node")
        pass

    def enterIdentifier(self, node):
        # print("Entering Identifier Node")
        pass

    def exitIdentifier(self, node):
        # print("Exiting Identifier Node")
        pass

    def enterDefinition(self, node):
        # print("Entering Definition Node")
        pass

    def exitDefinition(self, node):
        # print("Exiting Definition Node")
        pass

    def enterFunctionDefinition(self, node):
        # print("Entering Function Definition Node")
        pass

    def exitFunctionDefinition(self, node):
        # print("Exiting Function Definition Node")
        pass

    def enterUnaryOperation(self, node):
        # print("Entering Unary Operation Node")
        pass

    def exitUnaryOperation(self, node):
        # print("Exiting Unary Operation Node")
        pass

    def enterBinaryOperation(self, node):
        # print("Entering Binary Operation Node")
        pass

    def exitBinaryOperation(self, node):
        # print("Exiting Binary Operation Node")
        pass

    def enterAssignment(self, node):
        # print("Entering Assignment Node")
        pass

    def exitAssignment(self, node):
        # print("Exiting Assignment Node")
        pass

    def enterDeclaration(self, node):
        # print("Entering Declaration Node")
        pass

    def exitDeclaration(self, node):
        # print("Exiting Declaration Node")
        pass

    def enterFunctionDeclaration(self, node):
        #print("Entering Function Declaration Node")
        pass

    def exitFunctionDeclaration(self, node):
        # print("Exiting Function Declaration Node")
        pass

    def enterScope(self, node):
        # print("Entering Scope Node")
        pass

    def exitScope(self, node):
        # print("Exiting Scope Node")
        pass

    def enterWhile(self, node):
        # print("Entering While Node")
        pass

    def exitWhile(self, node):
        # print("Exiting While Node")
        pass

    def enterBranch(self, node):
        # print("Entering Branch Node")
        pass

    def exitBranch(self, node):
        # print("Exiting Branch Node")
        pass

    def enterIf(self, node):
        # print("Entering If Node")
        pass

    def exitIf(self, node):
        # print("Exiting If Node")
        pass

    def enterElif(self, node):
        # print("Entering Elif Node")
        pass

    def exitElif(self, node):
        # print("Exiting Elif Node")
        pass

    def enterElse(self, node):
        # print("Entering Else Node")
        pass

    def exitElse(self, node):
        # print("Exiting Else Node")
        pass

    def enterBreak(self, node):
        # print("Entering Break Node")
        pass

    def exitBreak(self, node):
        # print("Exiting Break Node")
        pass

    def enterContinue(self, node):
        # print("Entering Continue Node")
        pass

    def exitContinue(self, node):
        # print("Exiting Continue Node")
        pass

    def enterReturn(self, node):
        # print("Entering Return Node")
        pass

    def exitReturn(self, node):
        # print("Exiting Return Node")
        pass

    def enterFunctionCall(self, node):
        # print("Entering Function Call Node")
        pass

    def exitFunctionCall(self, node):
        # print("Exiting Function Call Node")
        pass

    def enterFunction(self, node):
        # print("Entering Function Node")
        pass

    def exitFunction(self, node):
        # print("Exiting Function Node")
        pass

    def enterArgList(self, node):
        # print("Entering Arg List Node")
        pass

    def exitArgList(self, node):
        # print("Exiting Arg List Node")
        pass
