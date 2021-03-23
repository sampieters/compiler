# Generated from src/grammars/loops/loops.g4 by ANTLR 4.9.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u";\u01b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write(u"\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write(u"\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write(u"\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24")
        buf.write(u"\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3")
        buf.write(u"\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(u"!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u00dc\n!")
        buf.write(u"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write(u"\u00ea\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write(u"\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0102\n#\3$\3$\7$\u0106\n")
        buf.write(u"$\f$\16$\u0109\13$\3$\5$\u010c\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3(\5(\u0128\n(\3(\3(\6(\u012c\n(\r(\16")
        buf.write(u"(\u012d\3)\3)\3)\3)\3)\3*\3*\5*\u0137\n*\3*\3*\3*\3+")
        buf.write(u"\3+\7+\u013e\n+\f+\16+\u0141\13+\3+\3+\3,\3,\3,\3,\3")
        buf.write(u",\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/")
        buf.write(u"\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3")
        buf.write(u"\66\3\66\3\66\3\66\3\67\3\67\7\67\u018b\n\67\f\67\16")
        buf.write(u"\67\u018e\13\67\38\68\u0191\n8\r8\168\u0192\38\38\39")
        buf.write(u"\39\39\39\79\u019b\n9\f9\169\u019e\139\39\39\39\39\3")
        buf.write(u":\3:\3:\3:\7:\u01a8\n:\f:\16:\u01ab\13:\3:\3:\3:\3:\3")
        buf.write(u":\4\u019c\u01a9\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write(u"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write(u"\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write(u"= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write(u"g\65i\66k\67m8o9q:s;\3\2\b\3\2\63;\3\2\62;\3\2#\u0080")
        buf.write(u"\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01bd")
        buf.write(u"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write(u"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write(u"\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write(u"\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write(u"\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3")
        buf.write(u"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2")
        buf.write(u"\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write(u"?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write(u"\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write(u"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write(u"\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write(u"\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write(u"o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5w\3\2\2\2")
        buf.write(u"\7y\3\2\2\2\t{\3\2\2\2\13}\3\2\2\2\r\177\3\2\2\2\17\u0081")
        buf.write(u"\3\2\2\2\21\u0084\3\2\2\2\23\u0086\3\2\2\2\25\u0088\3")
        buf.write(u"\2\2\2\27\u008b\3\2\2\2\31\u008e\3\2\2\2\33\u0091\3\2")
        buf.write(u"\2\2\35\u0094\3\2\2\2\37\u0097\3\2\2\2!\u0099\3\2\2\2")
        buf.write(u"#\u009c\3\2\2\2%\u009f\3\2\2\2\'\u00a1\3\2\2\2)\u00a3")
        buf.write(u"\3\2\2\2+\u00a5\3\2\2\2-\u00a7\3\2\2\2/\u00a9\3\2\2\2")
        buf.write(u"\61\u00ab\3\2\2\2\63\u00ad\3\2\2\2\65\u00af\3\2\2\2\67")
        buf.write(u"\u00b1\3\2\2\29\u00b3\3\2\2\2;\u00b9\3\2\2\2=\u00c0\3")
        buf.write(u"\2\2\2?\u00c9\3\2\2\2A\u00db\3\2\2\2C\u00e9\3\2\2\2E")
        buf.write(u"\u0101\3\2\2\2G\u010b\3\2\2\2I\u010d\3\2\2\2K\u0113\3")
        buf.write(u"\2\2\2M\u011a\3\2\2\2O\u0127\3\2\2\2Q\u012f\3\2\2\2S")
        buf.write(u"\u0134\3\2\2\2U\u013b\3\2\2\2W\u0144\3\2\2\2Y\u014b\3")
        buf.write(u"\2\2\2[\u014e\3\2\2\2]\u0156\3\2\2\2_\u015b\3\2\2\2a")
        buf.write(u"\u015f\3\2\2\2c\u0165\3\2\2\2e\u016b\3\2\2\2g\u0174\3")
        buf.write(u"\2\2\2i\u017b\3\2\2\2k\u0180\3\2\2\2m\u0188\3\2\2\2o")
        buf.write(u"\u0190\3\2\2\2q\u0196\3\2\2\2s\u01a3\3\2\2\2uv\7,\2\2")
        buf.write(u"v\4\3\2\2\2wx\7\61\2\2x\6\3\2\2\2yz\7-\2\2z\b\3\2\2\2")
        buf.write(u"{|\7/\2\2|\n\3\2\2\2}~\7>\2\2~\f\3\2\2\2\177\u0080\7")
        buf.write(u"@\2\2\u0080\16\3\2\2\2\u0081\u0082\7?\2\2\u0082\u0083")
        buf.write(u"\7?\2\2\u0083\20\3\2\2\2\u0084\u0085\7?\2\2\u0085\22")
        buf.write(u"\3\2\2\2\u0086\u0087\7\'\2\2\u0087\24\3\2\2\2\u0088\u0089")
        buf.write(u"\7>\2\2\u0089\u008a\7?\2\2\u008a\26\3\2\2\2\u008b\u008c")
        buf.write(u"\7@\2\2\u008c\u008d\7?\2\2\u008d\30\3\2\2\2\u008e\u008f")
        buf.write(u"\7#\2\2\u008f\u0090\7?\2\2\u0090\32\3\2\2\2\u0091\u0092")
        buf.write(u"\7(\2\2\u0092\u0093\7(\2\2\u0093\34\3\2\2\2\u0094\u0095")
        buf.write(u"\7~\2\2\u0095\u0096\7~\2\2\u0096\36\3\2\2\2\u0097\u0098")
        buf.write(u"\7#\2\2\u0098 \3\2\2\2\u0099\u009a\7-\2\2\u009a\u009b")
        buf.write(u"\7-\2\2\u009b\"\3\2\2\2\u009c\u009d\7/\2\2\u009d\u009e")
        buf.write(u"\7/\2\2\u009e$\3\2\2\2\u009f\u00a0\7*\2\2\u00a0&\3\2")
        buf.write(u"\2\2\u00a1\u00a2\7+\2\2\u00a2(\3\2\2\2\u00a3\u00a4\7")
        buf.write(u"}\2\2\u00a4*\3\2\2\2\u00a5\u00a6\7\177\2\2\u00a6,\3\2")
        buf.write(u"\2\2\u00a7\u00a8\7=\2\2\u00a8.\3\2\2\2\u00a9\u00aa\7")
        buf.write(u"<\2\2\u00aa\60\3\2\2\2\u00ab\u00ac\7\60\2\2\u00ac\62")
        buf.write(u"\3\2\2\2\u00ad\u00ae\7(\2\2\u00ae\64\3\2\2\2\u00af\u00b0")
        buf.write(u"\7)\2\2\u00b0\66\3\2\2\2\u00b1\u00b2\7^\2\2\u00b28\3")
        buf.write(u"\2\2\2\u00b3\u00b4\7e\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write(u"\7p\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7v\2\2\u00b8:")
        buf.write(u"\3\2\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7k\2\2\u00bb")
        buf.write(u"\u00bc\7i\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write(u"\u00bf\7f\2\2\u00bf<\3\2\2\2\u00c0\u00c1\7w\2\2\u00c1")
        buf.write(u"\u00c2\7p\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write(u"\u00c5\7i\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write(u"\u00c8\7f\2\2\u00c8>\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write(u"\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc@\3\2\2\2\u00cd")
        buf.write(u"\u00ce\7u\2\2\u00ce\u00cf\7j\2\2\u00cf\u00d0\7q\2\2\u00d0")
        buf.write(u"\u00d1\7t\2\2\u00d1\u00dc\7v\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write(u"\u00d4\7j\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write(u"\u00d7\7v\2\2\u00d7\u00d8\7\"\2\2\u00d8\u00d9\7k\2\2")
        buf.write(u"\u00d9\u00da\7p\2\2\u00da\u00dc\7v\2\2\u00db\u00cd\3")
        buf.write(u"\2\2\2\u00db\u00d2\3\2\2\2\u00dcB\3\2\2\2\u00dd\u00de")
        buf.write(u"\7n\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00ea")
        buf.write(u"\7i\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write(u"\7p\2\2\u00e4\u00e5\7i\2\2\u00e5\u00e6\7\"\2\2\u00e6")
        buf.write(u"\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00ea\7v\2\2\u00e9")
        buf.write(u"\u00dd\3\2\2\2\u00e9\u00e1\3\2\2\2\u00eaD\3\2\2\2\u00eb")
        buf.write(u"\u00ec\7n\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write(u"\u00ef\7i\2\2\u00ef\u00f0\7\"\2\2\u00f0\u00f1\7n\2\2")
        buf.write(u"\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u0102\7")
        buf.write(u"i\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7")
        buf.write(u"\7p\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\7\"\2\2\u00f9")
        buf.write(u"\u00fa\7n\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7p\2\2\u00fc")
        buf.write(u"\u00fd\7i\2\2\u00fd\u00fe\7\"\2\2\u00fe\u00ff\7k\2\2")
        buf.write(u"\u00ff\u0100\7p\2\2\u0100\u0102\7v\2\2\u0101\u00eb\3")
        buf.write(u"\2\2\2\u0101\u00f4\3\2\2\2\u0102F\3\2\2\2\u0103\u0107")
        buf.write(u"\t\2\2\2\u0104\u0106\t\3\2\2\u0105\u0104\3\2\2\2\u0106")
        buf.write(u"\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2")
        buf.write(u"\2\u0108\u010c\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010c")
        buf.write(u"\7\62\2\2\u010b\u0103\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write(u"H\3\2\2\2\u010d\u010e\7h\2\2\u010e\u010f\7n\2\2\u010f")
        buf.write(u"\u0110\7q\2\2\u0110\u0111\7c\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write(u"J\3\2\2\2\u0113\u0114\7f\2\2\u0114\u0115\7q\2\2\u0115")
        buf.write(u"\u0116\7w\2\2\u0116\u0117\7d\2\2\u0117\u0118\7n\2\2\u0118")
        buf.write(u"\u0119\7g\2\2\u0119L\3\2\2\2\u011a\u011b\7n\2\2\u011b")
        buf.write(u"\u011c\7q\2\2\u011c\u011d\7p\2\2\u011d\u011e\7i\2\2\u011e")
        buf.write(u"\u011f\7\"\2\2\u011f\u0120\7f\2\2\u0120\u0121\7q\2\2")
        buf.write(u"\u0121\u0122\7w\2\2\u0122\u0123\7d\2\2\u0123\u0124\7")
        buf.write(u"n\2\2\u0124\u0125\7g\2\2\u0125N\3\2\2\2\u0126\u0128\5")
        buf.write(u"G$\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129")
        buf.write(u"\3\2\2\2\u0129\u012b\5\61\31\2\u012a\u012c\t\3\2\2\u012b")
        buf.write(u"\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2")
        buf.write(u"\2\u012d\u012e\3\2\2\2\u012eP\3\2\2\2\u012f\u0130\7e")
        buf.write(u"\2\2\u0130\u0131\7j\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write(u"\7t\2\2\u0133R\3\2\2\2\u0134\u0136\5\65\33\2\u0135\u0137")
        buf.write(u"\5\67\34\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write(u"\u0138\3\2\2\2\u0138\u0139\t\4\2\2\u0139\u013a\5\65\33")
        buf.write(u"\2\u013aT\3\2\2\2\u013b\u013f\7$\2\2\u013c\u013e\5S*")
        buf.write(u"\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d")
        buf.write(u"\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141")
        buf.write(u"\u013f\3\2\2\2\u0142\u0143\7$\2\2\u0143V\3\2\2\2\u0144")
        buf.write(u"\u0145\7r\2\2\u0145\u0146\7t\2\2\u0146\u0147\7k\2\2\u0147")
        buf.write(u"\u0148\7p\2\2\u0148\u0149\7v\2\2\u0149\u014a\7h\2\2\u014a")
        buf.write(u"X\3\2\2\2\u014b\u014c\7k\2\2\u014c\u014d\7h\2\2\u014d")
        buf.write(u"Z\3\2\2\2\u014e\u014f\7g\2\2\u014f\u0150\7n\2\2\u0150")
        buf.write(u"\u0151\7u\2\2\u0151\u0152\7g\2\2\u0152\u0153\7\"\2\2")
        buf.write(u"\u0153\u0154\7k\2\2\u0154\u0155\7h\2\2\u0155\\\3\2\2")
        buf.write(u"\2\u0156\u0157\7g\2\2\u0157\u0158\7n\2\2\u0158\u0159")
        buf.write(u"\7u\2\2\u0159\u015a\7g\2\2\u015a^\3\2\2\2\u015b\u015c")
        buf.write(u"\7h\2\2\u015c\u015d\7q\2\2\u015d\u015e\7t\2\2\u015e`")
        buf.write(u"\3\2\2\2\u015f\u0160\7y\2\2\u0160\u0161\7j\2\2\u0161")
        buf.write(u"\u0162\7k\2\2\u0162\u0163\7n\2\2\u0163\u0164\7g\2\2\u0164")
        buf.write(u"b\3\2\2\2\u0165\u0166\7d\2\2\u0166\u0167\7t\2\2\u0167")
        buf.write(u"\u0168\7g\2\2\u0168\u0169\7c\2\2\u0169\u016a\7m\2\2\u016a")
        buf.write(u"d\3\2\2\2\u016b\u016c\7e\2\2\u016c\u016d\7q\2\2\u016d")
        buf.write(u"\u016e\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170\7k\2\2\u0170")
        buf.write(u"\u0171\7p\2\2\u0171\u0172\7w\2\2\u0172\u0173\7g\2\2\u0173")
        buf.write(u"f\3\2\2\2\u0174\u0175\7u\2\2\u0175\u0176\7y\2\2\u0176")
        buf.write(u"\u0177\7k\2\2\u0177\u0178\7v\2\2\u0178\u0179\7e\2\2\u0179")
        buf.write(u"\u017a\7j\2\2\u017ah\3\2\2\2\u017b\u017c\7e\2\2\u017c")
        buf.write(u"\u017d\7c\2\2\u017d\u017e\7u\2\2\u017e\u017f\7g\2\2\u017f")
        buf.write(u"j\3\2\2\2\u0180\u0181\7f\2\2\u0181\u0182\7g\2\2\u0182")
        buf.write(u"\u0183\7h\2\2\u0183\u0184\7c\2\2\u0184\u0185\7w\2\2\u0185")
        buf.write(u"\u0186\7n\2\2\u0186\u0187\7v\2\2\u0187l\3\2\2\2\u0188")
        buf.write(u"\u018c\t\5\2\2\u0189\u018b\t\6\2\2\u018a\u0189\3\2\2")
        buf.write(u"\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write(u"\3\2\2\2\u018dn\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0191")
        buf.write(u"\t\7\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write(u"\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2")
        buf.write(u"\2\u0194\u0195\b8\2\2\u0195p\3\2\2\2\u0196\u0197\7\61")
        buf.write(u"\2\2\u0197\u0198\7\61\2\2\u0198\u019c\3\2\2\2\u0199\u019b")
        buf.write(u"\13\2\2\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c")
        buf.write(u"\u019d\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019f\3\2\2")
        buf.write(u"\2\u019e\u019c\3\2\2\2\u019f\u01a0\7\f\2\2\u01a0\u01a1")
        buf.write(u"\3\2\2\2\u01a1\u01a2\b9\2\2\u01a2r\3\2\2\2\u01a3\u01a4")
        buf.write(u"\7\61\2\2\u01a4\u01a5\7,\2\2\u01a5\u01a9\3\2\2\2\u01a6")
        buf.write(u"\u01a8\13\2\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2")
        buf.write(u"\2\u01a9\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ac")
        buf.write(u"\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\7,\2\2\u01ad")
        buf.write(u"\u01ae\7\61\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b:\2")
        buf.write(u"\2\u01b0t\3\2\2\2\20\2\u00db\u00e9\u0101\u0107\u010b")
        buf.write(u"\u0127\u012d\u0136\u013f\u018c\u0192\u019c\u01a9\3\b")
        buf.write(u"\2\2")
        return buf.getvalue()


class variablesLexer(Lexer):

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
    LCURlY = 20
    RCULRY = 21
    END_INSTR = 22
    D_POINT = 23
    DOT = 24
    REF = 25
    SQUOTE = 26
    ESC = 27
    CONST = 28
    SIGNED = 29
    UNSIGNED = 30
    INT_PREF = 31
    SHORT_PREF = 32
    LONG_PREF = 33
    LONG_LONG_PREF = 34
    INT = 35
    FLOAT_PREF = 36
    DOUBLE_PREF = 37
    LONG_DOUBLE_PREF = 38
    FLOAT = 39
    CHAR_PREF = 40
    CHAR = 41
    STRING = 42
    PRINTF = 43
    IF = 44
    ELIF = 45
    ELSE = 46
    FOR = 47
    WHILE = 48
    BREAK = 49
    CONTINUE = 50
    SWITCH = 51
    CASE = 52
    DEFAULT = 53
    ID = 54
    WS = 55
    SINGLE_COMMENT = 56
    MULTI_COMMENT = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'*'", u"'/'", u"'+'", u"'-'", u"'<'", u"'>'", u"'=='", u"'='", 
            u"'%'", u"'<='", u"'>='", u"'!='", u"'&&'", u"'||'", u"'!'", 
            u"'++'", u"'--'", u"'('", u"')'", u"'{'", u"'}'", u"';'", u"':'", 
            u"'.'", u"'&'", u"'''", u"'\\'", u"'const'", u"'signed'", u"'unsigned'", 
            u"'int'", u"'float'", u"'double'", u"'long double'", u"'char'", 
            u"'printf'", u"'if'", u"'else if'", u"'else'", u"'for'", u"'while'", 
            u"'break'", u"'continue'", u"'switch'", u"'case'", u"'default'" ]

    symbolicNames = [ u"<INVALID>",
            u"MUL", u"DIV", u"ADD", u"SUB", u"LT", u"GT", u"DEQ", u"EQ", 
            u"MOD", u"LTE", u"GTE", u"NEQ", u"AND", u"OR", u"NOT", u"INCR", 
            u"DECR", u"LBRACKET", u"RBRACKET", u"LCURlY", u"RCULRY", u"END_INSTR", 
            u"D_POINT", u"DOT", u"REF", u"SQUOTE", u"ESC", u"CONST", u"SIGNED", 
            u"UNSIGNED", u"INT_PREF", u"SHORT_PREF", u"LONG_PREF", u"LONG_LONG_PREF", 
            u"INT", u"FLOAT_PREF", u"DOUBLE_PREF", u"LONG_DOUBLE_PREF", 
            u"FLOAT", u"CHAR_PREF", u"CHAR", u"STRING", u"PRINTF", u"IF", 
            u"ELIF", u"ELSE", u"FOR", u"WHILE", u"BREAK", u"CONTINUE", u"SWITCH", 
            u"CASE", u"DEFAULT", u"ID", u"WS", u"SINGLE_COMMENT", u"MULTI_COMMENT" ]

    ruleNames = [ u"MUL", u"DIV", u"ADD", u"SUB", u"LT", u"GT", u"DEQ", 
                  u"EQ", u"MOD", u"LTE", u"GTE", u"NEQ", u"AND", u"OR", 
                  u"NOT", u"INCR", u"DECR", u"LBRACKET", u"RBRACKET", u"LCURlY", 
                  u"RCULRY", u"END_INSTR", u"D_POINT", u"DOT", u"REF", u"SQUOTE", 
                  u"ESC", u"CONST", u"SIGNED", u"UNSIGNED", u"INT_PREF", 
                  u"SHORT_PREF", u"LONG_PREF", u"LONG_LONG_PREF", u"INT", 
                  u"FLOAT_PREF", u"DOUBLE_PREF", u"LONG_DOUBLE_PREF", u"FLOAT", 
                  u"CHAR_PREF", u"CHAR", u"STRING", u"PRINTF", u"IF", u"ELIF", 
                  u"ELSE", u"FOR", u"WHILE", u"BREAK", u"CONTINUE", u"SWITCH", 
                  u"CASE", u"DEFAULT", u"ID", u"WS", u"SINGLE_COMMENT", 
                  u"MULTI_COMMENT" ]

    grammarFileName = u"loops.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(variablesLexer, self).__init__(input, output=output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


