# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0215\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\7\27\u0120\n\27\f\27\16\27\u0123\13\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\5\32")
        buf.write("\u0130\n\32\3\32\6\32\u0133\n\32\r\32\16\32\u0134\3\33")
        buf.write("\3\33\5\33\u0139\n\33\3\34\3\34\3\34\3\34\5\34\u013f\n")
        buf.write("\34\3\35\3\35\3\35\3\35\5\35\u0145\n\35\3\36\3\36\3\36")
        buf.write("\5\36\u014a\n\36\3\37\3\37\3\37\7\37\u014f\n\37\f\37\16")
        buf.write("\37\u0152\13\37\5\37\u0154\n\37\3 \3 \3 \3 \7 \u015a\n")
        buf.write(" \f \16 \u015d\13 \3!\3!\3!\3!\7!\u0163\n!\f!\16!\u0166")
        buf.write("\13!\3\"\6\"\u0169\n\"\r\"\16\"\u016a\3\"\3\"\7\"\u016f")
        buf.write("\n\"\f\"\16\"\u0172\13\"\3\"\5\"\u0175\n\"\3\"\6\"\u0178")
        buf.write("\n\"\r\"\16\"\u0179\3\"\5\"\u017d\n\"\3\"\3\"\5\"\u0181")
        buf.write("\n\"\3#\3#\5#\u0185\n#\3$\3$\7$\u0189\n$\f$\16$\u018c")
        buf.write("\13$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\7G\u01e9\nG\fG\16G\u01ec\13G\3H\6H\u01ef\nH\rH\16")
        buf.write("H\u01f0\3H\3H\3I\3I\3J\3J\7J\u01f9\nJ\fJ\16J\u01fc\13")
        buf.write("J\3J\5J\u01ff\nJ\3J\3J\3K\3K\7K\u0205\nK\fK\16K\u0208")
        buf.write("\13K\3K\3K\3K\3L\3L\3L\3L\7L\u0211\nL\fL\16L\u0214\13")
        buf.write("L\4\u0121\u0212\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\2\61\2\63\2\65\2\67\29\2;\31=\32?\33")
        buf.write("A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60")
        buf.write("k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=")
        buf.write("\u0085>\u0087?\u0089@\u008bA\u008dB\u008fC\u0091D\u0093")
        buf.write("E\u0095F\u0097G\3\2\23\3\2\62;\3\2\63;\4\2GGgg\4\2--/")
        buf.write("/\6\2\f\f$$))^^\t\2))^^ddhhppttvv\3\2$$\4\2ZZzz\4\2\63")
        buf.write(";CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\3\2c|\6\2\62;C\\")
        buf.write("aac|\5\2\13\f\17\17\"\"\3\3\f\f\2\u0227\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2;\3\2\2\2\2=")
        buf.write("\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2")
        buf.write("G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009e\3\2\2")
        buf.write("\2\7\u00a3\3\2\2\2\t\u00aa\3\2\2\2\13\u00ad\3\2\2\2\r")
        buf.write("\u00b1\3\2\2\2\17\u00b7\3\2\2\2\21\u00bd\3\2\2\2\23\u00c4")
        buf.write("\3\2\2\2\25\u00cd\3\2\2\2\27\u00d7\3\2\2\2\31\u00dd\3")
        buf.write("\2\2\2\33\u00e6\3\2\2\2\35\u00ee\3\2\2\2\37\u00f2\3\2")
        buf.write("\2\2!\u00f9\3\2\2\2#\u00fe\3\2\2\2%\u0104\3\2\2\2\'\u0107")
        buf.write("\3\2\2\2)\u010d\3\2\2\2+\u0116\3\2\2\2-\u011b\3\2\2\2")
        buf.write("/\u0129\3\2\2\2\61\u012b\3\2\2\2\63\u012d\3\2\2\2\65\u0138")
        buf.write("\3\2\2\2\67\u013e\3\2\2\29\u0144\3\2\2\2;\u0149\3\2\2")
        buf.write("\2=\u0153\3\2\2\2?\u0155\3\2\2\2A\u015e\3\2\2\2C\u0180")
        buf.write("\3\2\2\2E\u0184\3\2\2\2G\u0186\3\2\2\2I\u0190\3\2\2\2")
        buf.write("K\u0192\3\2\2\2M\u0194\3\2\2\2O\u0196\3\2\2\2Q\u0198\3")
        buf.write("\2\2\2S\u019a\3\2\2\2U\u019d\3\2\2\2W\u01a0\3\2\2\2Y\u01a3")
        buf.write("\3\2\2\2[\u01a6\3\2\2\2]\u01a8\3\2\2\2_\u01ab\3\2\2\2")
        buf.write("a\u01ae\3\2\2\2c\u01b1\3\2\2\2e\u01b4\3\2\2\2g\u01b6\3")
        buf.write("\2\2\2i\u01b8\3\2\2\2k\u01bb\3\2\2\2m\u01be\3\2\2\2o\u01c2")
        buf.write("\3\2\2\2q\u01c5\3\2\2\2s\u01c8\3\2\2\2u\u01cc\3\2\2\2")
        buf.write("w\u01d0\3\2\2\2y\u01d2\3\2\2\2{\u01d4\3\2\2\2}\u01d6\3")
        buf.write("\2\2\2\177\u01d8\3\2\2\2\u0081\u01da\3\2\2\2\u0083\u01dc")
        buf.write("\3\2\2\2\u0085\u01de\3\2\2\2\u0087\u01e0\3\2\2\2\u0089")
        buf.write("\u01e2\3\2\2\2\u008b\u01e4\3\2\2\2\u008d\u01e6\3\2\2\2")
        buf.write("\u008f\u01ee\3\2\2\2\u0091\u01f4\3\2\2\2\u0093\u01f6\3")
        buf.write("\2\2\2\u0095\u0202\3\2\2\2\u0097\u020c\3\2\2\2\u0099\u009a")
        buf.write("\7D\2\2\u009a\u009b\7q\2\2\u009b\u009c\7f\2\2\u009c\u009d")
        buf.write("\7{\2\2\u009d\4\3\2\2\2\u009e\u009f\7G\2\2\u009f\u00a0")
        buf.write("\7n\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2\7g\2\2\u00a2\6")
        buf.write("\3\2\2\2\u00a3\u00a4\7G\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7f\2\2\u00a6\u00a7\7H\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\b\3\2\2\2\u00aa\u00ab\7K\2\2\u00ab\u00ac")
        buf.write("\7h\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7X\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7t\2\2\u00b0\f\3\2\2\2\u00b1\u00b2")
        buf.write("\7G\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7f\2\2\u00b4\u00b5")
        buf.write("\7F\2\2\u00b5\u00b6\7q\2\2\u00b6\16\3\2\2\2\u00b7\u00b8")
        buf.write("\7D\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7m\2\2\u00bc\20\3\2\2\2\u00bd\u00be")
        buf.write("\7G\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7K\2\2\u00c2\u00c3\7h\2\2\u00c3\22")
        buf.write("\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7\u00c8\7Y\2\2\u00c8\u00c9\7j\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7g\2\2\u00cc\24")
        buf.write("\3\2\2\2\u00cd\u00ce\7R\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7o\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7Y\2\2\u00d8\u00d9")
        buf.write("\7j\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7E\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7G\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea\7D\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7f\2\2\u00ec\u00ed\7{\2\2\u00ed\34")
        buf.write("\3\2\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7p\2\2\u00f8 \3\2\2\2\u00f9\u00fa")
        buf.write("\7V\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7H\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7n\2\2\u0101\u0102\7u\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103$\3\2\2\2\u0104\u0105\7F\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106&\3\2\2\2\u0107\u0108\7G\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7f\2\2\u010a\u010b\7K\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c(\3\2\2\2\u010d\u010e\7H\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7p\2\2\u0110\u0111\7e\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7k\2\2\u0113\u0114\7q\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115*\3\2\2\2\u0116\u0117\7V\2\2\u0117\u0118")
        buf.write("\7j\2\2\u0118\u0119\7g\2\2\u0119\u011a\7p\2\2\u011a,\3")
        buf.write("\2\2\2\u011b\u011c\7,\2\2\u011c\u011d\7,\2\2\u011d\u0121")
        buf.write("\3\2\2\2\u011e\u0120\13\2\2\2\u011f\u011e\3\2\2\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u0122\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\7")
        buf.write(",\2\2\u0125\u0126\7,\2\2\u0126\u0127\3\2\2\2\u0127\u0128")
        buf.write("\b\27\2\2\u0128.\3\2\2\2\u0129\u012a\t\2\2\2\u012a\60")
        buf.write("\3\2\2\2\u012b\u012c\t\3\2\2\u012c\62\3\2\2\2\u012d\u012f")
        buf.write("\t\4\2\2\u012e\u0130\t\5\2\2\u012f\u012e\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0133\5/\30\2")
        buf.write("\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3")
        buf.write("\2\2\2\u0134\u0135\3\2\2\2\u0135\64\3\2\2\2\u0136\u0139")
        buf.write("\n\6\2\2\u0137\u0139\5\67\34\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139\66\3\2\2\2\u013a\u013b\7^\2\2\u013b")
        buf.write("\u013f\t\7\2\2\u013c\u013d\7)\2\2\u013d\u013f\7$\2\2\u013e")
        buf.write("\u013a\3\2\2\2\u013e\u013c\3\2\2\2\u013f8\3\2\2\2\u0140")
        buf.write("\u0141\7^\2\2\u0141\u0145\n\7\2\2\u0142\u0143\7)\2\2\u0143")
        buf.write("\u0145\n\b\2\2\u0144\u0140\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0145:\3\2\2\2\u0146\u014a\5=\37\2\u0147\u014a\5? \2")
        buf.write("\u0148\u014a\5A!\2\u0149\u0146\3\2\2\2\u0149\u0147\3\2")
        buf.write("\2\2\u0149\u0148\3\2\2\2\u014a<\3\2\2\2\u014b\u0154\7")
        buf.write("\62\2\2\u014c\u0150\5\61\31\2\u014d\u014f\5/\30\2\u014e")
        buf.write("\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3")
        buf.write("\2\2\2\u0153\u014b\3\2\2\2\u0153\u014c\3\2\2\2\u0154>")
        buf.write("\3\2\2\2\u0155\u0156\7\62\2\2\u0156\u0157\t\t\2\2\u0157")
        buf.write("\u015b\t\n\2\2\u0158\u015a\t\13\2\2\u0159\u0158\3\2\2")
        buf.write("\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c@\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f")
        buf.write("\7\62\2\2\u015f\u0160\t\f\2\2\u0160\u0164\t\r\2\2\u0161")
        buf.write("\u0163\t\16\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2")
        buf.write("\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165B\3\2")
        buf.write("\2\2\u0166\u0164\3\2\2\2\u0167\u0169\5/\30\2\u0168\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u0170\5\u0081")
        buf.write("A\2\u016d\u016f\5/\30\2\u016e\u016d\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\5\63\32")
        buf.write("\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0181")
        buf.write("\3\2\2\2\u0176\u0178\5/\30\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017c\3\2\2\2\u017b\u017d\5\u0081A\2\u017c\u017b")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017f\5\63\32\2\u017f\u0181\3\2\2\2\u0180\u0168\3\2\2")
        buf.write("\2\u0180\u0177\3\2\2\2\u0181D\3\2\2\2\u0182\u0185\5!\21")
        buf.write("\2\u0183\u0185\5#\22\2\u0184\u0182\3\2\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185F\3\2\2\2\u0186\u018a\7$\2\2\u0187\u0189")
        buf.write("\5\65\33\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2")
        buf.write("\u018c\u018a\3\2\2\2\u018d\u018e\7$\2\2\u018e\u018f\b")
        buf.write("$\3\2\u018fH\3\2\2\2\u0190\u0191\7-\2\2\u0191J\3\2\2\2")
        buf.write("\u0192\u0193\7/\2\2\u0193L\3\2\2\2\u0194\u0195\7,\2\2")
        buf.write("\u0195N\3\2\2\2\u0196\u0197\7^\2\2\u0197P\3\2\2\2\u0198")
        buf.write("\u0199\7\'\2\2\u0199R\3\2\2\2\u019a\u019b\7-\2\2\u019b")
        buf.write("\u019c\7\60\2\2\u019cT\3\2\2\2\u019d\u019e\7/\2\2\u019e")
        buf.write("\u019f\7\60\2\2\u019fV\3\2\2\2\u01a0\u01a1\7,\2\2\u01a1")
        buf.write("\u01a2\7\60\2\2\u01a2X\3\2\2\2\u01a3\u01a4\7^\2\2\u01a4")
        buf.write("\u01a5\7\60\2\2\u01a5Z\3\2\2\2\u01a6\u01a7\7#\2\2\u01a7")
        buf.write("\\\3\2\2\2\u01a8\u01a9\7(\2\2\u01a9\u01aa\7(\2\2\u01aa")
        buf.write("^\3\2\2\2\u01ab\u01ac\7~\2\2\u01ac\u01ad\7~\2\2\u01ad")
        buf.write("`\3\2\2\2\u01ae\u01af\7?\2\2\u01af\u01b0\7?\2\2\u01b0")
        buf.write("b\3\2\2\2\u01b1\u01b2\7#\2\2\u01b2\u01b3\7?\2\2\u01b3")
        buf.write("d\3\2\2\2\u01b4\u01b5\7>\2\2\u01b5f\3\2\2\2\u01b6\u01b7")
        buf.write("\7@\2\2\u01b7h\3\2\2\2\u01b8\u01b9\7>\2\2\u01b9\u01ba")
        buf.write("\7?\2\2\u01baj\3\2\2\2\u01bb\u01bc\7@\2\2\u01bc\u01bd")
        buf.write("\7?\2\2\u01bdl\3\2\2\2\u01be\u01bf\7?\2\2\u01bf\u01c0")
        buf.write("\7\61\2\2\u01c0\u01c1\7?\2\2\u01c1n\3\2\2\2\u01c2\u01c3")
        buf.write("\7>\2\2\u01c3\u01c4\7\60\2\2\u01c4p\3\2\2\2\u01c5\u01c6")
        buf.write("\7@\2\2\u01c6\u01c7\7\60\2\2\u01c7r\3\2\2\2\u01c8\u01c9")
        buf.write("\7>\2\2\u01c9\u01ca\7?\2\2\u01ca\u01cb\7\60\2\2\u01cb")
        buf.write("t\3\2\2\2\u01cc\u01cd\7@\2\2\u01cd\u01ce\7?\2\2\u01ce")
        buf.write("\u01cf\7\60\2\2\u01cfv\3\2\2\2\u01d0\u01d1\7*\2\2\u01d1")
        buf.write("x\3\2\2\2\u01d2\u01d3\7+\2\2\u01d3z\3\2\2\2\u01d4\u01d5")
        buf.write("\7]\2\2\u01d5|\3\2\2\2\u01d6\u01d7\7_\2\2\u01d7~\3\2\2")
        buf.write("\2\u01d8\u01d9\7<\2\2\u01d9\u0080\3\2\2\2\u01da\u01db")
        buf.write("\7\60\2\2\u01db\u0082\3\2\2\2\u01dc\u01dd\7.\2\2\u01dd")
        buf.write("\u0084\3\2\2\2\u01de\u01df\7=\2\2\u01df\u0086\3\2\2\2")
        buf.write("\u01e0\u01e1\7}\2\2\u01e1\u0088\3\2\2\2\u01e2\u01e3\7")
        buf.write("\177\2\2\u01e3\u008a\3\2\2\2\u01e4\u01e5\7?\2\2\u01e5")
        buf.write("\u008c\3\2\2\2\u01e6\u01ea\t\17\2\2\u01e7\u01e9\t\20\2")
        buf.write("\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u008e\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ed\u01ef\t\21\2\2\u01ee\u01ed\3\2\2")
        buf.write("\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bH\2\2\u01f3")
        buf.write("\u0090\3\2\2\2\u01f4\u01f5\13\2\2\2\u01f5\u0092\3\2\2")
        buf.write("\2\u01f6\u01fa\7$\2\2\u01f7\u01f9\5\65\33\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fd\u01ff\t\22\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0200")
        buf.write("\3\2\2\2\u0200\u0201\bJ\4\2\u0201\u0094\3\2\2\2\u0202")
        buf.write("\u0206\7$\2\2\u0203\u0205\5\65\33\2\u0204\u0203\3\2\2")
        buf.write("\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u0206\3\2\2\2\u0209")
        buf.write("\u020a\59\35\2\u020a\u020b\bK\5\2\u020b\u0096\3\2\2\2")
        buf.write("\u020c\u020d\7,\2\2\u020d\u020e\7,\2\2\u020e\u0212\3\2")
        buf.write("\2\2\u020f\u0211\13\2\2\2\u0210\u020f\3\2\2\2\u0211\u0214")
        buf.write("\3\2\2\2\u0212\u0213\3\2\2\2\u0212\u0210\3\2\2\2\u0213")
        buf.write("\u0098\3\2\2\2\u0214\u0212\3\2\2\2\34\2\u0121\u012f\u0134")
        buf.write("\u0138\u013e\u0144\u0149\u0150\u0153\u015b\u0164\u016a")
        buf.write("\u0170\u0174\u0179\u017c\u0180\u0184\u018a\u01ea\u01f0")
        buf.write("\u01fa\u01fe\u0206\u0212\6\b\2\2\3$\2\3J\3\3K\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BODY = 1
    ELSE = 2
    ENDFOR = 3
    IF = 4
    VAR = 5
    ENDDO = 6
    BREAK = 7
    ELSEIF = 8
    ENDWHILE = 9
    PAR = 10
    WHILE = 11
    CONT = 12
    ENDBODY = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    DO = 18
    ENDIF = 19
    FUNCTION = 20
    THEN = 21
    BLOCK_COMMENT = 22
    Intlit = 23
    INTLIT = 24
    HEXALIT = 25
    OCTLIT = 26
    FLOATLIT = 27
    BOOLEAN = 28
    STRINGLIT = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    ADDF = 35
    SUBF = 36
    MULF = 37
    DIVF = 38
    NOT = 39
    AND = 40
    OR = 41
    EQUAL = 42
    NOT_EQUAL = 43
    LT = 44
    GT = 45
    LE = 46
    GE = 47
    NOT_EQUALF = 48
    LTF = 49
    GTF = 50
    LEF = 51
    GEF = 52
    LP = 53
    RP = 54
    LS = 55
    RS = 56
    CL = 57
    DOT = 58
    CM = 59
    SM = 60
    LB = 61
    RB = 62
    ASSIGN = 63
    ID = 64
    WS = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    UNTERMINATED_COMMENT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'False'", 
            "'Do'", "'EndIf'", "'Function'", "'Then'", "'+'", "'-'", "'*'", 
            "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
            "':'", "'.'", "','", "';'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", 
            "ENDWHILE", "PAR", "WHILE", "CONT", "ENDBODY", "FOR", "RETURN", 
            "TRUE", "FALSE", "DO", "ENDIF", "FUNCTION", "THEN", "BLOCK_COMMENT", 
            "Intlit", "INTLIT", "HEXALIT", "OCTLIT", "FLOATLIT", "BOOLEAN", 
            "STRINGLIT", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDF", "SUBF", 
            "MULF", "DIVF", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
            "GT", "LE", "GE", "NOT_EQUALF", "LTF", "GTF", "LEF", "GEF", 
            "LP", "RP", "LS", "RS", "CL", "DOT", "CM", "SM", "LB", "RB", 
            "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", 
                  "ELSEIF", "ENDWHILE", "PAR", "WHILE", "CONT", "ENDBODY", 
                  "FOR", "RETURN", "TRUE", "FALSE", "DO", "ENDIF", "FUNCTION", 
                  "THEN", "BLOCK_COMMENT", "Digit", "NonZeroDigit", "Exp", 
                  "STR_CHAR", "ESC_SEQ", "ILLEGAL_CHAR", "Intlit", "INTLIT", 
                  "HEXALIT", "OCTLIT", "FLOATLIT", "BOOLEAN", "STRINGLIT", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "ADDF", "SUBF", "MULF", 
                  "DIVF", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
                  "GT", "LE", "GE", "NOT_EQUALF", "LTF", "GTF", "LEF", "GEF", 
                  "LP", "RP", "LS", "RS", "CL", "DOT", "CM", "SM", "LB", 
                  "RB", "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[34] = self.STRINGLIT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:]
                if self.text[-1] == '\n':
                    self.text = self.text[:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:]

     


