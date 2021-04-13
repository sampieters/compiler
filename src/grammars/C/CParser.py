# Generated from src/grammars/C/C.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0125\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\5\2,\n\2\3\2\3\2\6\2\60\n\2\r")
        buf.write("\2\16\2\61\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3N\n\3\3\3\3\3\5\3R\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("f\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4w\n\4\f\4\16\4z\13\4\3\5\3\5\7\5~\n\5")
        buf.write("\f\5\16\5\u0081\13\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u0089")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\5\6\u0090\n\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00a1")
        buf.write("\n\b\f\b\16\b\u00a4\13\b\3\b\5\b\u00a7\n\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\7\13\u00ba\n\13\f\13\16\13\u00bd\13\13\3\13")
        buf.write("\3\13\3\13\5\13\u00c2\n\13\3\13\3\13\3\13\7\13\u00c7\n")
        buf.write("\13\f\13\16\13\u00ca\13\13\3\13\3\13\3\f\5\f\u00cf\n\f")
        buf.write("\3\f\5\f\u00d2\n\f\3\f\3\f\7\f\u00d6\n\f\f\f\16\f\u00d9")
        buf.write("\13\f\3\f\5\f\u00dc\n\f\3\f\3\f\7\f\u00e0\n\f\f\f\16\f")
        buf.write("\u00e3\13\f\3\f\5\f\u00e6\n\f\3\r\3\r\3\r\3\r\5\r\u00ec")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0107\n\23\3\24\3\24\3\24\3")
        buf.write("\24\7\24\u010d\n\24\f\24\16\24\u0110\13\24\3\24\5\24\u0113")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u011b\n\25\f")
        buf.write("\25\16\25\u011e\13\25\3\25\5\25\u0121\n\25\3\25\3\25\3")
        buf.write("\25\2\3\6\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(\2\f\4\2\3\3\33\33\3\2\22\23\3\2\5\6\4\2\3\4\13\13")
        buf.write("\4\2\7\b\f\r\4\2\t\t\16\16\3\2\17\20\3\2 !\5\2\"\"$&,")
        buf.write(",\3\2(*\2\u0145\2+\3\2\2\2\4Q\3\2\2\2\6e\3\2\2\2\b{\3")
        buf.write("\2\2\2\n\u0084\3\2\2\2\f\u0094\3\2\2\2\16\u009a\3\2\2")
        buf.write("\2\20\u00a8\3\2\2\2\22\u00ae\3\2\2\2\24\u00b1\3\2\2\2")
        buf.write("\26\u00e5\3\2\2\2\30\u00eb\3\2\2\2\32\u00ed\3\2\2\2\34")
        buf.write("\u00f0\3\2\2\2\36\u00f4\3\2\2\2 \u00f8\3\2\2\2\"\u00fb")
        buf.write("\3\2\2\2$\u0106\3\2\2\2&\u0108\3\2\2\2(\u0116\3\2\2\2")
        buf.write("*,\7;\2\2+*\3\2\2\2+,\3\2\2\2,/\3\2\2\2-\60\5\4\3\2.\60")
        buf.write("\5\b\5\2/-\3\2\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2")
        buf.write("\61\62\3\2\2\2\62\3\3\2\2\2\63\64\5\36\20\2\64\65\7\30")
        buf.write("\2\2\65R\3\2\2\2\66\67\5\32\16\2\678\7\30\2\28R\3\2\2")
        buf.write("\29:\5\"\22\2:;\7\30\2\2;R\3\2\2\2<=\5\6\4\2=>\7\30\2")
        buf.write("\2>R\3\2\2\2?@\7\65\2\2@R\7\30\2\2AB\7\66\2\2BR\7\30\2")
        buf.write("\2CR\5\n\6\2DR\5\f\7\2ER\5\16\b\2FR\5\24\13\2GH\5\34\17")
        buf.write("\2HI\7\30\2\2IR\3\2\2\2JR\5 \21\2KM\7:\2\2LN\5\6\4\2M")
        buf.write("L\3\2\2\2MN\3\2\2\2NO\3\2\2\2OR\7\30\2\2PR\7\30\2\2Q\63")
        buf.write("\3\2\2\2Q\66\3\2\2\2Q9\3\2\2\2Q<\3\2\2\2Q?\3\2\2\2QA\3")
        buf.write("\2\2\2QC\3\2\2\2QD\3\2\2\2QE\3\2\2\2QF\3\2\2\2QG\3\2\2")
        buf.write("\2QJ\3\2\2\2QK\3\2\2\2QP\3\2\2\2R\5\3\2\2\2ST\b\4\1\2")
        buf.write("TU\7\24\2\2UV\5\6\4\2VW\7\25\2\2Wf\3\2\2\2XY\t\2\2\2Y")
        buf.write("f\7<\2\2Z[\t\3\2\2[f\7<\2\2\\]\7<\2\2]f\t\3\2\2^_\t\4")
        buf.write("\2\2_f\5\6\4\f`a\7\21\2\2af\5\6\4\13bf\5\30\r\2cf\7<\2")
        buf.write("\2df\5$\23\2eS\3\2\2\2eX\3\2\2\2eZ\3\2\2\2e\\\3\2\2\2")
        buf.write("e^\3\2\2\2e`\3\2\2\2eb\3\2\2\2ec\3\2\2\2ed\3\2\2\2fx\3")
        buf.write("\2\2\2gh\f\n\2\2hi\t\5\2\2iw\5\6\4\13jk\f\t\2\2kl\t\4")
        buf.write("\2\2lw\5\6\4\nmn\f\b\2\2no\t\6\2\2ow\5\6\4\tpq\f\7\2\2")
        buf.write("qr\t\7\2\2rw\5\6\4\bst\f\6\2\2tu\t\b\2\2uw\5\6\4\7vg\3")
        buf.write("\2\2\2vj\3\2\2\2vm\3\2\2\2vp\3\2\2\2vs\3\2\2\2wz\3\2\2")
        buf.write("\2xv\3\2\2\2xy\3\2\2\2y\7\3\2\2\2zx\3\2\2\2{\177\7\26")
        buf.write("\2\2|~\5\4\3\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082")
        buf.write("\u0083\7\27\2\2\u0083\t\3\2\2\2\u0084\u0085\7\63\2\2\u0085")
        buf.write("\u0088\7\24\2\2\u0086\u0089\5\36\20\2\u0087\u0089\5\"")
        buf.write("\22\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008b\7\30\2\2\u008b\u008c\5\6\4\2\u008c")
        buf.write("\u008f\7\30\2\2\u008d\u0090\5\6\4\2\u008e\u0090\5\"\22")
        buf.write("\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0092\7\25\2\2\u0092\u0093\5\b\5\2\u0093")
        buf.write("\13\3\2\2\2\u0094\u0095\7\64\2\2\u0095\u0096\7\24\2\2")
        buf.write("\u0096\u0097\5\6\4\2\u0097\u0098\7\25\2\2\u0098\u0099")
        buf.write("\5\b\5\2\u0099\r\3\2\2\2\u009a\u009b\7\60\2\2\u009b\u009c")
        buf.write("\7\24\2\2\u009c\u009d\5\6\4\2\u009d\u009e\7\25\2\2\u009e")
        buf.write("\u00a2\5\b\5\2\u009f\u00a1\5\20\t\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a7\5\22\n\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2")
        buf.write("\2\u00a7\17\3\2\2\2\u00a8\u00a9\7\61\2\2\u00a9\u00aa\7")
        buf.write("\24\2\2\u00aa\u00ab\5\6\4\2\u00ab\u00ac\7\25\2\2\u00ac")
        buf.write("\u00ad\5\b\5\2\u00ad\21\3\2\2\2\u00ae\u00af\7\62\2\2\u00af")
        buf.write("\u00b0\5\b\5\2\u00b0\23\3\2\2\2\u00b1\u00b2\7\67\2\2\u00b2")
        buf.write("\u00b3\7\24\2\2\u00b3\u00b4\5\6\4\2\u00b4\u00b5\7\25\2")
        buf.write("\2\u00b5\u00bb\7\26\2\2\u00b6\u00b7\78\2\2\u00b7\u00b8")
        buf.write("\7\31\2\2\u00b8\u00ba\5\4\3\2\u00b9\u00b6\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00c1\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7")
        buf.write("9\2\2\u00bf\u00c0\7\31\2\2\u00c0\u00c2\5\4\3\2\u00c1\u00be")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c8\3\2\2\2\u00c3")
        buf.write("\u00c4\78\2\2\u00c4\u00c5\7\31\2\2\u00c5\u00c7\5\4\3\2")
        buf.write("\u00c6\u00c3\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00cb\u00cc\7\27\2\2\u00cc\25\3\2\2\2\u00cd\u00cf")
        buf.write("\7\37\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00d2\t\t\2\2\u00d1\u00d0\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d7\t")
        buf.write("\n\2\2\u00d4\u00d6\7\3\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00e6\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dc\7\37\2")
        buf.write("\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00e1\t\13\2\2\u00de\u00e0\7\3\2\2\u00df")
        buf.write("\u00de\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e6\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e4\u00e6\7#\2\2\u00e5\u00ce\3\2\2\2\u00e5\u00db")
        buf.write("\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\27\3\2\2\2\u00e7\u00ec")
        buf.write("\7+\2\2\u00e8\u00ec\7\'\2\2\u00e9\u00ec\7.\2\2\u00ea\u00ec")
        buf.write("\7-\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\31\3\2\2\2\u00ed")
        buf.write("\u00ee\5\26\f\2\u00ee\u00ef\7<\2\2\u00ef\33\3\2\2\2\u00f0")
        buf.write("\u00f1\5\26\f\2\u00f1\u00f2\7<\2\2\u00f2\u00f3\5&\24\2")
        buf.write("\u00f3\35\3\2\2\2\u00f4\u00f5\5\32\16\2\u00f5\u00f6\7")
        buf.write("\n\2\2\u00f6\u00f7\5\6\4\2\u00f7\37\3\2\2\2\u00f8\u00f9")
        buf.write("\5\34\17\2\u00f9\u00fa\5\b\5\2\u00fa!\3\2\2\2\u00fb\u00fc")
        buf.write("\7<\2\2\u00fc\u00fd\7\n\2\2\u00fd\u00fe\5\6\4\2\u00fe")
        buf.write("#\3\2\2\2\u00ff\u0100\7<\2\2\u0100\u0107\5(\25\2\u0101")
        buf.write("\u0102\7/\2\2\u0102\u0103\7\24\2\2\u0103\u0104\5\6\4\2")
        buf.write("\u0104\u0105\7\25\2\2\u0105\u0107\3\2\2\2\u0106\u00ff")
        buf.write("\3\2\2\2\u0106\u0101\3\2\2\2\u0107%\3\2\2\2\u0108\u0112")
        buf.write("\7\24\2\2\u0109\u010a\5\32\16\2\u010a\u010b\7\36\2\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u0109\3\2\2\2\u010d\u0110\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0111\u0113\5\32\16\2\u0112")
        buf.write("\u010e\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0115\7\25\2\2\u0115\'\3\2\2\2\u0116\u0120\7\24")
        buf.write("\2\2\u0117\u0118\5\6\4\2\u0118\u0119\7\36\2\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0117\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011f\u0121\5\6\4\2\u0120\u011c\3")
        buf.write("\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123")
        buf.write("\7\25\2\2\u0123)\3\2\2\2\36+/\61MQevx\177\u0088\u008f")
        buf.write("\u00a2\u00a6\u00bb\u00c1\u00c8\u00ce\u00d1\u00d7\u00db")
        buf.write("\u00e1\u00e5\u00eb\u0106\u010e\u0112\u011c\u0120")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", 
                     "'=='", "'='", "'%'", "'<='", "'>='", "'!='", "'&&'", 
                     "'||'", "'!'", "'++'", "'--'", "'('", "')'", "'{'", 
                     "'}'", "';'", "':'", "'.'", "'&'", "'''", "'\\'", "','", 
                     "'const'", "'signed'", "'unsigned'", "'int'", "'void'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'float'", "'double'", "'long double'", "<INVALID>", 
                     "'char'", "<INVALID>", "<INVALID>", "'printf'", "'if'", 
                     "'else if'", "'else'", "'for'", "'while'", "'break'", 
                     "'continue'", "'switch'", "'case'", "'default'", "'return'", 
                     "'#include <stdio.h>'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "ADD", "SUB", "LT", "GT", 
                      "DEQ", "EQ", "MOD", "LTE", "GTE", "NEQ", "AND", "OR", 
                      "NOT", "INCR", "DECR", "LBRACKET", "RBRACKET", "LCURLY", 
                      "RCURLY", "END_INSTR", "COLON", "DOT", "REF", "SQUOTE", 
                      "ESC", "COMMA", "CONST", "SIGNED", "UNSIGNED", "INT_PREF", 
                      "VOID_PREF", "SHORT_PREF", "LONG_PREF", "LONG_LONG_PREF", 
                      "INT", "FLOAT_PREF", "DOUBLE_PREF", "LONG_DOUBLE_PREF", 
                      "FLOAT", "CHAR_PREF", "CHAR", "STRING", "PRINTF", 
                      "IF", "ELIF", "ELSE", "FOR", "WHILE", "BREAK", "CONTINUE", 
                      "SWITCH", "CASE", "DEFAULT", "RETURN", "INCLUDE_IO", 
                      "ID", "WS", "SINGLE_COMMENT", "MULTI_COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_scope = 3
    RULE_for_stat = 4
    RULE_while_stat = 5
    RULE_if_stat = 6
    RULE_elif_stat = 7
    RULE_else_stat = 8
    RULE_switch_stat = 9
    RULE_type_specifier = 10
    RULE_literal = 11
    RULE_declaration = 12
    RULE_function_declaration = 13
    RULE_definition = 14
    RULE_function_definition = 15
    RULE_assignment = 16
    RULE_function_call = 17
    RULE_arg_list = 18
    RULE_call_list = 19

    ruleNames =  [ "prog", "stat", "expr", "scope", "for_stat", "while_stat", 
                   "if_stat", "elif_stat", "else_stat", "switch_stat", "type_specifier", 
                   "literal", "declaration", "function_declaration", "definition", 
                   "function_definition", "assignment", "function_call", 
                   "arg_list", "call_list" ]

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
    LCURLY=20
    RCURLY=21
    END_INSTR=22
    COLON=23
    DOT=24
    REF=25
    SQUOTE=26
    ESC=27
    COMMA=28
    CONST=29
    SIGNED=30
    UNSIGNED=31
    INT_PREF=32
    VOID_PREF=33
    SHORT_PREF=34
    LONG_PREF=35
    LONG_LONG_PREF=36
    INT=37
    FLOAT_PREF=38
    DOUBLE_PREF=39
    LONG_DOUBLE_PREF=40
    FLOAT=41
    CHAR_PREF=42
    CHAR=43
    STRING=44
    PRINTF=45
    IF=46
    ELIF=47
    ELSE=48
    FOR=49
    WHILE=50
    BREAK=51
    CONTINUE=52
    SWITCH=53
    CASE=54
    DEFAULT=55
    RETURN=56
    INCLUDE_IO=57
    ID=58
    WS=59
    SINGLE_COMMENT=60
    MULTI_COMMENT=61

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
            return CParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INCLUDE_IO(self):
            return self.getToken(CParser.INCLUDE_IO, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatContext)
            else:
                return self.getTypedRuleContext(CParser.StatContext,i)

        def scope(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ScopeContext)
            else:
                return self.getTypedRuleContext(CParser.ScopeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)



    def prog(self):

        localctx = CParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = CParser.ProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.INCLUDE_IO:
                self.state = 40
                self.match(CParser.INCLUDE_IO)


            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CParser.MUL, CParser.ADD, CParser.SUB, CParser.NOT, CParser.INCR, CParser.DECR, CParser.LBRACKET, CParser.END_INSTR, CParser.REF, CParser.CONST, CParser.SIGNED, CParser.UNSIGNED, CParser.INT_PREF, CParser.VOID_PREF, CParser.SHORT_PREF, CParser.LONG_PREF, CParser.LONG_LONG_PREF, CParser.INT, CParser.FLOAT_PREF, CParser.DOUBLE_PREF, CParser.LONG_DOUBLE_PREF, CParser.FLOAT, CParser.CHAR_PREF, CParser.CHAR, CParser.STRING, CParser.PRINTF, CParser.IF, CParser.FOR, CParser.WHILE, CParser.BREAK, CParser.CONTINUE, CParser.SWITCH, CParser.RETURN, CParser.ID]:
                    self.state = 43
                    self.stat()
                    pass
                elif token in [CParser.LCURLY]:
                    self.state = 44
                    self.scope()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.MUL) | (1 << CParser.ADD) | (1 << CParser.SUB) | (1 << CParser.NOT) | (1 << CParser.INCR) | (1 << CParser.DECR) | (1 << CParser.LBRACKET) | (1 << CParser.LCURLY) | (1 << CParser.END_INSTR) | (1 << CParser.REF) | (1 << CParser.CONST) | (1 << CParser.SIGNED) | (1 << CParser.UNSIGNED) | (1 << CParser.INT_PREF) | (1 << CParser.VOID_PREF) | (1 << CParser.SHORT_PREF) | (1 << CParser.LONG_PREF) | (1 << CParser.LONG_LONG_PREF) | (1 << CParser.INT) | (1 << CParser.FLOAT_PREF) | (1 << CParser.DOUBLE_PREF) | (1 << CParser.LONG_DOUBLE_PREF) | (1 << CParser.FLOAT) | (1 << CParser.CHAR_PREF) | (1 << CParser.CHAR) | (1 << CParser.STRING) | (1 << CParser.PRINTF) | (1 << CParser.IF) | (1 << CParser.FOR) | (1 << CParser.WHILE) | (1 << CParser.BREAK) | (1 << CParser.CONTINUE) | (1 << CParser.SWITCH) | (1 << CParser.RETURN) | (1 << CParser.ID))) != 0)):
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
            return CParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)


    class WhileStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_stat(self):
            return self.getTypedRuleContext(CParser.While_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class BreakStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(CParser.BREAK, 0)
        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)


    class IfStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_stat(self):
            return self.getTypedRuleContext(CParser.If_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def switch_stat(self):
            return self.getTypedRuleContext(CParser.Switch_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)


    class DefinitionStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def definition(self):
            return self.getTypedRuleContext(CParser.DefinitionContext,0)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitionStatement" ):
                listener.enterDefinitionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitionStatement" ):
                listener.exitDefinitionStatement(self)


    class FunctionDefinitionStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_definition(self):
            return self.getTypedRuleContext(CParser.Function_definitionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinitionStatement" ):
                listener.enterFunctionDefinitionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinitionStatement" ):
                listener.exitFunctionDefinitionStatement(self)


    class AssignmentStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(CParser.AssignmentContext,0)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)


    class ExpressionStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)


    class ReturnStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(CParser.RETURN, 0)
        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)
        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)


    class ForStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def for_stat(self):
            return self.getTypedRuleContext(CParser.For_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class FunctionDeclarationStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_declaration(self):
            return self.getTypedRuleContext(CParser.Function_declarationContext,0)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclarationStatement" ):
                listener.enterFunctionDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclarationStatement" ):
                listener.exitFunctionDeclarationStatement(self)


    class ContinueStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(CParser.CONTINUE, 0)
        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)


    class DeclarationStatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)

        def END_INSTR(self):
            return self.getToken(CParser.END_INSTR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)



    def stat(self):

        localctx = CParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = CParser.DefinitionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.definition()
                self.state = 50
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 2:
                localctx = CParser.DeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.declaration()
                self.state = 53
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 3:
                localctx = CParser.AssignmentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.assignment()
                self.state = 56
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 4:
                localctx = CParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 5:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(CParser.BREAK)
                self.state = 62
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 6:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.match(CParser.CONTINUE)
                self.state = 64
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 7:
                localctx = CParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.for_stat()
                pass

            elif la_ == 8:
                localctx = CParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.while_stat()
                pass

            elif la_ == 9:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.if_stat()
                pass

            elif la_ == 10:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 68
                self.switch_stat()
                pass

            elif la_ == 11:
                localctx = CParser.FunctionDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 69
                self.function_declaration()
                self.state = 70
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 12:
                localctx = CParser.FunctionDefinitionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 72
                self.function_definition()
                pass

            elif la_ == 13:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 73
                self.match(CParser.RETURN)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.MUL) | (1 << CParser.ADD) | (1 << CParser.SUB) | (1 << CParser.NOT) | (1 << CParser.INCR) | (1 << CParser.DECR) | (1 << CParser.LBRACKET) | (1 << CParser.REF) | (1 << CParser.INT) | (1 << CParser.FLOAT) | (1 << CParser.CHAR) | (1 << CParser.STRING) | (1 << CParser.PRINTF) | (1 << CParser.ID))) != 0):
                    self.state = 74
                    self.expr(0)


                self.state = 77
                self.match(CParser.END_INSTR)
                pass

            elif la_ == 14:
                localctx = CParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 78
                self.match(CParser.END_INSTR)
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
            return CParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)

        def ADD(self):
            return self.getToken(CParser.ADD, 0)
        def SUB(self):
            return self.getToken(CParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)


    class IdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)


    class BracketsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)

        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)


    class UnaryOpIdentifierSuffixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CParser.ID, 0)
        def INCR(self):
            return self.getToken(CParser.INCR, 0)
        def DECR(self):
            return self.getToken(CParser.DECR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpIdentifierSuffix" ):
                listener.enterUnaryOpIdentifierSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpIdentifierSuffix" ):
                listener.exitUnaryOpIdentifierSuffix(self)


    class UnaryOpPointerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CParser.ID, 0)
        def MUL(self):
            return self.getToken(CParser.MUL, 0)
        def REF(self):
            return self.getToken(CParser.REF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpPointer" ):
                listener.enterUnaryOpPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpPointer" ):
                listener.exitUnaryOpPointer(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(CParser.Function_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)


    class UnaryOpBooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)

        def NOT(self):
            return self.getToken(CParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpBoolean" ):
                listener.enterUnaryOpBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpBoolean" ):
                listener.exitUnaryOpBoolean(self)


    class UnaryOpIdentifierPrefixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CParser.ID, 0)
        def INCR(self):
            return self.getToken(CParser.INCR, 0)
        def DECR(self):
            return self.getToken(CParser.DECR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpIdentifierPrefix" ):
                listener.enterUnaryOpIdentifierPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpIdentifierPrefix" ):
                listener.exitUnaryOpIdentifierPrefix(self)


    class BinaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExprContext)
            else:
                return self.getTypedRuleContext(CParser.ExprContext,i)

        def MUL(self):
            return self.getToken(CParser.MUL, 0)
        def DIV(self):
            return self.getToken(CParser.DIV, 0)
        def MOD(self):
            return self.getToken(CParser.MOD, 0)
        def ADD(self):
            return self.getToken(CParser.ADD, 0)
        def SUB(self):
            return self.getToken(CParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)


    class BinaryOpBooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExprContext)
            else:
                return self.getTypedRuleContext(CParser.ExprContext,i)

        def LT(self):
            return self.getToken(CParser.LT, 0)
        def GT(self):
            return self.getToken(CParser.GT, 0)
        def LTE(self):
            return self.getToken(CParser.LTE, 0)
        def GTE(self):
            return self.getToken(CParser.GTE, 0)
        def DEQ(self):
            return self.getToken(CParser.DEQ, 0)
        def NEQ(self):
            return self.getToken(CParser.NEQ, 0)
        def AND(self):
            return self.getToken(CParser.AND, 0)
        def OR(self):
            return self.getToken(CParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOpBoolean" ):
                listener.enterBinaryOpBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOpBoolean" ):
                listener.exitBinaryOpBoolean(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = CParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 82
                self.match(CParser.LBRACKET)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(CParser.RBRACKET)
                pass

            elif la_ == 2:
                localctx = CParser.UnaryOpPointerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                _la = self._input.LA(1)
                if not(_la==CParser.MUL or _la==CParser.REF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 87
                self.match(CParser.ID)
                pass

            elif la_ == 3:
                localctx = CParser.UnaryOpIdentifierPrefixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==CParser.INCR or _la==CParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 89
                self.match(CParser.ID)
                pass

            elif la_ == 4:
                localctx = CParser.UnaryOpIdentifierSuffixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(CParser.ID)
                self.state = 91
                _la = self._input.LA(1)
                if not(_la==CParser.INCR or _la==CParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                localctx = CParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                _la = self._input.LA(1)
                if not(_la==CParser.ADD or _la==CParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self.expr(10)
                pass

            elif la_ == 6:
                localctx = CParser.UnaryOpBooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 94
                self.match(CParser.NOT)
                self.state = 95
                self.expr(9)
                pass

            elif la_ == 7:
                localctx = CParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.literal()
                pass

            elif la_ == 8:
                localctx = CParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(CParser.ID)
                pass

            elif la_ == 9:
                localctx = CParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.function_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CParser.BinaryOpContext(self, CParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 102
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.MUL) | (1 << CParser.DIV) | (1 << CParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = CParser.BinaryOpContext(self, CParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 105
                        _la = self._input.LA(1)
                        if not(_la==CParser.ADD or _la==CParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = CParser.BinaryOpBooleanContext(self, CParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 108
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.LT) | (1 << CParser.GT) | (1 << CParser.LTE) | (1 << CParser.GTE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = CParser.BinaryOpBooleanContext(self, CParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 111
                        _la = self._input.LA(1)
                        if not(_la==CParser.DEQ or _la==CParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = CParser.BinaryOpBooleanContext(self, CParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 114
                        _la = self._input.LA(1)
                        if not(_la==CParser.AND or _la==CParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expr(5)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(CParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(CParser.RCURLY, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatContext)
            else:
                return self.getTypedRuleContext(CParser.StatContext,i)


        def getRuleIndex(self):
            return CParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)




    def scope(self):

        localctx = CParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(CParser.LCURLY)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.MUL) | (1 << CParser.ADD) | (1 << CParser.SUB) | (1 << CParser.NOT) | (1 << CParser.INCR) | (1 << CParser.DECR) | (1 << CParser.LBRACKET) | (1 << CParser.END_INSTR) | (1 << CParser.REF) | (1 << CParser.CONST) | (1 << CParser.SIGNED) | (1 << CParser.UNSIGNED) | (1 << CParser.INT_PREF) | (1 << CParser.VOID_PREF) | (1 << CParser.SHORT_PREF) | (1 << CParser.LONG_PREF) | (1 << CParser.LONG_LONG_PREF) | (1 << CParser.INT) | (1 << CParser.FLOAT_PREF) | (1 << CParser.DOUBLE_PREF) | (1 << CParser.LONG_DOUBLE_PREF) | (1 << CParser.FLOAT) | (1 << CParser.CHAR_PREF) | (1 << CParser.CHAR) | (1 << CParser.STRING) | (1 << CParser.PRINTF) | (1 << CParser.IF) | (1 << CParser.FOR) | (1 << CParser.WHILE) | (1 << CParser.BREAK) | (1 << CParser.CONTINUE) | (1 << CParser.SWITCH) | (1 << CParser.RETURN) | (1 << CParser.ID))) != 0):
                self.state = 122
                self.stat()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(CParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CParser.FOR, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def END_INSTR(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.END_INSTR)
            else:
                return self.getToken(CParser.END_INSTR, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExprContext)
            else:
                return self.getTypedRuleContext(CParser.ExprContext,i)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def definition(self):
            return self.getTypedRuleContext(CParser.DefinitionContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentContext,i)


        def getRuleIndex(self):
            return CParser.RULE_for_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stat" ):
                listener.enterFor_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stat" ):
                listener.exitFor_stat(self)




    def for_stat(self):

        localctx = CParser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_for_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CParser.FOR)
            self.state = 131
            self.match(CParser.LBRACKET)
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.CONST, CParser.SIGNED, CParser.UNSIGNED, CParser.INT_PREF, CParser.VOID_PREF, CParser.SHORT_PREF, CParser.LONG_PREF, CParser.LONG_LONG_PREF, CParser.FLOAT_PREF, CParser.DOUBLE_PREF, CParser.LONG_DOUBLE_PREF, CParser.CHAR_PREF]:
                self.state = 132
                self.definition()
                pass
            elif token in [CParser.ID]:
                self.state = 133
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self.match(CParser.END_INSTR)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(CParser.END_INSTR)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 139
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 140
                self.assignment()
                pass


            self.state = 143
            self.match(CParser.RBRACKET)
            self.state = 144
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CParser.WHILE, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def getRuleIndex(self):
            return CParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)




    def while_stat(self):

        localctx = CParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CParser.WHILE)
            self.state = 147
            self.match(CParser.LBRACKET)
            self.state = 148
            self.expr(0)
            self.state = 149
            self.match(CParser.RBRACKET)
            self.state = 150
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CParser.IF, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def elif_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.Elif_statContext)
            else:
                return self.getTypedRuleContext(CParser.Elif_statContext,i)


        def else_stat(self):
            return self.getTypedRuleContext(CParser.Else_statContext,0)


        def getRuleIndex(self):
            return CParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)




    def if_stat(self):

        localctx = CParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CParser.IF)
            self.state = 153
            self.match(CParser.LBRACKET)
            self.state = 154
            self.expr(0)
            self.state = 155
            self.match(CParser.RBRACKET)
            self.state = 156
            self.scope()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.ELIF:
                self.state = 157
                self.elif_stat()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.ELSE:
                self.state = 163
                self.else_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(CParser.ELIF, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def getRuleIndex(self):
            return CParser.RULE_elif_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_stat" ):
                listener.enterElif_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_stat" ):
                listener.exitElif_stat(self)




    def elif_stat(self):

        localctx = CParser.Elif_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elif_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(CParser.ELIF)
            self.state = 167
            self.match(CParser.LBRACKET)
            self.state = 168
            self.expr(0)
            self.state = 169
            self.match(CParser.RBRACKET)
            self.state = 170
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CParser.ELSE, 0)

        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def getRuleIndex(self):
            return CParser.RULE_else_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stat" ):
                listener.enterElse_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stat" ):
                listener.exitElse_stat(self)




    def else_stat(self):

        localctx = CParser.Else_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(CParser.ELSE)
            self.state = 173
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(CParser.SWITCH, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def LCURLY(self):
            return self.getToken(CParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(CParser.RCURLY, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.CASE)
            else:
                return self.getToken(CParser.CASE, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COLON)
            else:
                return self.getToken(CParser.COLON, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatContext)
            else:
                return self.getTypedRuleContext(CParser.StatContext,i)


        def DEFAULT(self):
            return self.getToken(CParser.DEFAULT, 0)

        def getRuleIndex(self):
            return CParser.RULE_switch_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_stat" ):
                listener.enterSwitch_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_stat" ):
                listener.exitSwitch_stat(self)




    def switch_stat(self):

        localctx = CParser.Switch_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_switch_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(CParser.SWITCH)
            self.state = 176
            self.match(CParser.LBRACKET)
            self.state = 177
            self.expr(0)
            self.state = 178
            self.match(CParser.RBRACKET)
            self.state = 179
            self.match(CParser.LCURLY)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 180
                    self.match(CParser.CASE)
                    self.state = 181
                    self.match(CParser.COLON)
                    self.state = 182
                    self.stat() 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CParser.DEFAULT:
                self.state = 188
                self.match(CParser.DEFAULT)
                self.state = 189
                self.match(CParser.COLON)
                self.state = 190
                self.stat()


            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.CASE:
                self.state = 193
                self.match(CParser.CASE)
                self.state = 194
                self.match(CParser.COLON)
                self.state = 195
                self.stat()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(CParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_PREF(self):
            return self.getToken(CParser.SHORT_PREF, 0)

        def INT_PREF(self):
            return self.getToken(CParser.INT_PREF, 0)

        def LONG_PREF(self):
            return self.getToken(CParser.LONG_PREF, 0)

        def LONG_LONG_PREF(self):
            return self.getToken(CParser.LONG_LONG_PREF, 0)

        def CHAR_PREF(self):
            return self.getToken(CParser.CHAR_PREF, 0)

        def CONST(self):
            return self.getToken(CParser.CONST, 0)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.MUL)
            else:
                return self.getToken(CParser.MUL, i)

        def SIGNED(self):
            return self.getToken(CParser.SIGNED, 0)

        def UNSIGNED(self):
            return self.getToken(CParser.UNSIGNED, 0)

        def FLOAT_PREF(self):
            return self.getToken(CParser.FLOAT_PREF, 0)

        def DOUBLE_PREF(self):
            return self.getToken(CParser.DOUBLE_PREF, 0)

        def LONG_DOUBLE_PREF(self):
            return self.getToken(CParser.LONG_DOUBLE_PREF, 0)

        def VOID_PREF(self):
            return self.getToken(CParser.VOID_PREF, 0)

        def getRuleIndex(self):
            return CParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)




    def type_specifier(self):

        localctx = CParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.CONST:
                    self.state = 203
                    self.match(CParser.CONST)


                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.SIGNED or _la==CParser.UNSIGNED:
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==CParser.SIGNED or _la==CParser.UNSIGNED):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 209
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.INT_PREF) | (1 << CParser.SHORT_PREF) | (1 << CParser.LONG_PREF) | (1 << CParser.LONG_LONG_PREF) | (1 << CParser.CHAR_PREF))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CParser.MUL:
                    self.state = 210
                    self.match(CParser.MUL)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CParser.CONST:
                    self.state = 216
                    self.match(CParser.CONST)


                self.state = 219
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.FLOAT_PREF) | (1 << CParser.DOUBLE_PREF) | (1 << CParser.LONG_DOUBLE_PREF))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CParser.MUL:
                    self.state = 220
                    self.match(CParser.MUL)
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.match(CParser.VOID_PREF)
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
            return CParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)


    class FloatContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class CharacterContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter" ):
                listener.enterCharacter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter" ):
                listener.exitCharacter(self)


    class StringContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)



    def literal(self):

        localctx = CParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.FLOAT]:
                localctx = CParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(CParser.FLOAT)
                pass
            elif token in [CParser.INT]:
                localctx = CParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(CParser.INT)
                pass
            elif token in [CParser.STRING]:
                localctx = CParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.match(CParser.STRING)
                pass
            elif token in [CParser.CHAR]:
                localctx = CParser.CharacterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.match(CParser.CHAR)
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
            return self.getTypedRuleContext(CParser.Type_specifierContext,0)


        def ID(self):
            return self.getToken(CParser.ID, 0)

        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.type_specifier()
            self.state = 236
            self.match(CParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_function_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionDeclarationContext(Function_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CParser.Function_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_specifier(self):
            return self.getTypedRuleContext(CParser.Type_specifierContext,0)

        def ID(self):
            return self.getToken(CParser.ID, 0)
        def arg_list(self):
            return self.getTypedRuleContext(CParser.Arg_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)



    def function_declaration(self):

        localctx = CParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_declaration)
        try:
            localctx = CParser.FunctionDeclarationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.type_specifier()
            self.state = 239
            self.match(CParser.ID)
            self.state = 240
            self.arg_list()
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
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def EQ(self):
            return self.getToken(CParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def getRuleIndex(self):
            return CParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = CParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.declaration()
            self.state = 243
            self.match(CParser.EQ)
            self.state = 244
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(CParser.Function_declarationContext,0)


        def scope(self):
            return self.getTypedRuleContext(CParser.ScopeContext,0)


        def getRuleIndex(self):
            return CParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)




    def function_definition(self):

        localctx = CParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.function_declaration()
            self.state = 247
            self.scope()
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
            return self.getToken(CParser.ID, 0)

        def EQ(self):
            return self.getToken(CParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def getRuleIndex(self):
            return CParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(CParser.ID)
            self.state = 250
            self.match(CParser.EQ)
            self.state = 251
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CParser.ID, 0)

        def call_list(self):
            return self.getTypedRuleContext(CParser.Call_listContext,0)


        def PRINTF(self):
            return self.getToken(CParser.PRINTF, 0)

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def getRuleIndex(self):
            return CParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = CParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_call)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(CParser.ID)
                self.state = 254
                self.call_list()
                pass
            elif token in [CParser.PRINTF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(CParser.PRINTF)
                self.state = 256
                self.match(CParser.LBRACKET)
                self.state = 257
                self.expr(0)
                self.state = 258
                self.match(CParser.RBRACKET)
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


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = CParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(CParser.LBRACKET)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.CONST) | (1 << CParser.SIGNED) | (1 << CParser.UNSIGNED) | (1 << CParser.INT_PREF) | (1 << CParser.VOID_PREF) | (1 << CParser.SHORT_PREF) | (1 << CParser.LONG_PREF) | (1 << CParser.LONG_LONG_PREF) | (1 << CParser.FLOAT_PREF) | (1 << CParser.DOUBLE_PREF) | (1 << CParser.LONG_DOUBLE_PREF) | (1 << CParser.CHAR_PREF))) != 0):
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 263
                        self.declaration()
                        self.state = 264
                        self.match(CParser.COMMA) 
                    self.state = 270
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 271
                self.declaration()


            self.state = 274
            self.match(CParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(CParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(CParser.RBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExprContext)
            else:
                return self.getTypedRuleContext(CParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.COMMA)
            else:
                return self.getToken(CParser.COMMA, i)

        def getRuleIndex(self):
            return CParser.RULE_call_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_list" ):
                listener.enterCall_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_list" ):
                listener.exitCall_list(self)




    def call_list(self):

        localctx = CParser.Call_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(CParser.LBRACKET)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.MUL) | (1 << CParser.ADD) | (1 << CParser.SUB) | (1 << CParser.NOT) | (1 << CParser.INCR) | (1 << CParser.DECR) | (1 << CParser.LBRACKET) | (1 << CParser.REF) | (1 << CParser.INT) | (1 << CParser.FLOAT) | (1 << CParser.CHAR) | (1 << CParser.STRING) | (1 << CParser.PRINTF) | (1 << CParser.ID))) != 0):
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 277
                        self.expr(0)
                        self.state = 278
                        self.match(CParser.COMMA) 
                    self.state = 284
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 285
                self.expr(0)


            self.state = 288
            self.match(CParser.RBRACKET)
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




