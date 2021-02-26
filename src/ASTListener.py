from grammars.expressions.expressionsListener import expressionsListener
from ASTNode import ASTNode
class ASTListener(expressionsListener):
    def __init__(self, root_node):
        self.curr_node = root_node
        
    def enterProgram(self, ctx:expressionsParser.ProgramContext):
        pass

    # Exit a parse tree produced by expressionsParser#Program.
    def exitProgram(self, ctx:expressionsParser.ProgramContext):
        pass


    # Enter a parse tree produced by expressionsParser#Expression.
    def enterExpression(self, ctx:expressionsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by expressionsParser#Expression.
    def exitExpression(self, ctx:expressionsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by expressionsParser#Integer.
    def enterInteger(self, ctx:expressionsParser.IntegerContext):
        pass

    # Exit a parse tree produced by expressionsParser#Integer.
    def exitInteger(self, ctx:expressionsParser.IntegerContext):
        pass


    # Enter a parse tree produced by expressionsParser#UnaryOp.
    def enterUnaryOp(self, ctx:expressionsParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by expressionsParser#UnaryOp.
    def exitUnaryOp(self, ctx:expressionsParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by expressionsParser#Brackets.
    def enterBrackets(self, ctx:expressionsParser.BracketsContext):
        pass

    # Exit a parse tree produced by expressionsParser#Brackets.
    def exitBrackets(self, ctx:expressionsParser.BracketsContext):
        pass


    # Enter a parse tree produced by expressionsParser#BinaryOp.
    def enterBinaryOp(self, ctx:expressionsParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by expressionsParser#BinaryOp.
    def exitBinaryOp(self, ctx:expressionsParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by expressionsParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:expressionsParser.BinaryOpBooleanContext):
        pass

    # Exit a parse tree produced by expressionsParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:expressionsParser.BinaryOpBooleanContext):
        pass
