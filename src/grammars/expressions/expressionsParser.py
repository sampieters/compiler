# Generated from src/grammars/expressions/expressions.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\31\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\'")
        buf.write("\n\4\f\4\16\4*\13\4\3\4\2\3\6\5\2\4\6\2\b\4\2\5\6\20\20")
        buf.write("\4\2\3\4\n\n\3\2\5\6\4\2\7\b\13\f\4\2\t\t\r\r\3\2\16\17")
        buf.write("\2\60\2\t\3\2\2\2\4\r\3\2\2\2\6\30\3\2\2\2\b\n\5\4\3\2")
        buf.write("\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f")
        buf.write("\3\3\2\2\2\r\16\5\6\4\2\16\17\7\25\2\2\17\5\3\2\2\2\20")
        buf.write("\21\b\4\1\2\21\22\7\23\2\2\22\23\5\6\4\2\23\24\7\24\2")
        buf.write("\2\24\31\3\2\2\2\25\26\t\2\2\2\26\31\5\6\4\t\27\31\7\26")
        buf.write("\2\2\30\20\3\2\2\2\30\25\3\2\2\2\30\27\3\2\2\2\31(\3\2")
        buf.write("\2\2\32\33\f\b\2\2\33\34\t\3\2\2\34\'\5\6\4\t\35\36\f")
        buf.write("\7\2\2\36\37\t\4\2\2\37\'\5\6\4\b !\f\6\2\2!\'\t\5\2\2")
        buf.write("\"#\f\5\2\2#\'\t\6\2\2$%\f\4\2\2%\'\t\7\2\2&\32\3\2\2")
        buf.write("\2&\35\3\2\2\2& \3\2\2\2&\"\3\2\2\2&$\3\2\2\2\'*\3\2\2")
        buf.write("\2(&\3\2\2\2()\3\2\2\2)\7\3\2\2\2*(\3\2\2\2\6\13\30&(")
        return buf.getvalue()


class expressionsParser ( Parser ):

    grammarFileName = "expressions.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", 
                     "'=='", "'%'", "'<='", "'>='", "'!='", "'&&'", "'||'", 
                     "'!'", "'++'", "'--'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "ADD", "SUB", "LT", "GT", 
                      "EQ", "MOD", "LTE", "GTE", "NEQ", "AND", "OR", "NOT", 
                      "INCR", "DECR", "LBRACKET", "RBRACKET", "END_INSTR", 
                      "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    MUL=1
    DIV=2
    ADD=3
    SUB=4
    LT=5
    GT=6
    EQ=7
    MOD=8
    LTE=9
    GTE=10
    NEQ=11
    AND=12
    OR=13
    NOT=14
    INCR=15
    DECR=16
    LBRACKET=17
    RBRACKET=18
    END_INSTR=19
    INT=20
    WS=21

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expressionsParser.StatContext)
            else:
                return self.getTypedRuleContext(expressionsParser.StatContext,i)


        def getRuleIndex(self):
            return expressionsParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = expressionsParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << expressionsParser.ADD) | (1 << expressionsParser.SUB) | (1 << expressionsParser.NOT) | (1 << expressionsParser.LBRACKET) | (1 << expressionsParser.INT))) != 0)):
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

        def expr(self):
            return self.getTypedRuleContext(expressionsParser.ExprContext,0)


        def END_INSTR(self):
            return self.getToken(expressionsParser.END_INSTR, 0)

        def getRuleIndex(self):
            return expressionsParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = expressionsParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.expr(0)
            self.state = 12
            self.match(expressionsParser.END_INSTR)
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
            self.unary_op = None # Token
            self.binary_op = None # Token

        def LBRACKET(self):
            return self.getToken(expressionsParser.LBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(expressionsParser.ExprContext)
            else:
                return self.getTypedRuleContext(expressionsParser.ExprContext,i)


        def RBRACKET(self):
            return self.getToken(expressionsParser.RBRACKET, 0)

        def ADD(self):
            return self.getToken(expressionsParser.ADD, 0)

        def SUB(self):
            return self.getToken(expressionsParser.SUB, 0)

        def NOT(self):
            return self.getToken(expressionsParser.NOT, 0)

        def INT(self):
            return self.getToken(expressionsParser.INT, 0)

        def MUL(self):
            return self.getToken(expressionsParser.MUL, 0)

        def DIV(self):
            return self.getToken(expressionsParser.DIV, 0)

        def MOD(self):
            return self.getToken(expressionsParser.MOD, 0)

        def LT(self):
            return self.getToken(expressionsParser.LT, 0)

        def GT(self):
            return self.getToken(expressionsParser.GT, 0)

        def LTE(self):
            return self.getToken(expressionsParser.LTE, 0)

        def GTE(self):
            return self.getToken(expressionsParser.GTE, 0)

        def EQ(self):
            return self.getToken(expressionsParser.EQ, 0)

        def NEQ(self):
            return self.getToken(expressionsParser.NEQ, 0)

        def AND(self):
            return self.getToken(expressionsParser.AND, 0)

        def OR(self):
            return self.getToken(expressionsParser.OR, 0)

        def getRuleIndex(self):
            return expressionsParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = expressionsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [expressionsParser.LBRACKET]:
                self.state = 15
                self.match(expressionsParser.LBRACKET)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(expressionsParser.RBRACKET)
                pass
            elif token in [expressionsParser.ADD, expressionsParser.SUB, expressionsParser.NOT]:
                self.state = 19
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << expressionsParser.ADD) | (1 << expressionsParser.SUB) | (1 << expressionsParser.NOT))) != 0)):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.expr(7)
                pass
            elif token in [expressionsParser.INT]:
                self.state = 21
                self.match(expressionsParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = expressionsParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 25
                        localctx.binary_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << expressionsParser.MUL) | (1 << expressionsParser.DIV) | (1 << expressionsParser.MOD))) != 0)):
                            localctx.binary_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 26
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = expressionsParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 28
                        localctx.binary_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==expressionsParser.ADD or _la==expressionsParser.SUB):
                            localctx.binary_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = expressionsParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.binary_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << expressionsParser.LT) | (1 << expressionsParser.GT) | (1 << expressionsParser.LTE) | (1 << expressionsParser.GTE))) != 0)):
                            localctx.binary_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

                    elif la_ == 4:
                        localctx = expressionsParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        localctx.binary_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==expressionsParser.EQ or _la==expressionsParser.NEQ):
                            localctx.binary_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

                    elif la_ == 5:
                        localctx = expressionsParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        localctx.binary_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==expressionsParser.AND or _la==expressionsParser.OR):
                            localctx.binary_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




