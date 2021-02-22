# Generated from src/grammars/expressions/expressions.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .expressionsParser import expressionsParser
else:
    from expressionsParser import expressionsParser

# This class defines a complete listener for a parse tree produced by expressionsParser.
class expressionsListener(ParseTreeListener):

    # Enter a parse tree produced by expressionsParser#prog.
    def enterProg(self, ctx:expressionsParser.ProgContext):
        pass

    # Exit a parse tree produced by expressionsParser#prog.
    def exitProg(self, ctx:expressionsParser.ProgContext):
        pass


    # Enter a parse tree produced by expressionsParser#stat.
    def enterStat(self, ctx:expressionsParser.StatContext):
        pass

    # Exit a parse tree produced by expressionsParser#stat.
    def exitStat(self, ctx:expressionsParser.StatContext):
        pass


    # Enter a parse tree produced by expressionsParser#expr.
    def enterExpr(self, ctx:expressionsParser.ExprContext):
        pass

    # Exit a parse tree produced by expressionsParser#expr.
    def exitExpr(self, ctx:expressionsParser.ExprContext):
        pass



del expressionsParser