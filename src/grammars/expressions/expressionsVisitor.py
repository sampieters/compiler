# Generated from ./src/grammars/expressions/expressions.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .expressionsParser import expressionsParser
else:
    from expressionsParser import expressionsParser

# This class defines a complete generic visitor for a parse tree produced by expressionsParser.

class expressionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by expressionsParser#Program.
    def visitProgram(self, ctx:expressionsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#Expression.
    def visitExpression(self, ctx:expressionsParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#Integer.
    def visitInteger(self, ctx:expressionsParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#UnaryOp.
    def visitUnaryOp(self, ctx:expressionsParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#Brackets.
    def visitBrackets(self, ctx:expressionsParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx:expressionsParser.UnaryOpBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#BinaryOp.
    def visitBinaryOp(self, ctx:expressionsParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx:expressionsParser.BinaryOpBooleanContext):
        return self.visitChildren(ctx)



del expressionsParser