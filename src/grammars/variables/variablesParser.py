# Generated from src/grammars/variables/variables.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\67\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4H\n\4\f\4\16\4K\13\4\3\5\5\5")
        buf.write("N\n\5\3\5\5\5Q\n\5\3\5\3\5\5\5U\n\5\3\5\5\5X\n\5\3\5\3")
        buf.write("\5\5\5\\\n\5\5\5^\n\5\3\6\3\6\3\6\3\6\5\6d\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\2\3\6\n\2\4\6")
        buf.write("\b\n\f\16\20\2\f\4\2\3\3\30\30\3\2\22\23\3\2\5\6\4\2\3")
        buf.write("\4\13\13\4\2\7\b\f\r\4\2\t\t\16\16\3\2\17\20\3\2\34\35")
        buf.write("\4\2\36!\'\'\3\2#%\2\u0081\2\23\3\2\2\2\4#\3\2\2\2\6\66")
        buf.write("\3\2\2\2\b]\3\2\2\2\nc\3\2\2\2\fe\3\2\2\2\16h\3\2\2\2")
        buf.write("\20l\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2")
        buf.write("\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\30\5\16\b")
        buf.write("\2\30\31\7\26\2\2\31$\3\2\2\2\32\33\5\f\7\2\33\34\7\26")
        buf.write("\2\2\34$\3\2\2\2\35\36\5\20\t\2\36\37\7\26\2\2\37$\3\2")
        buf.write("\2\2 !\5\6\4\2!\"\7\26\2\2\"$\3\2\2\2#\27\3\2\2\2#\32")
        buf.write("\3\2\2\2#\35\3\2\2\2# \3\2\2\2$\5\3\2\2\2%&\b\4\1\2&\'")
        buf.write("\7\24\2\2\'(\5\6\4\2()\7\25\2\2)\67\3\2\2\2*+\t\2\2\2")
        buf.write("+\67\7*\2\2,-\t\3\2\2-\67\7*\2\2./\7*\2\2/\67\t\3\2\2")
        buf.write("\60\61\t\4\2\2\61\67\5\6\4\13\62\63\7\21\2\2\63\67\5\6")
        buf.write("\4\n\64\67\5\n\6\2\65\67\7*\2\2\66%\3\2\2\2\66*\3\2\2")
        buf.write("\2\66,\3\2\2\2\66.\3\2\2\2\66\60\3\2\2\2\66\62\3\2\2\2")
        buf.write("\66\64\3\2\2\2\66\65\3\2\2\2\67I\3\2\2\289\f\t\2\29:\t")
        buf.write("\5\2\2:H\5\6\4\n;<\f\b\2\2<=\t\4\2\2=H\5\6\4\t>?\f\7\2")
        buf.write("\2?@\t\6\2\2@H\5\6\4\bAB\f\6\2\2BC\t\7\2\2CH\5\6\4\7D")
        buf.write("E\f\5\2\2EF\t\b\2\2FH\5\6\4\6G8\3\2\2\2G;\3\2\2\2G>\3")
        buf.write("\2\2\2GA\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2")
        buf.write("\2J\7\3\2\2\2KI\3\2\2\2LN\7\33\2\2ML\3\2\2\2MN\3\2\2\2")
        buf.write("NP\3\2\2\2OQ\t\t\2\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RT\t")
        buf.write("\n\2\2SU\7\3\2\2TS\3\2\2\2TU\3\2\2\2U^\3\2\2\2VX\7\33")
        buf.write("\2\2WV\3\2\2\2WX\3\2\2\2XY\3\2\2\2Y[\t\13\2\2Z\\\7\3\2")
        buf.write("\2[Z\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]M\3\2\2\2]W\3\2\2\2")
        buf.write("^\t\3\2\2\2_d\7&\2\2`d\7\"\2\2ad\7)\2\2bd\7(\2\2c_\3\2")
        buf.write("\2\2c`\3\2\2\2ca\3\2\2\2cb\3\2\2\2d\13\3\2\2\2ef\5\b\5")
        buf.write("\2fg\7*\2\2g\r\3\2\2\2hi\5\f\7\2ij\7\n\2\2jk\5\6\4\2k")
        buf.write("\17\3\2\2\2lm\7*\2\2mn\7\n\2\2no\5\6\4\2o\21\3\2\2\2\16")
        buf.write("\25#\66GIMPTW[]c")
        return buf.getvalue()


