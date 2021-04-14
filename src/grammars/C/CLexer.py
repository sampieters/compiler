# Generated from src/grammars/C/C.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u00f5\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u0103\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u011b\n\'\3(\3(\7(\u011f\n(\f(\16(\u0122\13(\3(\5")
        buf.write("(\u0125\n(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\5,\u0141\n,\3,\3,\6")
        buf.write(",\u0145\n,\r,\16,\u0146\3-\3-\3-\3-\3-\3.\3.\5.\u0150")
        buf.write("\n.\3.\3.\3.\3/\3/\7/\u0157\n/\f/\16/\u015a\13/\3/\3/")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\38\38\38\38\38\38\39\39\39\39\39\39\39")
        buf.write("\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3>\3>\7>\u01c4\n>\f>\16>\u01c7\13>\3?\6?\u01ca")
        buf.write("\n?\r?\16?\u01cb\3?\3?\3@\3@\3@\3@\7@\u01d4\n@\f@\16@")
        buf.write("\u01d7\13@\3@\3@\3@\3@\3A\3A\3A\3A\7A\u01e1\nA\fA\16A")
        buf.write("\u01e4\13A\3A\3A\3A\3A\3A\5\u0158\u01d5\u01e2\2B\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>")
        buf.write("{?}@\177A\u0081B\3\2\7\3\2\63;\3\2\62;\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01f6\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5")
        buf.write("\u0085\3\2\2\2\7\u0087\3\2\2\2\t\u0089\3\2\2\2\13\u008b")
        buf.write("\3\2\2\2\r\u008d\3\2\2\2\17\u008f\3\2\2\2\21\u0092\3\2")
        buf.write("\2\2\23\u0094\3\2\2\2\25\u0096\3\2\2\2\27\u0099\3\2\2")
        buf.write("\2\31\u009c\3\2\2\2\33\u009f\3\2\2\2\35\u00a2\3\2\2\2")
        buf.write("\37\u00a5\3\2\2\2!\u00a7\3\2\2\2#\u00aa\3\2\2\2%\u00ad")
        buf.write("\3\2\2\2\'\u00af\3\2\2\2)\u00b1\3\2\2\2+\u00b3\3\2\2\2")
        buf.write("-\u00b5\3\2\2\2/\u00b7\3\2\2\2\61\u00b9\3\2\2\2\63\u00bb")
        buf.write("\3\2\2\2\65\u00bd\3\2\2\2\67\u00bf\3\2\2\29\u00c1\3\2")
        buf.write("\2\2;\u00c3\3\2\2\2=\u00c5\3\2\2\2?\u00c7\3\2\2\2A\u00cd")
        buf.write("\3\2\2\2C\u00d4\3\2\2\2E\u00dd\3\2\2\2G\u00e1\3\2\2\2")
        buf.write("I\u00f4\3\2\2\2K\u0102\3\2\2\2M\u011a\3\2\2\2O\u0124\3")
        buf.write("\2\2\2Q\u0126\3\2\2\2S\u012c\3\2\2\2U\u0133\3\2\2\2W\u0140")
        buf.write("\3\2\2\2Y\u0148\3\2\2\2[\u014d\3\2\2\2]\u0154\3\2\2\2")
        buf.write("_\u015d\3\2\2\2a\u0164\3\2\2\2c\u016a\3\2\2\2e\u016d\3")
        buf.write("\2\2\2g\u0175\3\2\2\2i\u017a\3\2\2\2k\u017e\3\2\2\2m\u0184")
        buf.write("\3\2\2\2o\u018a\3\2\2\2q\u0193\3\2\2\2s\u019a\3\2\2\2")
        buf.write("u\u019f\3\2\2\2w\u01a7\3\2\2\2y\u01ae\3\2\2\2{\u01c1\3")
        buf.write("\2\2\2}\u01c9\3\2\2\2\177\u01cf\3\2\2\2\u0081\u01dc\3")
        buf.write("\2\2\2\u0083\u0084\7,\2\2\u0084\4\3\2\2\2\u0085\u0086")
        buf.write("\7\61\2\2\u0086\6\3\2\2\2\u0087\u0088\7-\2\2\u0088\b\3")
        buf.write("\2\2\2\u0089\u008a\7/\2\2\u008a\n\3\2\2\2\u008b\u008c")
        buf.write("\7>\2\2\u008c\f\3\2\2\2\u008d\u008e\7@\2\2\u008e\16\3")
        buf.write("\2\2\2\u008f\u0090\7?\2\2\u0090\u0091\7?\2\2\u0091\20")
        buf.write("\3\2\2\2\u0092\u0093\7?\2\2\u0093\22\3\2\2\2\u0094\u0095")
        buf.write("\7\'\2\2\u0095\24\3\2\2\2\u0096\u0097\7>\2\2\u0097\u0098")
        buf.write("\7?\2\2\u0098\26\3\2\2\2\u0099\u009a\7@\2\2\u009a\u009b")
        buf.write("\7?\2\2\u009b\30\3\2\2\2\u009c\u009d\7#\2\2\u009d\u009e")
        buf.write("\7?\2\2\u009e\32\3\2\2\2\u009f\u00a0\7(\2\2\u00a0\u00a1")
        buf.write("\7(\2\2\u00a1\34\3\2\2\2\u00a2\u00a3\7~\2\2\u00a3\u00a4")
        buf.write("\7~\2\2\u00a4\36\3\2\2\2\u00a5\u00a6\7#\2\2\u00a6 \3\2")
        buf.write("\2\2\u00a7\u00a8\7-\2\2\u00a8\u00a9\7-\2\2\u00a9\"\3\2")
        buf.write("\2\2\u00aa\u00ab\7/\2\2\u00ab\u00ac\7/\2\2\u00ac$\3\2")
        buf.write("\2\2\u00ad\u00ae\7*\2\2\u00ae&\3\2\2\2\u00af\u00b0\7+")
        buf.write("\2\2\u00b0(\3\2\2\2\u00b1\u00b2\7]\2\2\u00b2*\3\2\2\2")
        buf.write("\u00b3\u00b4\7_\2\2\u00b4,\3\2\2\2\u00b5\u00b6\7}\2\2")
        buf.write("\u00b6.\3\2\2\2\u00b7\u00b8\7\177\2\2\u00b8\60\3\2\2\2")
        buf.write("\u00b9\u00ba\7=\2\2\u00ba\62\3\2\2\2\u00bb\u00bc\7<\2")
        buf.write("\2\u00bc\64\3\2\2\2\u00bd\u00be\7\60\2\2\u00be\66\3\2")
        buf.write("\2\2\u00bf\u00c0\7(\2\2\u00c08\3\2\2\2\u00c1\u00c2\7)")
        buf.write("\2\2\u00c2:\3\2\2\2\u00c3\u00c4\7^\2\2\u00c4<\3\2\2\2")
        buf.write("\u00c5\u00c6\7.\2\2\u00c6>\3\2\2\2\u00c7\u00c8\7e\2\2")
        buf.write("\u00c8\u00c9\7q\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7u")
        buf.write("\2\2\u00cb\u00cc\7v\2\2\u00cc@\3\2\2\2\u00cd\u00ce\7u")
        buf.write("\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7i\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7f\2\2\u00d3B\3")
        buf.write("\2\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7")
        buf.write("\7u\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7f\2\2\u00dcD\3")
        buf.write("\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0F\3\2\2\2\u00e1\u00e2\7x\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7f\2\2\u00e5H\3")
        buf.write("\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7j\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\u00f5\7v\2\2\u00eb\u00ec")
        buf.write("\7u\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7\"\2\2\u00f1\u00f2")
        buf.write("\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f5\7v\2\2\u00f4\u00e6")
        buf.write("\3\2\2\2\u00f4\u00eb\3\2\2\2\u00f5J\3\2\2\2\u00f6\u00f7")
        buf.write("\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7p\2\2\u00f9\u0103")
        buf.write("\7i\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7\"\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0103\7v\2\2\u0102\u00f6")
        buf.write("\3\2\2\2\u0102\u00fa\3\2\2\2\u0103L\3\2\2\2\u0104\u0105")
        buf.write("\7n\2\2\u0105\u0106\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7i\2\2\u0108\u0109\7\"\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7q\2\2\u010b\u010c\7p\2\2\u010c\u011b\7i\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7q\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\7i\2\2\u0111\u0112\7\"\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7p\2\2\u0115\u0116\7i\2\2\u0116\u0117")
        buf.write("\7\"\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011b")
        buf.write("\7v\2\2\u011a\u0104\3\2\2\2\u011a\u010d\3\2\2\2\u011b")
        buf.write("N\3\2\2\2\u011c\u0120\t\2\2\2\u011d\u011f\t\3\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u0125\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0123\u0125\7\62\2\2\u0124\u011c\3\2\2\2\u0124")
        buf.write("\u0123\3\2\2\2\u0125P\3\2\2\2\u0126\u0127\7h\2\2\u0127")
        buf.write("\u0128\7n\2\2\u0128\u0129\7q\2\2\u0129\u012a\7c\2\2\u012a")
        buf.write("\u012b\7v\2\2\u012bR\3\2\2\2\u012c\u012d\7f\2\2\u012d")
        buf.write("\u012e\7q\2\2\u012e\u012f\7w\2\2\u012f\u0130\7d\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131\u0132\7g\2\2\u0132T\3\2\2\2\u0133")
        buf.write("\u0134\7n\2\2\u0134\u0135\7q\2\2\u0135\u0136\7p\2\2\u0136")
        buf.write("\u0137\7i\2\2\u0137\u0138\7\"\2\2\u0138\u0139\7f\2\2\u0139")
        buf.write("\u013a\7q\2\2\u013a\u013b\7w\2\2\u013b\u013c\7d\2\2\u013c")
        buf.write("\u013d\7n\2\2\u013d\u013e\7g\2\2\u013eV\3\2\2\2\u013f")
        buf.write("\u0141\5O(\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0144\5\65\33\2\u0143\u0145\t\3\2")
        buf.write("\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147X\3\2\2\2\u0148\u0149")
        buf.write("\7e\2\2\u0149\u014a\7j\2\2\u014a\u014b\7c\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014cZ\3\2\2\2\u014d\u014f\59\35\2\u014e\u0150")
        buf.write("\5;\36\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0152\13\2\2\2\u0152\u0153\59\35")
        buf.write("\2\u0153\\\3\2\2\2\u0154\u0158\7$\2\2\u0155\u0157\13\2")
        buf.write("\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015b\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015c\7$\2\2\u015c^\3\2\2\2\u015d")
        buf.write("\u015e\7r\2\2\u015e\u015f\7t\2\2\u015f\u0160\7k\2\2\u0160")
        buf.write("\u0161\7p\2\2\u0161\u0162\7v\2\2\u0162\u0163\7h\2\2\u0163")
        buf.write("`\3\2\2\2\u0164\u0165\7u\2\2\u0165\u0166\7e\2\2\u0166")
        buf.write("\u0167\7c\2\2\u0167\u0168\7p\2\2\u0168\u0169\7h\2\2\u0169")
        buf.write("b\3\2\2\2\u016a\u016b\7k\2\2\u016b\u016c\7h\2\2\u016c")
        buf.write("d\3\2\2\2\u016d\u016e\7g\2\2\u016e\u016f\7n\2\2\u016f")
        buf.write("\u0170\7u\2\2\u0170\u0171\7g\2\2\u0171\u0172\7\"\2\2\u0172")
        buf.write("\u0173\7k\2\2\u0173\u0174\7h\2\2\u0174f\3\2\2\2\u0175")
        buf.write("\u0176\7g\2\2\u0176\u0177\7n\2\2\u0177\u0178\7u\2\2\u0178")
        buf.write("\u0179\7g\2\2\u0179h\3\2\2\2\u017a\u017b\7h\2\2\u017b")
        buf.write("\u017c\7q\2\2\u017c\u017d\7t\2\2\u017dj\3\2\2\2\u017e")
        buf.write("\u017f\7y\2\2\u017f\u0180\7j\2\2\u0180\u0181\7k\2\2\u0181")
        buf.write("\u0182\7n\2\2\u0182\u0183\7g\2\2\u0183l\3\2\2\2\u0184")
        buf.write("\u0185\7d\2\2\u0185\u0186\7t\2\2\u0186\u0187\7g\2\2\u0187")
        buf.write("\u0188\7c\2\2\u0188\u0189\7m\2\2\u0189n\3\2\2\2\u018a")
        buf.write("\u018b\7e\2\2\u018b\u018c\7q\2\2\u018c\u018d\7p\2\2\u018d")
        buf.write("\u018e\7v\2\2\u018e\u018f\7k\2\2\u018f\u0190\7p\2\2\u0190")
        buf.write("\u0191\7w\2\2\u0191\u0192\7g\2\2\u0192p\3\2\2\2\u0193")
        buf.write("\u0194\7u\2\2\u0194\u0195\7y\2\2\u0195\u0196\7k\2\2\u0196")
        buf.write("\u0197\7v\2\2\u0197\u0198\7e\2\2\u0198\u0199\7j\2\2\u0199")
        buf.write("r\3\2\2\2\u019a\u019b\7e\2\2\u019b\u019c\7c\2\2\u019c")
        buf.write("\u019d\7u\2\2\u019d\u019e\7g\2\2\u019et\3\2\2\2\u019f")
        buf.write("\u01a0\7f\2\2\u01a0\u01a1\7g\2\2\u01a1\u01a2\7h\2\2\u01a2")
        buf.write("\u01a3\7c\2\2\u01a3\u01a4\7w\2\2\u01a4\u01a5\7n\2\2\u01a5")
        buf.write("\u01a6\7v\2\2\u01a6v\3\2\2\2\u01a7\u01a8\7t\2\2\u01a8")
        buf.write("\u01a9\7g\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab\7w\2\2\u01ab")
        buf.write("\u01ac\7t\2\2\u01ac\u01ad\7p\2\2\u01adx\3\2\2\2\u01ae")
        buf.write("\u01af\7%\2\2\u01af\u01b0\7k\2\2\u01b0\u01b1\7p\2\2\u01b1")
        buf.write("\u01b2\7e\2\2\u01b2\u01b3\7n\2\2\u01b3\u01b4\7w\2\2\u01b4")
        buf.write("\u01b5\7f\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7\7\"\2\2\u01b7")
        buf.write("\u01b8\7>\2\2\u01b8\u01b9\7u\2\2\u01b9\u01ba\7v\2\2\u01ba")
        buf.write("\u01bb\7f\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd\7q\2\2\u01bd")
        buf.write("\u01be\7\60\2\2\u01be\u01bf\7j\2\2\u01bf\u01c0\7@\2\2")
        buf.write("\u01c0z\3\2\2\2\u01c1\u01c5\t\4\2\2\u01c2\u01c4\t\5\2")
        buf.write("\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6|\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c8\u01ca\t\6\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\b?\2\2\u01ce~\3\2\2\2")
        buf.write("\u01cf\u01d0\7\61\2\2\u01d0\u01d1\7\61\2\2\u01d1\u01d5")
        buf.write("\3\2\2\2\u01d2\u01d4\13\2\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d7\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7")
        buf.write("\f\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\b@\2\2\u01db\u0080")
        buf.write("\3\2\2\2\u01dc\u01dd\7\61\2\2\u01dd\u01de\7,\2\2\u01de")
        buf.write("\u01e2\3\2\2\2\u01df\u01e1\13\2\2\2\u01e0\u01df\3\2\2")
        buf.write("\2\u01e1\u01e4\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5")
        buf.write("\u01e6\7,\2\2\u01e6\u01e7\7\61\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\bA\2\2\u01e9\u0082\3\2\2\2\20\2\u00f4\u0102")
        buf.write("\u011a\u0120\u0124\u0140\u0146\u014f\u0158\u01c5\u01cb")
        buf.write("\u01d5\u01e2\3\b\2\2")
        return buf.getvalue()


class CLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MUL = 1
    DIV = 2
    ADD = 3
    SUB = 4
    LT = 5
    GT = 6
    DEQ = 7
    EQ = 8
    MOD = 9
    LTE = 10
    GTE = 11
    NEQ = 12
    AND = 13
    OR = 14
    NOT = 15
    INCR = 16
    DECR = 17
    LBRACKET = 18
    RBRACKET = 19
    LSQUARE = 20
    RSQUARE = 21
    LCURLY = 22
    RCURLY = 23
    END_INSTR = 24
    COLON = 25
    DOT = 26
    REF = 27
    SQUOTE = 28
    ESC = 29
    COMMA = 30
    CONST = 31
    SIGNED = 32
    UNSIGNED = 33
    INT_PREF = 34
    VOID_PREF = 35
    SHORT_PREF = 36
    LONG_PREF = 37
    LONG_LONG_PREF = 38
    INT = 39
    FLOAT_PREF = 40
    DOUBLE_PREF = 41
    LONG_DOUBLE_PREF = 42
    FLOAT = 43
    CHAR_PREF = 44
    CHAR = 45
    STRING = 46
    PRINTF = 47
    SCANF = 48
    IF = 49
    ELIF = 50
    ELSE = 51
    FOR = 52
    WHILE = 53
    BREAK = 54
    CONTINUE = 55
    SWITCH = 56
    CASE = 57
    DEFAULT = 58
    RETURN = 59
    INCLUDE_IO = 60
    ID = 61
    WS = 62
    SINGLE_COMMENT = 63
    MULTI_COMMENT = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", "'='", "'%'", 
            "'<='", "'>='", "'!='", "'&&'", "'||'", "'!'", "'++'", "'--'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", 
            "'&'", "'''", "'\\'", "','", "'const'", "'signed'", "'unsigned'", 
            "'int'", "'void'", "'float'", "'double'", "'long double'", "'char'", 
            "'printf'", "'scanf'", "'if'", "'else if'", "'else'", "'for'", 
            "'while'", "'break'", "'continue'", "'switch'", "'case'", "'default'", 
            "'return'", "'#include <stdio.h>'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "LT", "GT", "DEQ", "EQ", "MOD", 
            "LTE", "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", "LBRACKET", 
            "RBRACKET", "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", "END_INSTR", 
            "COLON", "DOT", "REF", "SQUOTE", "ESC", "COMMA", "CONST", "SIGNED", 
            "UNSIGNED", "INT_PREF", "VOID_PREF", "SHORT_PREF", "LONG_PREF", 
            "LONG_LONG_PREF", "INT", "FLOAT_PREF", "DOUBLE_PREF", "LONG_DOUBLE_PREF", 
            "FLOAT", "CHAR_PREF", "CHAR", "STRING", "PRINTF", "SCANF", "IF", 
            "ELIF", "ELSE", "FOR", "WHILE", "BREAK", "CONTINUE", "SWITCH", 
            "CASE", "DEFAULT", "RETURN", "INCLUDE_IO", "ID", "WS", "SINGLE_COMMENT", 
            "MULTI_COMMENT" ]

    ruleNames = [ "MUL", "DIV", "ADD", "SUB", "LT", "GT", "DEQ", "EQ", "MOD", 
                  "LTE", "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", 
                  "LBRACKET", "RBRACKET", "LSQUARE", "RSQUARE", "LCURLY", 
                  "RCURLY", "END_INSTR", "COLON", "DOT", "REF", "SQUOTE", 
                  "ESC", "COMMA", "CONST", "SIGNED", "UNSIGNED", "INT_PREF", 
                  "VOID_PREF", "SHORT_PREF", "LONG_PREF", "LONG_LONG_PREF", 
                  "INT", "FLOAT_PREF", "DOUBLE_PREF", "LONG_DOUBLE_PREF", 
                  "FLOAT", "CHAR_PREF", "CHAR", "STRING", "PRINTF", "SCANF", 
                  "IF", "ELIF", "ELSE", "FOR", "WHILE", "BREAK", "CONTINUE", 
                  "SWITCH", "CASE", "DEFAULT", "RETURN", "INCLUDE_IO", "ID", 
                  "WS", "SINGLE_COMMENT", "MULTI_COMMENT" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


