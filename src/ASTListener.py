from grammars.expressions.expressionsListener import expressionsListener
class ASTListener(expressionsListener):
    # Enter a parse tree produced by expressionsParser#prog.
    def enterProg(self, ctx:expressionsParser.ProgContext):
        print("ENTERING PROGRAM")

    # Exit a parse tree produced by expressionsParser#prog.
    def exitProg(self, ctx:expressionsParser.ProgContext):
        print("ENTERING PROGRAM")

    # Enter a parse tree produced by expressionsParser#stat.
    def enterStat(self, ctx:expressionsParser.StatContext):
        print("ENTERING PROGRAM")

    # Exit a parse tree produced by expressionsParser#stat.
    def exitStat(self, ctx:expressionsParser.StatContext):
        print("ENTERING PROGRAM")


    # Enter a parse tree produced by expressionsParser#expr.
    def enterExpr(self, ctx:expressionsParser.ExprContext):
        print("ENTERING PROGRAM")

    # Exit a parse tree produced by expressionsParser#expr.
    def exitExpr(self, ctx:expressionsParser.ExprContext):
        print("ENTERING PROGRAM")