class variablesParser ( Parser ):

    grammarFileName = "variables.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", 
                     "'=='", "'='", "'%'", "'<='", "'>='", "'!='", "'&&'", 
                     "'||'", "'!'", "'++'", "'--'", "'('", "')'", "';'", 
                     "'.'", "'&'", "'''", "'\\'", "'const'", "'signed'", 
                     "'unsigned'", "'int'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'float'", "'double'", "'long double'", 
                     "<INVALID>", "'char'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "ADD", "SUB", "LT", "GT", 
                      "DEQ", "EQ", "MOD", "LTE", "GTE", "NEQ", "AND", "OR", 
                      "NOT", "INCR", "DECR", "LBRACKET", "RBRACKET", "END_INSTR", 
                      "DOT", "REF", "SQUOTE", "ESC", "CONST", "SIGNED", 
                      "UNSIGNED", "INT_PREF", "SHORT_PREF", "LONG_PREF", 
                      "LONG_LONG_PREF", "INT", "FLOAT_PREF", "DOUBLE_PREF", 
                      "LONG_DOUBLE_PREF", "FLOAT", "CHAR_PREF", "CHAR", 
                      "STRING", "ID", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_type_specifier = 3
    RULE_literal = 4
    RULE_declaration = 5
    RULE_definition = 6
    RULE_assignment = 7

    ruleNames =  [ "prog", "stat", "expr", "type_specifier", "literal", 
                   "declaration", "definition", "assignment" ]

    EOF = Token.EOF
    MUL=1
    DIV=2
    ADD=3
    SUB=4
    LT=5
    GT=6
    DEQ=7
    EQ=8
    MOD=9
    LTE=10
    GTE=11
    NEQ=12
    AND=13
    OR=14
    NOT=15
    INCR=16
    DECR=17
    LBRACKET=18
    RBRACKET=19
    END_INSTR=20
    DOT=21
    REF=22
    SQUOTE=23
    ESC=24
    CONST=25
    SIGNED=26
    UNSIGNED=27
    INT_PREF=28
    SHORT_PREF=29
    LONG_PREF=30
    LONG_LONG_PREF=31
    INT=32
    FLOAT_PREF=33
    DOUBLE_PREF=34
    LONG_DOUBLE_PREF=35
    FLOAT=36
    CHAR_PREF=37
    CHAR=38
    STRING=39
    ID=40
    WS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return variablesParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(variablesParser.StatContext)
            else:
                return self.getTypedRuleContext(variablesParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = variablesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = variablesParser.ProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stat()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << variablesParser.MUL) | (1 << variablesParser.ADD) | (1 << variablesParser.SUB) | (1 << variablesParser.NOT) | (1 << variablesParser.INCR) | (1 << variablesParser.DECR) | (1 << variablesParser.LBRACKET) | (1 << variablesParser.REF) | (1 << variablesParser.CONST) | (1 << variablesParser.SIGNED) | (1 << variablesParser.UNSIGNED) | (1 << variablesParser.INT_PREF) | (1 << variablesParser.SHORT_PREF) | (1 << variablesParser.LONG_PREF) | (1 << variablesParser.LONG_LONG_PREF) | (1 << variablesParser.INT) | (1 << variablesParser.FLOAT_PREF) | (1 << variablesParser.DOUBLE_PREF) | (1 << variablesParser.LONG_DOUBLE_PREF) | (1 << variablesParser.FLOAT) | (1 << variablesParser.CHAR_PREF) | (1 << variablesParser.CHAR) | (1 << variablesParser.STRING) | (1 << variablesParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return variablesParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefinitionStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def definition(self):
            return self.getTypedRuleContext(variablesParser.DefinitionContext,0)

        def END_INSTR(self):
            return self.getToken(variablesParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitionStatement" ):
                listener.enterDefinitionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitionStatement" ):
                listener.exitDefinitionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionStatement" ):
                return visitor.visitDefinitionStatement(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(variablesParser.AssignmentContext,0)

        def END_INSTR(self):
            return self.getToken(variablesParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)

        def END_INSTR(self):
            return self.getToken(variablesParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(variablesParser.DeclarationContext,0)

        def END_INSTR(self):
            return self.getToken(variablesParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = variablesParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = variablesParser.DefinitionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.definition()
                self.state = 22
                self.match(variablesParser.END_INSTR)
                pass

            elif la_ == 2:
                localctx = variablesParser.DeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.declaration()
                self.state = 25
                self.match(variablesParser.END_INSTR)
                pass

            elif la_ == 3:
                localctx = variablesParser.AssignmentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.assignment()
                self.state = 28
                self.match(variablesParser.END_INSTR)
                pass

            elif la_ == 4:
                localctx = variablesParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(variablesParser.END_INSTR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return variablesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)

        def ADD(self):
            return self.getToken(variablesParser.ADD, 0)
        def SUB(self):
            return self.getToken(variablesParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(variablesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class BracketsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACKET(self):
            return self.getToken(variablesParser.LBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)

        def RBRACKET(self):
            return self.getToken(variablesParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOpPointerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(variablesParser.ID, 0)
        def MUL(self):
            return self.getToken(variablesParser.MUL, 0)
        def REF(self):
            return self.getToken(variablesParser.REF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpPointer" ):
                listener.enterUnaryOpPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpPointer" ):
                listener.exitUnaryOpPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOpPointer" ):
                return visitor.visitUnaryOpPointer(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(variablesParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOpIdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(variablesParser.ID, 0)
        def INCR(self):
            return self.getToken(variablesParser.INCR, 0)
        def DECR(self):
            return self.getToken(variablesParser.DECR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpIdentifier" ):
                listener.enterUnaryOpIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpIdentifier" ):
                listener.exitUnaryOpIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOpIdentifier" ):
                return visitor.visitUnaryOpIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOpBooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)

        def NOT(self):
            return self.getToken(variablesParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpBoolean" ):
                listener.enterUnaryOpBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpBoolean" ):
                listener.exitUnaryOpBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOpBoolean" ):
                return visitor.visitUnaryOpBoolean(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(variablesParser.ExprContext)
            else:
                return self.getTypedRuleContext(variablesParser.ExprContext,i)

        def MUL(self):
            return self.getToken(variablesParser.MUL, 0)
        def DIV(self):
            return self.getToken(variablesParser.DIV, 0)
        def MOD(self):
            return self.getToken(variablesParser.MOD, 0)
        def ADD(self):
            return self.getToken(variablesParser.ADD, 0)
        def SUB(self):
            return self.getToken(variablesParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOpBooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(variablesParser.ExprContext)
            else:
                return self.getTypedRuleContext(variablesParser.ExprContext,i)

        def LT(self):
            return self.getToken(variablesParser.LT, 0)
        def GT(self):
            return self.getToken(variablesParser.GT, 0)
        def LTE(self):
            return self.getToken(variablesParser.LTE, 0)
        def GTE(self):
            return self.getToken(variablesParser.GTE, 0)
        def DEQ(self):
            return self.getToken(variablesParser.DEQ, 0)
        def NEQ(self):
            return self.getToken(variablesParser.NEQ, 0)
        def AND(self):
            return self.getToken(variablesParser.AND, 0)
        def OR(self):
            return self.getToken(variablesParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOpBoolean" ):
                listener.enterBinaryOpBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOpBoolean" ):
                listener.exitBinaryOpBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOpBoolean" ):
                return visitor.visitBinaryOpBoolean(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = variablesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = variablesParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(variablesParser.LBRACKET)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(variablesParser.RBRACKET)
                pass

            elif la_ == 2:
                localctx = variablesParser.UnaryOpPointerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==variablesParser.MUL or _la==variablesParser.REF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.match(variablesParser.ID)
                pass

            elif la_ == 3:
                localctx = variablesParser.UnaryOpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==variablesParser.INCR or _la==variablesParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self.match(variablesParser.ID)
                pass

            elif la_ == 4:
                localctx = variablesParser.UnaryOpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(variablesParser.ID)
                self.state = 45
                _la = self._input.LA(1)
                if not(_la==variablesParser.INCR or _la==variablesParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                localctx = variablesParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==variablesParser.ADD or _la==variablesParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.expr(9)
                pass

            elif la_ == 6:
                localctx = variablesParser.UnaryOpBooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 48
                self.match(variablesParser.NOT)
                self.state = 49
                self.expr(8)
                pass

            elif la_ == 7:
                localctx = variablesParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.literal()
                pass

            elif la_ == 8:
                localctx = variablesParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(variablesParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = variablesParser.BinaryOpContext(self, variablesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << variablesParser.MUL) | (1 << variablesParser.DIV) | (1 << variablesParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = variablesParser.BinaryOpContext(self, variablesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==variablesParser.ADD or _la==variablesParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = variablesParser.BinaryOpBooleanContext(self, variablesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << variablesParser.LT) | (1 << variablesParser.GT) | (1 << variablesParser.LTE) | (1 << variablesParser.GTE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = variablesParser.BinaryOpBooleanContext(self, variablesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 64
                        _la = self._input.LA(1)
                        if not(_la==variablesParser.DEQ or _la==variablesParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = variablesParser.BinaryOpBooleanContext(self, variablesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 67
                        _la = self._input.LA(1)
                        if not(_la==variablesParser.AND or _la==variablesParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.expr(4)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_PREF(self):
            return self.getToken(variablesParser.SHORT_PREF, 0)

        def INT_PREF(self):
            return self.getToken(variablesParser.INT_PREF, 0)

        def LONG_PREF(self):
            return self.getToken(variablesParser.LONG_PREF, 0)

        def LONG_LONG_PREF(self):
            return self.getToken(variablesParser.LONG_LONG_PREF, 0)

        def CHAR_PREF(self):
            return self.getToken(variablesParser.CHAR_PREF, 0)

        def CONST(self):
            return self.getToken(variablesParser.CONST, 0)

        def MUL(self):
            return self.getToken(variablesParser.MUL, 0)

        def SIGNED(self):
            return self.getToken(variablesParser.SIGNED, 0)

        def UNSIGNED(self):
            return self.getToken(variablesParser.UNSIGNED, 0)

        def FLOAT_PREF(self):
            return self.getToken(variablesParser.FLOAT_PREF, 0)

        def DOUBLE_PREF(self):
            return self.getToken(variablesParser.DOUBLE_PREF, 0)

        def LONG_DOUBLE_PREF(self):
            return self.getToken(variablesParser.LONG_DOUBLE_PREF, 0)

        def getRuleIndex(self):
            return variablesParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = variablesParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==variablesParser.CONST:
                    self.state = 74
                    self.match(variablesParser.CONST)


                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==variablesParser.SIGNED or _la==variablesParser.UNSIGNED:
                    self.state = 77
                    _la = self._input.LA(1)
                    if not(_la==variablesParser.SIGNED or _la==variablesParser.UNSIGNED):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 80
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << variablesParser.INT_PREF) | (1 << variablesParser.SHORT_PREF) | (1 << variablesParser.LONG_PREF) | (1 << variablesParser.LONG_LONG_PREF) | (1 << variablesParser.CHAR_PREF))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==variablesParser.MUL:
                    self.state = 81
                    self.match(variablesParser.MUL)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==variablesParser.CONST:
                    self.state = 84
                    self.match(variablesParser.CONST)


                self.state = 87
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << variablesParser.FLOAT_PREF) | (1 << variablesParser.DOUBLE_PREF) | (1 << variablesParser.LONG_DOUBLE_PREF))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==variablesParser.MUL:
                    self.state = 88
                    self.match(variablesParser.MUL)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return variablesParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(variablesParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(variablesParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class CharacterContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(variablesParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter" ):
                listener.enterCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter" ):
                listener.exitCharacter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacter" ):
                return visitor.visitCharacter(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a variablesParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(variablesParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = variablesParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [variablesParser.FLOAT]:
                localctx = variablesParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(variablesParser.FLOAT)
                pass
            elif token in [variablesParser.INT]:
                localctx = variablesParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(variablesParser.INT)
                pass
            elif token in [variablesParser.STRING]:
                localctx = variablesParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.match(variablesParser.STRING)
                pass
            elif token in [variablesParser.CHAR]:
                localctx = variablesParser.CharacterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(variablesParser.CHAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(variablesParser.Type_specifierContext,0)


        def ID(self):
            return self.getToken(variablesParser.ID, 0)

        def getRuleIndex(self):
            return variablesParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = variablesParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.type_specifier()
            self.state = 100
            self.match(variablesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(variablesParser.DeclarationContext,0)


        def EQ(self):
            return self.getToken(variablesParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)


        def getRuleIndex(self):
            return variablesParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = variablesParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.declaration()
            self.state = 103
            self.match(variablesParser.EQ)
            self.state = 104
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(variablesParser.ID, 0)

        def EQ(self):
            return self.getToken(variablesParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(variablesParser.ExprContext,0)


        def getRuleIndex(self):
            return variablesParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = variablesParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(variablesParser.ID)
            self.state = 107
            self.match(variablesParser.EQ)
            self.state = 108
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




