# Generated from ./src/grammars/expressions/expressions.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("i\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\7\25^\n\25\f\25\16\25a")
        buf.write("\13\25\3\26\6\26d\n\26\r\26\16\26e\3\26\3\26\2\2\27\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\5\3\2")
        buf.write("\63;\3\2\62;\5\2\13\f\17\17\"\"\2j\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5/\3\2\2\2\7\61\3\2")
        buf.write("\2\2\t\63\3\2\2\2\13\65\3\2\2\2\r\67\3\2\2\2\179\3\2\2")
        buf.write("\2\21<\3\2\2\2\23>\3\2\2\2\25A\3\2\2\2\27D\3\2\2\2\31")
        buf.write("G\3\2\2\2\33J\3\2\2\2\35M\3\2\2\2\37O\3\2\2\2!R\3\2\2")
        buf.write("\2#U\3\2\2\2%W\3\2\2\2\'Y\3\2\2\2)[\3\2\2\2+c\3\2\2\2")
        buf.write("-.\7,\2\2.\4\3\2\2\2/\60\7\61\2\2\60\6\3\2\2\2\61\62\7")
        buf.write("-\2\2\62\b\3\2\2\2\63\64\7/\2\2\64\n\3\2\2\2\65\66\7>")
        buf.write("\2\2\66\f\3\2\2\2\678\7@\2\28\16\3\2\2\29:\7?\2\2:;\7")
        buf.write("?\2\2;\20\3\2\2\2<=\7\'\2\2=\22\3\2\2\2>?\7>\2\2?@\7?")
        buf.write("\2\2@\24\3\2\2\2AB\7@\2\2BC\7?\2\2C\26\3\2\2\2DE\7#\2")
        buf.write("\2EF\7?\2\2F\30\3\2\2\2GH\7(\2\2HI\7(\2\2I\32\3\2\2\2")
        buf.write("JK\7~\2\2KL\7~\2\2L\34\3\2\2\2MN\7#\2\2N\36\3\2\2\2OP")
        buf.write("\7-\2\2PQ\7-\2\2Q \3\2\2\2RS\7/\2\2ST\7/\2\2T\"\3\2\2")
        buf.write("\2UV\7*\2\2V$\3\2\2\2WX\7+\2\2X&\3\2\2\2YZ\7=\2\2Z(\3")
        buf.write("\2\2\2[_\t\2\2\2\\^\t\3\2\2]\\\3\2\2\2^a\3\2\2\2_]\3\2")
        buf.write("\2\2_`\3\2\2\2`*\3\2\2\2a_\3\2\2\2bd\t\4\2\2cb\3\2\2\2")
        buf.write("de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\b\26\2\2h,")
        buf.write("\3\2\2\2\5\2_e\3\b\2\2")
        return buf.getvalue()


class expressionsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MUL = 1
    DIV = 2
    ADD = 3
    SUB = 4
    LT = 5
    GT = 6
    EQ = 7
    MOD = 8
    LTE = 9
    GTE = 10
    NEQ = 11
    AND = 12
    OR = 13
    NOT = 14
    INCR = 15
    DECR = 16
    LBRACKET = 17
    RBRACKET = 18
    END_INSTR = 19
    INT = 20
    WS = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", "'%'", "'<='", 
            "'>='", "'!='", "'&&'", "'||'", "'!'", "'++'", "'--'", "'('", 
            "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "LT", "GT", "EQ", "MOD", "LTE", 
            "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", "LBRACKET", 
            "RBRACKET", "END_INSTR", "INT", "WS" ]

    ruleNames = [ "MUL", "DIV", "ADD", "SUB", "LT", "GT", "EQ", "MOD", "LTE", 
                  "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", "LBRACKET", 
                  "RBRACKET", "END_INSTR", "INT", "WS" ]

    grammarFileName = "expressions.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


