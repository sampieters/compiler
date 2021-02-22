# Generated from src/grammars/expressions/expressions.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .expressionsParser import expressionsParser
else:
    from expressionsParser import expressionsParser

# This class defines a complete generic visitor for a parse tree produced by expressionsParser.

class expressionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by expressionsParser#prog.
    def visitProg(self, ctx:expressionsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#stat.
    def visitStat(self, ctx:expressionsParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by expressionsParser#expr.
    def visitExpr(self, ctx:expressionsParser.ExprContext):
        return self.visitChildren(ctx)



del expressionsParser