import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
"""if not './main/bkit/parser/' in sys.path:
    sys.path.append('./main/bkit/parser/')
if os.path.isdir('../target/main/bkit/parser') and not '../target/main/bkit/parser/' in sys.path:
    sys.path.append('../target/main/bkit/parser/')"""
from BKITLexer import BKITLexer
from BKITParser import BKITParser
from lexererr import *
from ASTGeneration import ASTGeneration

testcase = "./test2string/GenSuite.py"
testfile = open(testcase,"w")
testfile.write("""import unittest
from TestUtils import TestAST
from AST import *
from main.bkit.utils.AST import ArrayLiteral, BooleanLiteral, FloatLiteral, IntLiteral, Program, StringLiteral

class ASTGenSuite(unittest.TestCase):""")

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        """tmp = repr(inputStr)
        file.write(tmp[1:-1])"""
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+","+str(tok.type)+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg


class TestAST:
    __count = 301
    @staticmethod
    def checkASTGen(input,expect,num):
        testfile.write("""
    def test_""" + str(TestAST._TestAST__count) + """(self):
        input = \"\"\"""" + input + """\"\"\" 
        expect = """)

        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = BKITLexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()

        testfile.write(line + """
        self.assertTrue(TestAST.checkASTGen(input,expect,"""+str(TestAST._TestAST__count)+"""))\n""")
        TestAST.__count += 1

        return line == str(expect)
        
        
