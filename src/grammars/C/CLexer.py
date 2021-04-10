# Generated from ./src/grammars/C/C.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5")
        buf.write("#\u00eb\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u00f9")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\5%\u0111\n%\3&\3&\7&\u0115\n&\f&\16&")
        buf.write("\u0118\13&\3&\5&\u011b\n&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\5*\u0137\n*\3*\3*\6*\u013b\n*\r*\16*\u013c\3+\3+\3+")
        buf.write("\3+\3+\3,\3,\5,\u0146\n,\3,\3,\3,\3-\3-\7-\u014d\n-\f")
        buf.write("-\16-\u0150\13-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\7;\u01b4\n;\f;\16;\u01b7")
        buf.write("\13;\3<\6<\u01ba\n<\r<\16<\u01bb\3<\3<\3=\3=\3=\3=\7=")
        buf.write("\u01c4\n=\f=\16=\u01c7\13=\3=\3=\3=\3=\3>\3>\3>\3>\7>")
        buf.write("\u01d1\n>\f>\16>\u01d4\13>\3>\3>\3>\3>\3>\4\u01c5\u01d2")
        buf.write("\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?\3\2\b\3\2\63;\3\2\62;\3\2#\u0080\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01e6\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\3}\3\2\2\2\5\177\3\2\2\2\7\u0081\3\2\2\2\t\u0083\3\2")
        buf.write("\2\2\13\u0085\3\2\2\2\r\u0087\3\2\2\2\17\u0089\3\2\2\2")
        buf.write("\21\u008c\3\2\2\2\23\u008e\3\2\2\2\25\u0090\3\2\2\2\27")
        buf.write("\u0093\3\2\2\2\31\u0096\3\2\2\2\33\u0099\3\2\2\2\35\u009c")
        buf.write("\3\2\2\2\37\u009f\3\2\2\2!\u00a1\3\2\2\2#\u00a4\3\2\2")
        buf.write("\2%\u00a7\3\2\2\2\'\u00a9\3\2\2\2)\u00ab\3\2\2\2+\u00ad")
        buf.write("\3\2\2\2-\u00af\3\2\2\2/\u00b1\3\2\2\2\61\u00b3\3\2\2")
        buf.write("\2\63\u00b5\3\2\2\2\65\u00b7\3\2\2\2\67\u00b9\3\2\2\2")
        buf.write("9\u00bb\3\2\2\2;\u00bd\3\2\2\2=\u00c3\3\2\2\2?\u00ca\3")
        buf.write("\2\2\2A\u00d3\3\2\2\2C\u00d7\3\2\2\2E\u00ea\3\2\2\2G\u00f8")
        buf.write("\3\2\2\2I\u0110\3\2\2\2K\u011a\3\2\2\2M\u011c\3\2\2\2")
        buf.write("O\u0122\3\2\2\2Q\u0129\3\2\2\2S\u0136\3\2\2\2U\u013e\3")
        buf.write("\2\2\2W\u0143\3\2\2\2Y\u014a\3\2\2\2[\u0153\3\2\2\2]\u015a")
        buf.write("\3\2\2\2_\u015d\3\2\2\2a\u0165\3\2\2\2c\u016a\3\2\2\2")
        buf.write("e\u016e\3\2\2\2g\u0174\3\2\2\2i\u017a\3\2\2\2k\u0183\3")
        buf.write("\2\2\2m\u018a\3\2\2\2o\u018f\3\2\2\2q\u0197\3\2\2\2s\u019e")
        buf.write("\3\2\2\2u\u01b1\3\2\2\2w\u01b9\3\2\2\2y\u01bf\3\2\2\2")
        buf.write("{\u01cc\3\2\2\2}~\7,\2\2~\4\3\2\2\2\177\u0080\7\61\2\2")
        buf.write("\u0080\6\3\2\2\2\u0081\u0082\7-\2\2\u0082\b\3\2\2\2\u0083")
        buf.write("\u0084\7/\2\2\u0084\n\3\2\2\2\u0085\u0086\7>\2\2\u0086")
        buf.write("\f\3\2\2\2\u0087\u0088\7@\2\2\u0088\16\3\2\2\2\u0089\u008a")
        buf.write("\7?\2\2\u008a\u008b\7?\2\2\u008b\20\3\2\2\2\u008c\u008d")
        buf.write("\7?\2\2\u008d\22\3\2\2\2\u008e\u008f\7\'\2\2\u008f\24")
        buf.write("\3\2\2\2\u0090\u0091\7>\2\2\u0091\u0092\7?\2\2\u0092\26")
        buf.write("\3\2\2\2\u0093\u0094\7@\2\2\u0094\u0095\7?\2\2\u0095\30")
        buf.write("\3\2\2\2\u0096\u0097\7#\2\2\u0097\u0098\7?\2\2\u0098\32")
        buf.write("\3\2\2\2\u0099\u009a\7(\2\2\u009a\u009b\7(\2\2\u009b\34")
        buf.write("\3\2\2\2\u009c\u009d\7~\2\2\u009d\u009e\7~\2\2\u009e\36")
        buf.write("\3\2\2\2\u009f\u00a0\7#\2\2\u00a0 \3\2\2\2\u00a1\u00a2")
        buf.write("\7-\2\2\u00a2\u00a3\7-\2\2\u00a3\"\3\2\2\2\u00a4\u00a5")
        buf.write("\7/\2\2\u00a5\u00a6\7/\2\2\u00a6$\3\2\2\2\u00a7\u00a8")
        buf.write("\7*\2\2\u00a8&\3\2\2\2\u00a9\u00aa\7+\2\2\u00aa(\3\2\2")
        buf.write("\2\u00ab\u00ac\7}\2\2\u00ac*\3\2\2\2\u00ad\u00ae\7\177")
        buf.write("\2\2\u00ae,\3\2\2\2\u00af\u00b0\7=\2\2\u00b0.\3\2\2\2")
        buf.write("\u00b1\u00b2\7<\2\2\u00b2\60\3\2\2\2\u00b3\u00b4\7\60")
        buf.write("\2\2\u00b4\62\3\2\2\2\u00b5\u00b6\7(\2\2\u00b6\64\3\2")
        buf.write("\2\2\u00b7\u00b8\7)\2\2\u00b8\66\3\2\2\2\u00b9\u00ba\7")
        buf.write("^\2\2\u00ba8\3\2\2\2\u00bb\u00bc\7.\2\2\u00bc:\3\2\2\2")
        buf.write("\u00bd\u00be\7e\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7p")
        buf.write("\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7v\2\2\u00c2<\3\2")
        buf.write("\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6")
        buf.write("\7i\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9")
        buf.write("\7f\2\2\u00c9>\3\2\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7i\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2@\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6B\3\2\2\2\u00d7\u00d8")
        buf.write("\7x\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7f\2\2\u00dbD\3\2\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de")
        buf.write("\7j\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7t\2\2\u00e0\u00eb")
        buf.write("\7v\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3\7j\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7\"\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00eb")
        buf.write("\7v\2\2\u00ea\u00dc\3\2\2\2\u00ea\u00e1\3\2\2\2\u00eb")
        buf.write("F\3\2\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7q\2\2\u00ee")
        buf.write("\u00ef\7p\2\2\u00ef\u00f9\7i\2\2\u00f0\u00f1\7n\2\2\u00f1")
        buf.write("\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7i\2\2\u00f4")
        buf.write("\u00f5\7\"\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f9\7v\2\2\u00f8\u00ec\3\2\2\2\u00f8\u00f0\3\2\2\2")
        buf.write("\u00f9H\3\2\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7q\2\2")
        buf.write("\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7\"")
        buf.write("\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0111\7i\2\2\u0103\u0104\7n\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7p\2\2\u0106\u0107\7i\2\2\u0107\u0108")
        buf.write("\7\"\2\2\u0108\u0109\7n\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7i\2\2\u010c\u010d\7\"\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7p\2\2\u010f\u0111\7v\2\2\u0110\u00fa")
        buf.write("\3\2\2\2\u0110\u0103\3\2\2\2\u0111J\3\2\2\2\u0112\u0116")
        buf.write("\t\2\2\2\u0113\u0115\t\3\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u011b\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\7")
        buf.write("\62\2\2\u011a\u0112\3\2\2\2\u011a\u0119\3\2\2\2\u011b")
        buf.write("L\3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7n\2\2\u011e")
        buf.write("\u011f\7q\2\2\u011f\u0120\7c\2\2\u0120\u0121\7v\2\2\u0121")
        buf.write("N\3\2\2\2\u0122\u0123\7f\2\2\u0123\u0124\7q\2\2\u0124")
        buf.write("\u0125\7w\2\2\u0125\u0126\7d\2\2\u0126\u0127\7n\2\2\u0127")
        buf.write("\u0128\7g\2\2\u0128P\3\2\2\2\u0129\u012a\7n\2\2\u012a")
        buf.write("\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c\u012d\7i\2\2\u012d")
        buf.write("\u012e\7\"\2\2\u012e\u012f\7f\2\2\u012f\u0130\7q\2\2\u0130")
        buf.write("\u0131\7w\2\2\u0131\u0132\7d\2\2\u0132\u0133\7n\2\2\u0133")
        buf.write("\u0134\7g\2\2\u0134R\3\2\2\2\u0135\u0137\5K&\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\5\61\31\2\u0139\u013b\t\3\2\2\u013a\u0139\3\2\2")
        buf.write("\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013dT\3\2\2\2\u013e\u013f\7e\2\2\u013f\u0140")
        buf.write("\7j\2\2\u0140\u0141\7c\2\2\u0141\u0142\7t\2\2\u0142V\3")
        buf.write("\2\2\2\u0143\u0145\5\65\33\2\u0144\u0146\5\67\34\2\u0145")
        buf.write("\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0148\t\4\2\2\u0148\u0149\5\65\33\2\u0149X\3\2")
        buf.write("\2\2\u014a\u014e\7$\2\2\u014b\u014d\5W,\2\u014c\u014b")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0151\u0152\7$\2\2\u0152Z\3\2\2\2\u0153\u0154\7r\2\2")
        buf.write("\u0154\u0155\7t\2\2\u0155\u0156\7k\2\2\u0156\u0157\7p")
        buf.write("\2\2\u0157\u0158\7v\2\2\u0158\u0159\7h\2\2\u0159\\\3\2")
        buf.write("\2\2\u015a\u015b\7k\2\2\u015b\u015c\7h\2\2\u015c^\3\2")
        buf.write("\2\2\u015d\u015e\7g\2\2\u015e\u015f\7n\2\2\u015f\u0160")
        buf.write("\7u\2\2\u0160\u0161\7g\2\2\u0161\u0162\7\"\2\2\u0162\u0163")
        buf.write("\7k\2\2\u0163\u0164\7h\2\2\u0164`\3\2\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166\u0167\7n\2\2\u0167\u0168\7u\2\2\u0168\u0169")
        buf.write("\7g\2\2\u0169b\3\2\2\2\u016a\u016b\7h\2\2\u016b\u016c")
        buf.write("\7q\2\2\u016c\u016d\7t\2\2\u016dd\3\2\2\2\u016e\u016f")
        buf.write("\7y\2\2\u016f\u0170\7j\2\2\u0170\u0171\7k\2\2\u0171\u0172")
        buf.write("\7n\2\2\u0172\u0173\7g\2\2\u0173f\3\2\2\2\u0174\u0175")
        buf.write("\7d\2\2\u0175\u0176\7t\2\2\u0176\u0177\7g\2\2\u0177\u0178")
        buf.write("\7c\2\2\u0178\u0179\7m\2\2\u0179h\3\2\2\2\u017a\u017b")
        buf.write("\7e\2\2\u017b\u017c\7q\2\2\u017c\u017d\7p\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017e\u017f\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181")
        buf.write("\7w\2\2\u0181\u0182\7g\2\2\u0182j\3\2\2\2\u0183\u0184")
        buf.write("\7u\2\2\u0184\u0185\7y\2\2\u0185\u0186\7k\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7e\2\2\u0188\u0189\7j\2\2\u0189l\3")
        buf.write("\2\2\2\u018a\u018b\7e\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7u\2\2\u018d\u018e\7g\2\2\u018en\3\2\2\2\u018f\u0190")
        buf.write("\7f\2\2\u0190\u0191\7g\2\2\u0191\u0192\7h\2\2\u0192\u0193")
        buf.write("\7c\2\2\u0193\u0194\7w\2\2\u0194\u0195\7n\2\2\u0195\u0196")
        buf.write("\7v\2\2\u0196p\3\2\2\2\u0197\u0198\7t\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199\u019a\7v\2\2\u019a\u019b\7w\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c\u019d\7p\2\2\u019dr\3\2\2\2\u019e\u019f")
        buf.write("\7%\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1\7p\2\2\u01a1\u01a2")
        buf.write("\7e\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4\7w\2\2\u01a4\u01a5")
        buf.write("\7f\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7\"\2\2\u01a7\u01a8")
        buf.write("\7>\2\2\u01a8\u01a9\7u\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab")
        buf.write("\7f\2\2\u01ab\u01ac\7k\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae")
        buf.write("\7\60\2\2\u01ae\u01af\7j\2\2\u01af\u01b0\7@\2\2\u01b0")
        buf.write("t\3\2\2\2\u01b1\u01b5\t\5\2\2\u01b2\u01b4\t\6\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6v\3\2\2\2\u01b7\u01b5\3\2\2")
        buf.write("\2\u01b8\u01ba\t\7\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\b<\2\2\u01bex\3\2\2\2\u01bf")
        buf.write("\u01c0\7\61\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c5\3\2\2")
        buf.write("\2\u01c2\u01c4\13\2\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6")
        buf.write("\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7\f\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cb\b=\2\2\u01cbz\3\2\2\2")
        buf.write("\u01cc\u01cd\7\61\2\2\u01cd\u01ce\7,\2\2\u01ce\u01d2\3")
        buf.write("\2\2\2\u01cf\u01d1\13\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d4\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d6\7")
        buf.write(",\2\2\u01d6\u01d7\7\61\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9")
        buf.write("\b>\2\2\u01d9|\3\2\2\2\20\2\u00ea\u00f8\u0110\u0116\u011a")
        buf.write("\u0136\u013c\u0145\u014e\u01b5\u01bb\u01c5\u01d2\3\b\2")
        buf.write("\2")
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
    LCURLY = 20
    RCURLY = 21
    END_INSTR = 22
    COLON = 23
    DOT = 24
    REF = 25
    SQUOTE = 26
    ESC = 27
    COMMA = 28
    CONST = 29
    SIGNED = 30
    UNSIGNED = 31
    INT_PREF = 32
    VOID_PREF = 33
    SHORT_PREF = 34
    LONG_PREF = 35
    LONG_LONG_PREF = 36
    INT = 37
    FLOAT_PREF = 38
    DOUBLE_PREF = 39
    LONG_DOUBLE_PREF = 40
    FLOAT = 41
    CHAR_PREF = 42
    CHAR = 43
    STRING = 44
    PRINTF = 45
    IF = 46
    ELIF = 47
    ELSE = 48
    FOR = 49
    WHILE = 50
    BREAK = 51
    CONTINUE = 52
    SWITCH = 53
    CASE = 54
    DEFAULT = 55
    RETURN = 56
    INCLUDE_IO = 57
    ID = 58
    WS = 59
    SINGLE_COMMENT = 60
    MULTI_COMMENT = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", "'='", "'%'", 
            "'<='", "'>='", "'!='", "'&&'", "'||'", "'!'", "'++'", "'--'", 
            "'('", "')'", "'{'", "'}'", "';'", "':'", "'.'", "'&'", "'''", 
            "'\\'", "','", "'const'", "'signed'", "'unsigned'", "'int'", 
            "'void'", "'float'", "'double'", "'long double'", "'char'", 
            "'printf'", "'if'", "'else if'", "'else'", "'for'", "'while'", 
            "'break'", "'continue'", "'switch'", "'case'", "'default'", 
            "'return'", "'#include <stdio.h>'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "LT", "GT", "DEQ", "EQ", "MOD", 
            "LTE", "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", "LBRACKET", 
            "RBRACKET", "LCURLY", "RCURLY", "END_INSTR", "COLON", "DOT", 
            "REF", "SQUOTE", "ESC", "COMMA", "CONST", "SIGNED", "UNSIGNED", 
            "INT_PREF", "VOID_PREF", "SHORT_PREF", "LONG_PREF", "LONG_LONG_PREF", 
            "INT", "FLOAT_PREF", "DOUBLE_PREF", "LONG_DOUBLE_PREF", "FLOAT", 
            "CHAR_PREF", "CHAR", "STRING", "PRINTF", "IF", "ELIF", "ELSE", 
            "FOR", "WHILE", "BREAK", "CONTINUE", "SWITCH", "CASE", "DEFAULT", 
            "RETURN", "INCLUDE_IO", "ID", "WS", "SINGLE_COMMENT", "MULTI_COMMENT" ]

    ruleNames = [ "MUL", "DIV", "ADD", "SUB", "LT", "GT", "DEQ", "EQ", "MOD", 
                  "LTE", "GTE", "NEQ", "AND", "OR", "NOT", "INCR", "DECR", 
                  "LBRACKET", "RBRACKET", "LCURLY", "RCURLY", "END_INSTR", 
                  "COLON", "DOT", "REF", "SQUOTE", "ESC", "COMMA", "CONST", 
                  "SIGNED", "UNSIGNED", "INT_PREF", "VOID_PREF", "SHORT_PREF", 
                  "LONG_PREF", "LONG_LONG_PREF", "INT", "FLOAT_PREF", "DOUBLE_PREF", 
                  "LONG_DOUBLE_PREF", "FLOAT", "CHAR_PREF", "CHAR", "STRING", 
                  "PRINTF", "IF", "ELIF", "ELSE", "FOR", "WHILE", "BREAK", 
                  "CONTINUE", "SWITCH", "CASE", "DEFAULT", "RETURN", "INCLUDE_IO", 
                  "ID", "WS", "SINGLE_COMMENT", "MULTI_COMMENT" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


