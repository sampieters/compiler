# Generated from src/grammars/C/C.g4 by ANTLR 4.9.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u">\u01d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write(u"\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write(u"\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write(u"\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3")
        buf.write(u"\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write(u"\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3")
        buf.write(u"\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write(u"!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\5\"\u00e4\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\5#\u00f2\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u010a\n$\3%\3%\7")
        buf.write(u"%\u010e\n%\f%\16%\u0111\13%\3%\5%\u0114\n%\3&\3&\3&\3")
        buf.write(u"&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3)\5)\u0130\n)\3)\3)\6)\u0134\n)")
        buf.write(u"\r)\16)\u0135\3*\3*\3*\3*\3*\3+\3+\5+\u013f\n+\3+\3+")
        buf.write(u"\3+\3,\3,\7,\u0146\n,\f,\16,\u0149\13,\3,\3,\3-\3-\3")
        buf.write(u"-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\3")
        buf.write(u"8\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39")
        buf.write(u"\39\39\3:\3:\7:\u01ad\n:\f:\16:\u01b0\13:\3;\6;\u01b3")
        buf.write(u"\n;\r;\16;\u01b4\3;\3;\3<\3<\3<\3<\7<\u01bd\n<\f<\16")
        buf.write(u"<\u01c0\13<\3<\3<\3<\3<\3=\3=\3=\3=\7=\u01ca\n=\f=\16")
        buf.write(u"=\u01cd\13=\3=\3=\3=\3=\3=\4\u01be\u01cb\2>\3\3\5\4\7")
        buf.write(u"\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write(u"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write(u"\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W")
        buf.write(u"-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>\3")
        buf.write(u"\2\b\3\2\63;\3\2\62;\3\2#\u0080\5\2C\\aac|\6\2\62;C\\")
        buf.write(u"aac|\5\2\13\f\17\17\"\"\2\u01df\2\3\3\2\2\2\2\5\3\2\2")
        buf.write(u"\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write(u"\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write(u"\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write(u"\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write(u"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write(u"\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3")
        buf.write(u"\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write(u"C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write(u"\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write(u"\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write(u"\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write(u"\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write(u"s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{\3\2\2\2")
        buf.write(u"\5}\3\2\2\2\7\177\3\2\2\2\t\u0081\3\2\2\2\13\u0083\3")
        buf.write(u"\2\2\2\r\u0085\3\2\2\2\17\u0087\3\2\2\2\21\u008a\3\2")
        buf.write(u"\2\2\23\u008c\3\2\2\2\25\u008e\3\2\2\2\27\u0091\3\2\2")
        buf.write(u"\2\31\u0094\3\2\2\2\33\u0097\3\2\2\2\35\u009a\3\2\2\2")
        buf.write(u"\37\u009d\3\2\2\2!\u009f\3\2\2\2#\u00a2\3\2\2\2%\u00a5")
        buf.write(u"\3\2\2\2\'\u00a7\3\2\2\2)\u00a9\3\2\2\2+\u00ab\3\2\2")
        buf.write(u"\2-\u00ad\3\2\2\2/\u00af\3\2\2\2\61\u00b1\3\2\2\2\63")
        buf.write(u"\u00b3\3\2\2\2\65\u00b5\3\2\2\2\67\u00b7\3\2\2\29\u00b9")
        buf.write(u"\3\2\2\2;\u00bb\3\2\2\2=\u00c1\3\2\2\2?\u00c8\3\2\2\2")
        buf.write(u"A\u00d1\3\2\2\2C\u00e3\3\2\2\2E\u00f1\3\2\2\2G\u0109")
        buf.write(u"\3\2\2\2I\u0113\3\2\2\2K\u0115\3\2\2\2M\u011b\3\2\2\2")
        buf.write(u"O\u0122\3\2\2\2Q\u012f\3\2\2\2S\u0137\3\2\2\2U\u013c")
        buf.write(u"\3\2\2\2W\u0143\3\2\2\2Y\u014c\3\2\2\2[\u0153\3\2\2\2")
        buf.write(u"]\u0156\3\2\2\2_\u015e\3\2\2\2a\u0163\3\2\2\2c\u0167")
        buf.write(u"\3\2\2\2e\u016d\3\2\2\2g\u0173\3\2\2\2i\u017c\3\2\2\2")
        buf.write(u"k\u0183\3\2\2\2m\u0188\3\2\2\2o\u0190\3\2\2\2q\u0197")
        buf.write(u"\3\2\2\2s\u01aa\3\2\2\2u\u01b2\3\2\2\2w\u01b8\3\2\2\2")
        buf.write(u"y\u01c5\3\2\2\2{|\7,\2\2|\4\3\2\2\2}~\7\61\2\2~\6\3\2")
        buf.write(u"\2\2\177\u0080\7-\2\2\u0080\b\3\2\2\2\u0081\u0082\7/")
        buf.write(u"\2\2\u0082\n\3\2\2\2\u0083\u0084\7>\2\2\u0084\f\3\2\2")
        buf.write(u"\2\u0085\u0086\7@\2\2\u0086\16\3\2\2\2\u0087\u0088\7")
        buf.write(u"?\2\2\u0088\u0089\7?\2\2\u0089\20\3\2\2\2\u008a\u008b")
        buf.write(u"\7?\2\2\u008b\22\3\2\2\2\u008c\u008d\7\'\2\2\u008d\24")
        buf.write(u"\3\2\2\2\u008e\u008f\7>\2\2\u008f\u0090\7?\2\2\u0090")
        buf.write(u"\26\3\2\2\2\u0091\u0092\7@\2\2\u0092\u0093\7?\2\2\u0093")
        buf.write(u"\30\3\2\2\2\u0094\u0095\7#\2\2\u0095\u0096\7?\2\2\u0096")
        buf.write(u"\32\3\2\2\2\u0097\u0098\7(\2\2\u0098\u0099\7(\2\2\u0099")
        buf.write(u"\34\3\2\2\2\u009a\u009b\7~\2\2\u009b\u009c\7~\2\2\u009c")
        buf.write(u"\36\3\2\2\2\u009d\u009e\7#\2\2\u009e \3\2\2\2\u009f\u00a0")
        buf.write(u"\7-\2\2\u00a0\u00a1\7-\2\2\u00a1\"\3\2\2\2\u00a2\u00a3")
        buf.write(u"\7/\2\2\u00a3\u00a4\7/\2\2\u00a4$\3\2\2\2\u00a5\u00a6")
        buf.write(u"\7*\2\2\u00a6&\3\2\2\2\u00a7\u00a8\7+\2\2\u00a8(\3\2")
        buf.write(u"\2\2\u00a9\u00aa\7}\2\2\u00aa*\3\2\2\2\u00ab\u00ac\7")
        buf.write(u"\177\2\2\u00ac,\3\2\2\2\u00ad\u00ae\7=\2\2\u00ae.\3\2")
        buf.write(u"\2\2\u00af\u00b0\7<\2\2\u00b0\60\3\2\2\2\u00b1\u00b2")
        buf.write(u"\7\60\2\2\u00b2\62\3\2\2\2\u00b3\u00b4\7(\2\2\u00b4\64")
        buf.write(u"\3\2\2\2\u00b5\u00b6\7)\2\2\u00b6\66\3\2\2\2\u00b7\u00b8")
        buf.write(u"\7^\2\2\u00b88\3\2\2\2\u00b9\u00ba\7.\2\2\u00ba:\3\2")
        buf.write(u"\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write(u"\7p\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7v\2\2\u00c0<")
        buf.write(u"\3\2\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write(u"\u00c4\7i\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write(u"\u00c7\7f\2\2\u00c7>\3\2\2\2\u00c8\u00c9\7w\2\2\u00c9")
        buf.write(u"\u00ca\7p\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7k\2\2\u00cc")
        buf.write(u"\u00cd\7i\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write(u"\u00d0\7f\2\2\u00d0@\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write(u"\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4B\3\2\2\2\u00d5")
        buf.write(u"\u00d6\7u\2\2\u00d6\u00d7\7j\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write(u"\u00d9\7t\2\2\u00d9\u00e4\7v\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write(u"\u00dc\7j\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7t\2\2\u00de")
        buf.write(u"\u00df\7v\2\2\u00df\u00e0\7\"\2\2\u00e0\u00e1\7k\2\2")
        buf.write(u"\u00e1\u00e2\7p\2\2\u00e2\u00e4\7v\2\2\u00e3\u00d5\3")
        buf.write(u"\2\2\2\u00e3\u00da\3\2\2\2\u00e4D\3\2\2\2\u00e5\u00e6")
        buf.write(u"\7n\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8\u00f2")
        buf.write(u"\7i\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write(u"\7p\2\2\u00ec\u00ed\7i\2\2\u00ed\u00ee\7\"\2\2\u00ee")
        buf.write(u"\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f2\7v\2\2\u00f1")
        buf.write(u"\u00e5\3\2\2\2\u00f1\u00e9\3\2\2\2\u00f2F\3\2\2\2\u00f3")
        buf.write(u"\u00f4\7n\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write(u"\u00f7\7i\2\2\u00f7\u00f8\7\"\2\2\u00f8\u00f9\7n\2\2")
        buf.write(u"\u00f9\u00fa\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\u010a\7")
        buf.write(u"i\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write(u"\7p\2\2\u00ff\u0100\7i\2\2\u0100\u0101\7\"\2\2\u0101")
        buf.write(u"\u0102\7n\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104")
        buf.write(u"\u0105\7i\2\2\u0105\u0106\7\"\2\2\u0106\u0107\7k\2\2")
        buf.write(u"\u0107\u0108\7p\2\2\u0108\u010a\7v\2\2\u0109\u00f3\3")
        buf.write(u"\2\2\2\u0109\u00fc\3\2\2\2\u010aH\3\2\2\2\u010b\u010f")
        buf.write(u"\t\2\2\2\u010c\u010e\t\3\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write(u"\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2")
        buf.write(u"\2\u0110\u0114\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0114")
        buf.write(u"\7\62\2\2\u0113\u010b\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write(u"J\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117\7n\2\2\u0117")
        buf.write(u"\u0118\7q\2\2\u0118\u0119\7c\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write(u"L\3\2\2\2\u011b\u011c\7f\2\2\u011c\u011d\7q\2\2\u011d")
        buf.write(u"\u011e\7w\2\2\u011e\u011f\7d\2\2\u011f\u0120\7n\2\2\u0120")
        buf.write(u"\u0121\7g\2\2\u0121N\3\2\2\2\u0122\u0123\7n\2\2\u0123")
        buf.write(u"\u0124\7q\2\2\u0124\u0125\7p\2\2\u0125\u0126\7i\2\2\u0126")
        buf.write(u"\u0127\7\"\2\2\u0127\u0128\7f\2\2\u0128\u0129\7q\2\2")
        buf.write(u"\u0129\u012a\7w\2\2\u012a\u012b\7d\2\2\u012b\u012c\7")
        buf.write(u"n\2\2\u012c\u012d\7g\2\2\u012dP\3\2\2\2\u012e\u0130\5")
        buf.write(u"I%\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131")
        buf.write(u"\3\2\2\2\u0131\u0133\5\61\31\2\u0132\u0134\t\3\2\2\u0133")
        buf.write(u"\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2")
        buf.write(u"\2\u0135\u0136\3\2\2\2\u0136R\3\2\2\2\u0137\u0138\7e")
        buf.write(u"\2\2\u0138\u0139\7j\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write(u"\7t\2\2\u013bT\3\2\2\2\u013c\u013e\5\65\33\2\u013d\u013f")
        buf.write(u"\5\67\34\2\u013e\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write(u"\u0140\3\2\2\2\u0140\u0141\t\4\2\2\u0141\u0142\5\65\33")
        buf.write(u"\2\u0142V\3\2\2\2\u0143\u0147\7$\2\2\u0144\u0146\5U+")
        buf.write(u"\2\u0145\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145")
        buf.write(u"\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2\u0149")
        buf.write(u"\u0147\3\2\2\2\u014a\u014b\7$\2\2\u014bX\3\2\2\2\u014c")
        buf.write(u"\u014d\7r\2\2\u014d\u014e\7t\2\2\u014e\u014f\7k\2\2\u014f")
        buf.write(u"\u0150\7p\2\2\u0150\u0151\7v\2\2\u0151\u0152\7h\2\2\u0152")
        buf.write(u"Z\3\2\2\2\u0153\u0154\7k\2\2\u0154\u0155\7h\2\2\u0155")
        buf.write(u"\\\3\2\2\2\u0156\u0157\7g\2\2\u0157\u0158\7n\2\2\u0158")
        buf.write(u"\u0159\7u\2\2\u0159\u015a\7g\2\2\u015a\u015b\7\"\2\2")
        buf.write(u"\u015b\u015c\7k\2\2\u015c\u015d\7h\2\2\u015d^\3\2\2\2")
        buf.write(u"\u015e\u015f\7g\2\2\u015f\u0160\7n\2\2\u0160\u0161\7")
        buf.write(u"u\2\2\u0161\u0162\7g\2\2\u0162`\3\2\2\2\u0163\u0164\7")
        buf.write(u"h\2\2\u0164\u0165\7q\2\2\u0165\u0166\7t\2\2\u0166b\3")
        buf.write(u"\2\2\2\u0167\u0168\7y\2\2\u0168\u0169\7j\2\2\u0169\u016a")
        buf.write(u"\7k\2\2\u016a\u016b\7n\2\2\u016b\u016c\7g\2\2\u016cd")
        buf.write(u"\3\2\2\2\u016d\u016e\7d\2\2\u016e\u016f\7t\2\2\u016f")
        buf.write(u"\u0170\7g\2\2\u0170\u0171\7c\2\2\u0171\u0172\7m\2\2\u0172")
        buf.write(u"f\3\2\2\2\u0173\u0174\7e\2\2\u0174\u0175\7q\2\2\u0175")
        buf.write(u"\u0176\7p\2\2\u0176\u0177\7v\2\2\u0177\u0178\7k\2\2\u0178")
        buf.write(u"\u0179\7p\2\2\u0179\u017a\7w\2\2\u017a\u017b\7g\2\2\u017b")
        buf.write(u"h\3\2\2\2\u017c\u017d\7u\2\2\u017d\u017e\7y\2\2\u017e")
        buf.write(u"\u017f\7k\2\2\u017f\u0180\7v\2\2\u0180\u0181\7e\2\2\u0181")
        buf.write(u"\u0182\7j\2\2\u0182j\3\2\2\2\u0183\u0184\7e\2\2\u0184")
        buf.write(u"\u0185\7c\2\2\u0185\u0186\7u\2\2\u0186\u0187\7g\2\2\u0187")
        buf.write(u"l\3\2\2\2\u0188\u0189\7f\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write(u"\u018b\7h\2\2\u018b\u018c\7c\2\2\u018c\u018d\7w\2\2\u018d")
        buf.write(u"\u018e\7n\2\2\u018e\u018f\7v\2\2\u018fn\3\2\2\2\u0190")
        buf.write(u"\u0191\7t\2\2\u0191\u0192\7g\2\2\u0192\u0193\7v\2\2\u0193")
        buf.write(u"\u0194\7w\2\2\u0194\u0195\7t\2\2\u0195\u0196\7p\2\2\u0196")
        buf.write(u"p\3\2\2\2\u0197\u0198\7%\2\2\u0198\u0199\7k\2\2\u0199")
        buf.write(u"\u019a\7p\2\2\u019a\u019b\7e\2\2\u019b\u019c\7n\2\2\u019c")
        buf.write(u"\u019d\7w\2\2\u019d\u019e\7f\2\2\u019e\u019f\7g\2\2\u019f")
        buf.write(u"\u01a0\7\"\2\2\u01a0\u01a1\7>\2\2\u01a1\u01a2\7u\2\2")
        buf.write(u"\u01a2\u01a3\7v\2\2\u01a3\u01a4\7f\2\2\u01a4\u01a5\7")
        buf.write(u"k\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7\7\60\2\2\u01a7\u01a8")
        buf.write(u"\7j\2\2\u01a8\u01a9\7@\2\2\u01a9r\3\2\2\2\u01aa\u01ae")
        buf.write(u"\t\5\2\2\u01ab\u01ad\t\6\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write(u"\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2")
        buf.write(u"\2\u01aft\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\t\7")
        buf.write(u"\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2")
        buf.write(u"\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write(u"\u01b7\b;\2\2\u01b7v\3\2\2\2\u01b8\u01b9\7\61\2\2\u01b9")
        buf.write(u"\u01ba\7\61\2\2\u01ba\u01be\3\2\2\2\u01bb\u01bd\13\2")
        buf.write(u"\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bf")
        buf.write(u"\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0")
        buf.write(u"\u01be\3\2\2\2\u01c1\u01c2\7\f\2\2\u01c2\u01c3\3\2\2")
        buf.write(u"\2\u01c3\u01c4\b<\2\2\u01c4x\3\2\2\2\u01c5\u01c6\7\61")
        buf.write(u"\2\2\u01c6\u01c7\7,\2\2\u01c7\u01cb\3\2\2\2\u01c8\u01ca")
        buf.write(u"\13\2\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb")
        buf.write(u"\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01ce\3\2\2")
        buf.write(u"\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7,\2\2\u01cf\u01d0")
        buf.write(u"\7\61\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\b=\2\2\u01d2")
        buf.write(u"z\3\2\2\2\20\2\u00e3\u00f1\u0109\u010f\u0113\u012f\u0135")
        buf.write(u"\u013e\u0147\u01ae\u01b4\u01be\u01cb\3\b\2\2")
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
    SHORT_PREF = 33
    LONG_PREF = 34
    LONG_LONG_PREF = 35
    INT = 36
    FLOAT_PREF = 37
    DOUBLE_PREF = 38
    LONG_DOUBLE_PREF = 39
    FLOAT = 40
    CHAR_PREF = 41
    CHAR = 42
    STRING = 43
    PRINTF = 44
    IF = 45
    ELIF = 46
    ELSE = 47
    FOR = 48
    WHILE = 49
    BREAK = 50
    CONTINUE = 51
    SWITCH = 52
    CASE = 53
    DEFAULT = 54
    RETURN = 55
    INCLUDE_IO = 56
    ID = 57
    WS = 58
    SINGLE_COMMENT = 59
    MULTI_COMMENT = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'*'", u"'/'", u"'+'", u"'-'", u"'<'", u"'>'", u"'=='", u"'='", 
            u"'%'", u"'<='", u"'>='", u"'!='", u"'&&'", u"'||'", u"'!'", 
            u"'++'", u"'--'", u"'('", u"')'", u"'{'", u"'}'", u"';'", u"':'", 
            u"'.'", u"'&'", u"'''", u"'\\'", u"','", u"'const'", u"'signed'", 
            u"'unsigned'", u"'int'", u"'float'", u"'double'", u"'long double'", 
            u"'char'", u"'printf'", u"'if'", u"'else if'", u"'else'", u"'for'", 
            u"'while'", u"'break'", u"'continue'", u"'switch'", u"'case'", 
            u"'default'", u"'return'", u"'#include <stdio.h>'" ]

    symbolicNames = [ u"<INVALID>",
            u"MUL", u"DIV", u"ADD", u"SUB", u"LT", u"GT", u"DEQ", u"EQ", 
            u"MOD", u"LTE", u"GTE", u"NEQ", u"AND", u"OR", u"NOT", u"INCR", 
            u"DECR", u"LBRACKET", u"RBRACKET", u"LCURLY", u"RCURLY", u"END_INSTR", 
            u"COLON", u"DOT", u"REF", u"SQUOTE", u"ESC", u"COMMA", u"CONST", 
            u"SIGNED", u"UNSIGNED", u"INT_PREF", u"SHORT_PREF", u"LONG_PREF", 
            u"LONG_LONG_PREF", u"INT", u"FLOAT_PREF", u"DOUBLE_PREF", u"LONG_DOUBLE_PREF", 
            u"FLOAT", u"CHAR_PREF", u"CHAR", u"STRING", u"PRINTF", u"IF", 
            u"ELIF", u"ELSE", u"FOR", u"WHILE", u"BREAK", u"CONTINUE", u"SWITCH", 
            u"CASE", u"DEFAULT", u"RETURN", u"INCLUDE_IO", u"ID", u"WS", 
            u"SINGLE_COMMENT", u"MULTI_COMMENT" ]

    ruleNames = [ u"MUL", u"DIV", u"ADD", u"SUB", u"LT", u"GT", u"DEQ", 
                  u"EQ", u"MOD", u"LTE", u"GTE", u"NEQ", u"AND", u"OR", 
                  u"NOT", u"INCR", u"DECR", u"LBRACKET", u"RBRACKET", u"LCURLY", 
                  u"RCURLY", u"END_INSTR", u"COLON", u"DOT", u"REF", u"SQUOTE", 
                  u"ESC", u"COMMA", u"CONST", u"SIGNED", u"UNSIGNED", u"INT_PREF", 
                  u"SHORT_PREF", u"LONG_PREF", u"LONG_LONG_PREF", u"INT", 
                  u"FLOAT_PREF", u"DOUBLE_PREF", u"LONG_DOUBLE_PREF", u"FLOAT", 
                  u"CHAR_PREF", u"CHAR", u"STRING", u"PRINTF", u"IF", u"ELIF", 
                  u"ELSE", u"FOR", u"WHILE", u"BREAK", u"CONTINUE", u"SWITCH", 
                  u"CASE", u"DEFAULT", u"RETURN", u"INCLUDE_IO", u"ID", 
                  u"WS", u"SINGLE_COMMENT", u"MULTI_COMMENT" ]

    grammarFileName = u"C.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(CLexer, self).__init__(input, output=output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


