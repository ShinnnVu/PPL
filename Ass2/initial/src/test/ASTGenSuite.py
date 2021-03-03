import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_1(self):
        """Simple program: int main() {} """
        input = """Var:x, y, z,a,b,c,d,e,f;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None), VarDecl(Id("a"), [], None), VarDecl(
            Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_2(self):
        """Simple program: int main() {} """
        input = """Var:x = 1, y = 0X5F, z = 0O11, k = True, z = False;
                   Var: x = 1e05 , y = 1.e05 , z= 1.25 , k ="Hohoho";
                   Var: x =" hehe " , y = {} , z = {1,2,3} ,k ={1,{2,3},True};"""
        expect = Program([VarDecl(Id("x"), [], IntLiteral(1)), VarDecl(Id("y"), [], IntLiteral(95)), VarDecl(Id("z"), [], IntLiteral(9)), VarDecl(Id("k"), [], BooleanLiteral(True)), VarDecl(Id("z"), [], BooleanLiteral(False)), VarDecl(Id("x"), [], FloatLiteral(100000.0)), VarDecl(Id("y"), [], FloatLiteral(100000.0)), VarDecl(Id("z"), [], FloatLiteral(
            1.25)), VarDecl(Id("k"), [], StringLiteral("Hohoho")), VarDecl(Id("x"), [], StringLiteral(" hehe ")), VarDecl(Id("y"), [], ArrayLiteral([])), VarDecl(Id("z"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), VarDecl(Id("k"), [], ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(2), IntLiteral(3)]), BooleanLiteral(True)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_3(self):
        input = """Var: x = {1,1e05,{1,2,3,True,{{{}}}},"hohoho"};
                    Var: x[1], y[1][2][3] , z[1] = 5;"""
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral([IntLiteral(1), FloatLiteral(100000.0), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), BooleanLiteral(True), ArrayLiteral(
            [ArrayLiteral([ArrayLiteral([])])])]), StringLiteral("hohoho")])), VarDecl(Id("x"), [1], None), VarDecl(Id("y"), [1, 2, 3], None), VarDecl(Id("z"), [1], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_4(self):
        input = """Var: x[1] = 1, x[0X1] = 2;
                    Var: x[1], y[1][2][3][4][0X11][0O11] , z[1] = 5;"""
        expect = Program([VarDecl(Id("x"), [1], IntLiteral(1)), VarDecl(Id("x"), [1], IntLiteral(2)), VarDecl(
            Id("x"), [1], None), VarDecl(Id("y"), [1, 2, 3, 4, 17, 9], None), VarDecl(Id("z"), [1], IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_5(self):
        """Simple program: int main() {} """
        input = """Var: b[1] = {{1,2,3},{4,5,6},{}};
                        Var: x;
                        Var: x[1][2][3][4][5];
                        Var: m,n[10];
                        Var: a, b = 1, c, d,e ={1};"""
        expect = Program([VarDecl(Id("b"), [1], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)]), ArrayLiteral([])])), VarDecl(Id("x"), [], None), VarDecl(Id("x"), [
                         1, 2, 3, 4, 5], None), VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None), VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], IntLiteral(1)), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("e"), [], ArrayLiteral([IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_6(self):
        input = """Var   :   x,b="bla bla" ;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(
            Id("b"), [], StringLiteral("bla bla"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_7(self):
        input = """Var: x="This is John:'"Where you?'"";"""
        expect = Program(
            [VarDecl(Id("x"), [], StringLiteral("This is John:\'\"Where you?\'\""))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_8(self):
        input = """Var: x[1] = {{"ga","@#@#!@"}, {1,2,3}};"""
        expect = Program([VarDecl(Id("x"), [1], ArrayLiteral([ArrayLiteral([StringLiteral(
            "ga"), StringLiteral("@#@#!@")]), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_9(self):
        input = """Var: x = " '"this is a string'". ", y =0X1234, z = 0O1234 , a= 123 , b= 12.e-5; """
        expect = Program([VarDecl(Id("x"), [], StringLiteral(" \'\"this is a string\'\". ")), VarDecl(Id("y"), [], IntLiteral(4660)), VarDecl(
            Id("z"), [], IntLiteral(668)), VarDecl(Id("a"), [], IntLiteral(123)), VarDecl(Id("b"), [], FloatLiteral(0.00012))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_10(self):
        input = """Var: x = {{{1}}} ;"""
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral(
            [ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_11(self):
        input = """ Var: x[1][2][3][4] = {{{"abc","\\r\\n"},"abc"},1234};"""
        expect = Program([VarDecl(Id("x"), [1, 2, 3, 4], ArrayLiteral([ArrayLiteral([ArrayLiteral(
            [StringLiteral("abc"), StringLiteral("\\r\\n")]), StringLiteral("abc")]), IntLiteral(1234)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_12(self):
        input = """ Function: a
            Parameter: a,b,c,d, e[10], f[1][2][3][4]
            Body:
            a = 5+1;
            b[1][2][3][4] = 1*3;
            foo(1+5)[1][2][3] = (1*3)+(6*2);
            (1+1)[foo()][a[1][2]] = foo(1, True, 1., "abcd")[a][b][c];
            EndBody.
            """
        expect = Program([FuncDecl(Id("a"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("e"), [10], None), VarDecl(Id("f"), [1, 2, 3, 4], None)], ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(5), IntLiteral(1))), Assign(ArrayCell(Id("b"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]), BinaryOp("*", IntLiteral(1), IntLiteral(3))), Assign(ArrayCell(CallExpr(Id("foo"), [BinaryOp(
            "+", IntLiteral(1), IntLiteral(5))]), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), BinaryOp("+", BinaryOp("*", IntLiteral(1), IntLiteral(3)), BinaryOp("*", IntLiteral(6), IntLiteral(2)))), Assign(ArrayCell(BinaryOp("+", IntLiteral(1), IntLiteral(1)), [CallExpr(Id("foo"), []), ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)])]), ArrayCell(CallExpr(Id("foo"), [IntLiteral(1), BooleanLiteral(True), FloatLiteral(1.0), StringLiteral("abcd")]), [Id("a"), Id("b"), Id("c")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_13(self):
        input = """
Var: a, b;
Var: c;

Function: foo
    Body:
    EndBody.

Function: foo2
    Body:
    EndBody.
Function: foo3
    Body:
    EndBody.
"""
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), FuncDecl(
            Id("foo"), [], ([], [])), FuncDecl(Id("foo2"), [], ([], [])), FuncDecl(Id("foo3"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    """ Variable declaration """

    def test_14(self):
        input = """
Var: a1[0];
Var: a1[1], a2[1][2], a3[1][2][3], a4[1][2][3][4];
Var: a5[1][2][3][4][5];
"""
        expect = Program([VarDecl(Id("a1"), [0], None), VarDecl(Id("a1"), [1], None), VarDecl(Id("a2"), [1, 2], None), VarDecl(
            Id("a3"), [1, 2, 3], None), VarDecl(Id("a4"), [1, 2, 3, 4], None), VarDecl(Id("a5"), [1, 2, 3, 4, 5], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_15(self):
        input = """
Var: a1[0o7][0o6][0o5][0o4][0o3][0o2][0o1][0o111];
Var: a1[0O1][0O2][0O3][0O4][0O5][0O6][0O7];
Var: a1[0o10000000], a1[0O1234567];
"""
        expect = Program([VarDecl(Id("a1"), [7, 6, 5, 4, 3, 2, 1, 73], None), VarDecl(Id("a1"), [
                         1, 2, 3, 4, 5, 6, 7], None), VarDecl(Id("a1"), [2097152], None), VarDecl(Id("a1"), [342391], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_16(self):
        input = """
Var: a[0x1][0x2][0x3][0x4][0x5][0x6][0x7][0x8][0x9];
Var: b[0xA][0xB][0xC][0xD][0xE][0xF];
Var: c[0X1][0X2][0X3][0X4][0X5][0X6][0X7][0X8][0X9];
Var: d[0XA][0XB][0XC][0XD][0XE][0XF];
Var: e[0x123456], e[0XFECBDE];
"""
        expect = Program([VarDecl(Id("a"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None), VarDecl(Id("b"), [10, 11, 12, 13, 14, 15], None), VarDecl(Id("c"), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9], None), VarDecl(Id("d"), [10, 11, 12, 13, 14, 15], None), VarDecl(Id("e"), [1193046], None), VarDecl(Id("e"), [16698334], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    """ Function declaration """

    def test_17(self):
        input = """
Function: main
    Body:
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_18(self):
        input = """
Function: main
    Body:
        Var: a;
        Var: b;
        Var: c[1][2][3][4];
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(
            Id("b"), [], None), VarDecl(Id("c"), [1, 2, 3, 4], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_19(self):
        input = """
Function: main
    Body:
        foo();
        foo(1+3,2+5);
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), []), CallStmt(Id("foo"), [
                         BinaryOp("+", IntLiteral(1), IntLiteral(3)), BinaryOp("+", IntLiteral(2), IntLiteral(5))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_20(self):
        input = """
Function: main
    Body:
        Var: a, b;
        foo1();
        foo2();
        foo3();
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], [
                         CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), []), CallStmt(Id("foo3"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_21(self):
        input = """
            Function: function
            Parameter: a,b,c,d, e[10], f[1][2][3][4]
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                EndBody.
            """
        expect = Program([FuncDecl(Id("function"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("e"), [10], None), VarDecl(Id("f"), [1, 2, 3, 4], None)], ([VarDecl(
            Id("r"), [], FloatLiteral(10.0)), VarDecl(Id("v"), [], None)], [Assign(Id("v"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("\.", FloatLiteral(4.0), FloatLiteral(3.0)), FloatLiteral(3.14)), Id("r")), Id("r")), Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_22(self):
        input = """
            Function: test
            Body:
                Var: arr[2][3] = {{"Hi","Hello"},"Bai","Bye",{}};
                a= 10e2;
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("arr"), [2, 3], ArrayLiteral([ArrayLiteral([StringLiteral("Hi"), StringLiteral(
            "Hello")]), StringLiteral("Bai"), StringLiteral("Bye"), ArrayLiteral([])]))], [Assign(Id("a"), FloatLiteral(1000.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_23(self):
        input = """
            Function: boo
            Body:
                Var: x, b =5 , c[1][2][3] = {{1,2},{3,4},{5,6}};
                a =  1 \\ 2 \\ 3 \\ 4 \\ 5 \\6 \\.7;
            EndBody.
            """
        expect = Program([FuncDecl(Id("boo"), [], ([VarDecl(Id("x"), [], None), VarDecl(Id("b"), [], IntLiteral(5)), VarDecl(Id("c"), [1, 2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)]), ArrayLiteral(
            [IntLiteral(5), IntLiteral(6)])]))], [Assign(Id("a"), BinaryOp("\.", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)), IntLiteral(5)), IntLiteral(6)), IntLiteral(7)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_24(self):
        input = """
            Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Return 1;
            EndBody.
            """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None), VarDecl(
            Id("b"), [], None)], ([VarDecl(Id("i"), [], IntLiteral(0))], [Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_25(self):
        input = """
            Function: foo
            Parameter: a[10], b, c, d
            Body:
                Var: i = {12.,{2,{{2.e5},"hi"},4.}};
            EndBody.
            """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [10], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], ([VarDecl(Id("i"), [
        ], ArrayLiteral([FloatLiteral(12.0), ArrayLiteral([IntLiteral(2), ArrayLiteral([ArrayLiteral([FloatLiteral(200000.0)]), StringLiteral("hi")]), FloatLiteral(4.0)])]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_26(self):
        input = """
            Function: test___
            Parameter: x[10], a[2][3][2][9]
            Body:
                Return test({1,2,3,4,5,6,7,8,9,10}, {"abcd","efgh"});
            EndBody.
            """
        expect = Program([FuncDecl(Id("test___"), [VarDecl(Id("x"), [10], None), VarDecl(Id("a"), [2, 3, 2, 9], None)], ([], [Return(CallExpr(Id("test"), [ArrayLiteral([IntLiteral(1), IntLiteral(
            2), IntLiteral(3), IntLiteral(4), IntLiteral(5), IntLiteral(6), IntLiteral(7), IntLiteral(8), IntLiteral(9), IntLiteral(10)]), ArrayLiteral([StringLiteral("abcd"), StringLiteral("efgh")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
                Var: x = 12345;
                Var: y = 0;
                Var: z = 12.e5;
                Var: g = 22.;
                Var: h = 12.0e5;
                Var: t = 12e5;
                Var: x = True;
                Var: a = False;
                Var: z = "This is a string \\n \\n \\n \\n \\n '" ";
                Var: k = {1,2} , m = {{"A","a"},"b"};
            EndBody.
            """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([VarDecl(Id("x"), [], IntLiteral(12345)), VarDecl(Id("y"), [], IntLiteral(0)), VarDecl(Id("z"), [], FloatLiteral(1200000.0)), VarDecl(Id("g"), [], FloatLiteral(22.0)), VarDecl(Id("h"), [], FloatLiteral(1200000.0)), VarDecl(Id("t"), [], FloatLiteral(1200000.0)), VarDecl(
            Id("x"), [], BooleanLiteral(True)), VarDecl(Id("a"), [], BooleanLiteral(False)), VarDecl(Id("z"), [], StringLiteral("This is a string \\n \\n \\n \\n \\n \'\" ")), VarDecl(Id("k"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2)])), VarDecl(Id("m"), [], ArrayLiteral([ArrayLiteral([StringLiteral("A"), StringLiteral("a")]), StringLiteral("b")]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_28(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
              Var: x_ = 5 , z = "   ";
            EndBody.
            """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([
                         VarDecl(Id("x_"), [], IntLiteral(5)), VarDecl(Id("z"), [], StringLiteral("   "))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_29(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[5] = 1+2;
            EndBody.
             """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([], [
                         Assign(ArrayCell(Id("a"), [IntLiteral(5)]), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_30(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[5][1+2*3\\6%3*(1+2)] = 1;
            EndBody.
             """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([], [Assign(ArrayCell(Id("a"), [IntLiteral(5), BinaryOp("+", IntLiteral(1), BinaryOp(
            "*", BinaryOp("%", BinaryOp("\\", BinaryOp("*", IntLiteral(2), IntLiteral(3)), IntLiteral(6)), IntLiteral(3)), BinaryOp("+", IntLiteral(1), IntLiteral(2))))]), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_31(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[1+foo(2)] = 1+2;
            EndBody.
             """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([], [Assign(ArrayCell(
            Id("a"), [BinaryOp("+", IntLiteral(1), CallExpr(Id("foo"), [IntLiteral(2)]))]), BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_32(self):
        input = """
            Var: x, y = 5e3, z;
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = (x\\x\\x\\x\\x\\x\\x\\x\\x\\x) * (True || False) * (2.*.y + test___(2)- test());
                x = x -. 20.5;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], FloatLiteral(5000.0)), VarDecl(Id("z"), [], None), FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([], [Assign(Id("z"), BinaryOp("*", BinaryOp("*", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp("\\", BinaryOp(
            "\\", Id("x"), Id("x")), Id("x")), Id("x")), Id("x")), Id("x")), Id("x")), Id("x")), Id("x")), Id("x")), BinaryOp("||", BooleanLiteral(True), BooleanLiteral(False))), BinaryOp("-", BinaryOp("+", BinaryOp("*.", FloatLiteral(2.0), Id("y")), CallExpr(Id("test___"), [IntLiteral(2)])), CallExpr(Id("test"), [])))), Assign(Id("x"), BinaryOp("-.", Id("x"), FloatLiteral(20.5)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_33(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = !foo(2) && ( a|| b);
                y = z+a;
            EndBody.
            """
        expect = Program([FuncDecl(Id("test____"), [VarDecl(Id("x"), [1], None), VarDecl(Id("a"), [2], None)], ([], [Assign(Id("z"), BinaryOp(
            "&&", UnaryOp("!", CallExpr(Id("foo"), [IntLiteral(2)])), BinaryOp("||", Id("a"), Id("b")))), Assign(Id("y"), BinaryOp("+", Id("z"), Id("a")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_34(self):
        input = """
            Function: test
            Body:
                Var: x;
                If (1) Then x= x+3;
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("x"), [], None)], [If(
            [(IntLiteral(1), [], [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(3)))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_35(self):
        input = """
            Function: test
            Body:
                If ( i < 200) Then  x = y+1;
                ElseIf i >= 200 Then x =y;
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [If([(BinaryOp("<", Id("i"), IntLiteral(200)), [], [Assign(Id("x"), BinaryOp(
            "+", Id("y"), IntLiteral(1)))]), (BinaryOp(">=", Id("i"), IntLiteral(200)), [], [Assign(Id("x"), Id("y"))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_36(self):
        input = """
            Function: test
            Body:
                If i<1 Then i =1;
                ElseIf i<2 Then i=2;
                ElseIf i<3 Then i=3;
                ElseIf i<4 Then i=4;
                Else i=5;
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [If([(BinaryOp("<", Id("i"), IntLiteral(1)), [], [Assign(Id("i"), IntLiteral(1))]), (BinaryOp("<", Id("i"), IntLiteral(2)), [], [Assign(Id("i"), IntLiteral(
            2))]), (BinaryOp("<", Id("i"), IntLiteral(3)), [], [Assign(Id("i"), IntLiteral(3))]), (BinaryOp("<", Id("i"), IntLiteral(4)), [], [Assign(Id("i"), IntLiteral(4))])], ([], [Assign(Id("i"), IntLiteral(5))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_37(self):
        input = """
            Function: test
            Body:
                Var: diemthi = 3;
                If (diemthi == 0)  Then print("Hoc lai");
                ElseIf(diemthi != 0) Then
                    If (diemthi == 3) Then print("Hen");
                    ElseIf (diemthi == 5) Then print("Hoc gioi");
                    Else print("Adu vjp");
                    EndIf.
                Else print("Diem 13");
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("diemthi"), [], IntLiteral(3))], [If([(BinaryOp("==", Id("diemthi"), IntLiteral(0)), [], [CallStmt(Id("print"), [StringLiteral("Hoc lai")])]), (BinaryOp("!=", Id("diemthi"), IntLiteral(0)), [], [If([(BinaryOp("==", Id("diemthi"), IntLiteral(
            3)), [], [CallStmt(Id("print"), [StringLiteral("Hen")])]), (BinaryOp("==", Id("diemthi"), IntLiteral(5)), [], [CallStmt(Id("print"), [StringLiteral("Hoc gioi")])])], ([], [CallStmt(Id("print"), [StringLiteral("Adu vjp")])]))])], ([], [CallStmt(Id("print"), [StringLiteral("Diem 13")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_38(self):
        input = """
            Function: test
            Body:
                If (false == True) Then
                    If (true == False) Then print("true = false");
                    Else
                        If writeLn("false = true") Then Continue;
                        ElseIf i<1 Then a =1 ;
                        EndIf.
                    EndIf.
                Else print("nope");
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [If([(BinaryOp("==", Id("false"), BooleanLiteral(True)), [], [If([(BinaryOp("==", Id("true"), BooleanLiteral(False)), [], [CallStmt(Id("print"), [StringLiteral("true = false")])])], ([], [
                         If([(CallExpr(Id("writeLn"), [StringLiteral("false = true")]), [], [Continue()]), (BinaryOp("<", Id("i"), IntLiteral(1)), [], [Assign(Id("a"), IntLiteral(1))])], ([], []))]))])], ([], [CallStmt(Id("print"), [StringLiteral("nope")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_39(self):
        input = """
            Function: test
            Body:
                Var: abc = 1, cde = 2, efg = 3;
                If abc + cde == efg Then Else efg = 3;
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("abc"), [], IntLiteral(1)), VarDecl(Id("cde"), [], IntLiteral(2)), VarDecl(Id("efg"), [
        ], IntLiteral(3))], [If([(BinaryOp("==", BinaryOp("+", Id("abc"), Id("cde")), Id("efg")), [], [])], ([], [Assign(Id("efg"), IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_40(self):
        input = """
            Function: test
            Body:
                Var: i = 20, a, b, c;
                If i == 10 Then
                    a = 1;
                    b = 2;
                    c = a + b;
                ElseIf i == 15 Then
                    a = 3;
                    b = 4;
                    c = b - a;
                ElseIf i == 20 Then
                    a = 2;
                    b = 2;
                    c = a*2 + b*3;
                EndIf.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("i"), [], IntLiteral(20)), VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None)], [If([(BinaryOp("==", Id("i"), IntLiteral(10)), [], [Assign(Id("a"), IntLiteral(1)), Assign(Id("b"), IntLiteral(2)), Assign(Id("c"), BinaryOp("+", Id("a"), Id("b")))]), (BinaryOp("==", Id("i"), IntLiteral(
            15)), [], [Assign(Id("a"), IntLiteral(3)), Assign(Id("b"), IntLiteral(4)), Assign(Id("c"), BinaryOp("-", Id("b"), Id("a")))]), (BinaryOp("==", Id("i"), IntLiteral(20)), [], [Assign(Id("a"), IntLiteral(2)), Assign(Id("b"), IntLiteral(2)), Assign(Id("c"), BinaryOp("+", BinaryOp("*", Id("a"), IntLiteral(2)), BinaryOp("*", Id("b"), IntLiteral(3))))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_41(self):
        input = """
                    Function: main
                    Body:
                        If True Then Return;
                        ElseIf True Then
                            If True Then
                                If False Then
                                    If False Then
                                    Else
                                    EndIf.
                                EndIf.
                            EndIf.
                        EndIf.
                EndBody.
    """
        expect = Program([FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [Return(None)]), (BooleanLiteral(True), [], [If([(BooleanLiteral(
            True), [], [If([(BooleanLiteral(False), [], [If([(BooleanLiteral(False), [], [])], ([], []))])], ([], []))])], ([], []))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_42(self):
        input = """
            Function: test
            Body:
                For (i = 0, i < 100, i+1) Do
                    print("i");
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(
            100)), BinaryOp("+", Id("i"), IntLiteral(1)), ([], [CallStmt(Id("print"), [StringLiteral("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_43(self):
        input = """
            Function: test
            Parameter: n
            Body:
                Var: x;
                For (i = 0, i < sqrt(n)*2, 1) Do
                    x = i+n;
                    x[1][2] = 1*2 \\. foo(1,2,3,4);
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("x"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), BinaryOp("*", CallExpr(Id("sqrt"), [Id("n")]), IntLiteral(2))), IntLiteral(1), ([], [Assign(
            Id("x"), BinaryOp("+", Id("i"), Id("n"))), Assign(ArrayCell(Id("x"), [IntLiteral(1), IntLiteral(2)]), BinaryOp("\.", BinaryOp("*", IntLiteral(1), IntLiteral(2)), CallExpr(Id("foo"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_44(self):
        input = """
            Function: test
            Body:
                For (i = 0.5, i <= 1000, 1) Do
                    If i%2 == 0 Then writeln(i\\2);
                    EndIf.
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [For(Id("i"), FloatLiteral(0.5), BinaryOp("<=", Id("i"), IntLiteral(1000)), IntLiteral(1), ([], [If(
            [(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [CallStmt(Id("writeln"), [BinaryOp("\\", Id("i"), IntLiteral(2))])])], ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_45(self):
        input = """
            Function: test
            Body:
                For (i = 0, i < 10, 1) Do
                    For (j = 0, j < 10, 1) Do
                        For (k = 0, k<10 , 1) Do
                        arr[i][j] = 0;
                        If (i<0) Then Continue;
                        EndIf.
                        Break;
                        EndFor.
                    EndFor.
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), ([], [For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), IntLiteral(10)), IntLiteral(1), ([], [For(
            Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(10)), IntLiteral(1), ([], [Assign(ArrayCell(Id("arr"), [Id("i"), Id("j")]), IntLiteral(0)), If([(BinaryOp("<", Id("i"), IntLiteral(0)), [], [Continue()])], ([], [])), Break()]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_46(self):
        input = """
            Function: test
            Body:
                For (i = 0, True, False) Do
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [For(Id("i"), IntLiteral(
            0), BooleanLiteral(True), BooleanLiteral(False), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_47(self):
        input = """
            Function: test
            Body:
                Var: a = 2;
                For (i = 10 - foo(2), a < 100, a + 1) Do
                    i = i + 1;
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("a"), [], IntLiteral(2))], [For(Id("i"), BinaryOp("-", IntLiteral(10), CallExpr(Id("foo"), [IntLiteral(2)])),
                                                                                                BinaryOp("<", Id("a"), IntLiteral(100)), BinaryOp("+", Id("a"), IntLiteral(1)), ([], [Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_48(self):
        input = """
            Function: test_____
            Body:
                While False Do
                EndWhile.
            EndBody.
            """
        expect = Program(
            [FuncDecl(Id("test_____"), [], ([], [While(BooleanLiteral(False), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_49(self):
        input = """
            Function: test
            Parameter: t
            Body:
                While t < 10 Do
                    While t<5 Do
                    EndWhile.
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("t"), [], None)], ([], [While(BinaryOp(
            "<", Id("t"), IntLiteral(10)), ([], [While(BinaryOp("<", Id("t"), IntLiteral(5)), ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_50(self):
        input = """
            Function: test
            Body:
                Var: x=1;
                While (x<10) Do
                    Var: x=2;
                    While (x<20) Do
                    EndWhile.
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("x"), [], IntLiteral(1))], [While(BinaryOp("<", Id("x"), IntLiteral(
            10)), ([VarDecl(Id("x"), [], IntLiteral(2))], [While(BinaryOp("<", Id("x"), IntLiteral(20)), ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_51(self):
        input = """
            Function: test
            Body:
                Var: x= False;
                While (!x && (1+2)*3\\5 || True || False || !x) Do
                   Var: x = False;
                   If (i<1) Then
                   EndIf.
                   While (i<5) Do
                   EndWhile.
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("x"), [], BooleanLiteral(False))], [While(BinaryOp("||", BinaryOp("||", BinaryOp("||", BinaryOp("&&", UnaryOp("!", Id("x")), BinaryOp("\\", BinaryOp("*", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3)),
                                                                                                                                                                                                      IntLiteral(5))), BooleanLiteral(True)), BooleanLiteral(False)), UnaryOp("!", Id("x"))), ([VarDecl(Id("x"), [], BooleanLiteral(False))], [If([(BinaryOp("<", Id("i"), IntLiteral(1)), [], [])], ([], [])), While(BinaryOp("<", Id("i"), IntLiteral(5)), ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_52(self):
        input = """
            Function: test
            Parameter: m, n, o, p
            Body:
                Var: x;
                While (m <= 2) Do
                    While (n >= 1) Do
                        While (o <= n) Do
                            o = o - 1;
                            While (p <= 2) Do
                                p = p + 1;
                            EndWhile.
                        EndWhile.
                        x = True;
                        n = n - 1;
                    EndWhile.
                    x = m * n * p * o;
                    m = m + 1;
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("m"), [], None), VarDecl(Id("n"), [], None), VarDecl(Id("o"), [], None), VarDecl(Id("p"), [], None)], ([VarDecl(Id("x"), [], None)], [While(BinaryOp("<=", Id("m"), IntLiteral(2)), ([], [While(BinaryOp(">=", Id("n"), IntLiteral(1)), ([], [While(BinaryOp("<=", Id("o"), Id("n")), ([], [Assign(Id("o"), BinaryOp("-", Id("o"), IntLiteral(1))),
                                                                                                                                                                                                                                                                                                                                                       While(BinaryOp("<=", Id("p"), IntLiteral(2)), ([], [Assign(Id("p"), BinaryOp("+", Id("p"), IntLiteral(1)))]))])), Assign(Id("x"), BooleanLiteral(True)), Assign(Id("n"), BinaryOp("-", Id("n"), IntLiteral(1)))])), Assign(Id("x"), BinaryOp("*", BinaryOp("*", BinaryOp("*", Id("m"), Id("n")), Id("p")), Id("o"))), Assign(Id("m"), BinaryOp("+", Id("m"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_53(self):
        input = """
            ** Phao of N **
            Function: lcd **LCD of n**
            Parameter: n
            Body:
                While (n % i != 0) Do  ** Hello **
                    i = i - 1;
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("lcd"), [VarDecl(Id("n"), [], None)], ([], [While(BinaryOp("!=", BinaryOp(
            "%", Id("n"), Id("i")), IntLiteral(0)), ([], [Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_54(self):
        input = """
            Function: sNum **square number**
            Parameter: n
            Body:
                Var: i = 0;
                While (i*i <= n) Do
                    If (i*i == n) Then
                        Return;
                        Continue;
                        Break;
                        While 5 Do
                            Break;
                        EndWhile.
                    EndIf.
                EndWhile.
            EndBody.
            """
        expect = Program([FuncDecl(Id("sNum"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("i"), [], IntLiteral(0))], [While(BinaryOp("<=", BinaryOp("*", Id("i"), Id("i")), Id("n")),
                                                                                                                            ([], [If([(BinaryOp("==", BinaryOp("*", Id("i"), Id("i")), Id("n")), [], [Return(None), Continue(), Break(), While(IntLiteral(5), ([], [Break()]))])], ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_55(self):
        input = """
            Function: test
            Body:
                Var: i = 0;
                Do  ** Hello **
                    print("Hello");
                    i = i + 1;
                While (i < 10) EndDo.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("i"), [], IntLiteral(0))], [Dowhile(([], [CallStmt(Id("print"), [
                         StringLiteral("Hello")]), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]), BinaryOp("<", Id("i"), IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_56(self):
        input = """
            Function: test **1 + 2 + ... n < max**
            Parameter: max
            Body:
                Var: n = 0, s = 0;
                Do
                    n = n + 1;
                    s = s + n;
                While (s + n + 1 < max) EndDo.
                writeln(n);
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("max"), [], None)], ([VarDecl(Id("n"), [], IntLiteral(0)), VarDecl(Id("s"), [], IntLiteral(0))], [Dowhile(([], [Assign(Id("n"), BinaryOp(
            "+", Id("n"), IntLiteral(1))), Assign(Id("s"), BinaryOp("+", Id("s"), Id("n")))]), BinaryOp("<", BinaryOp("+", BinaryOp("+", Id("s"), Id("n")), IntLiteral(1)), Id("max"))), CallStmt(Id("writeln"), [Id("n")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_57(self):
        input = """
            Function: test
            Parameter: n
            Body:
                Var: flag = 0;
                Do
                While i<=1 EndDo.
                print(i);
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("flag"), [], IntLiteral(0))], [
                         Dowhile(([], []), BinaryOp("<=", Id("i"), IntLiteral(1))), CallStmt(Id("print"), [Id("i")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_58(self):
        input = """
            Function: test
            Body:
                Var: flag = 0;
                Do
                    While !flag Do
                        While !flag Do
                        Do
                        While flag EndDo.
                        EndWhile.
                    EndWhile.
                While flag EndDo.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("flag"), [], IntLiteral(0))], [Dowhile(([], [While(UnaryOp(
            "!", Id("flag")), ([], [While(UnaryOp("!", Id("flag")), ([], [Dowhile(([], []), Id("flag"))]))]))]), Id("flag"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_59(self):
        input = """
            Function: test
            Body:
                Do
                    Do
                        Do
                        While (True) EndDo.
                            Do
                            While (True) EndDo.
                        Do
                            Do
                            While (True) EndDo.
                        While (True) EndDo.
                        Do
                        While (True) EndDo.
                    While (True) EndDo.
                While (True) EndDo.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [Dowhile(([], [Dowhile(([], [Dowhile(([], []), BooleanLiteral(True)), Dowhile(([], []), BooleanLiteral(True)), Dowhile(
            ([], [Dowhile(([], []), BooleanLiteral(True))]), BooleanLiteral(True)), Dowhile(([], []), BooleanLiteral(True))]), BooleanLiteral(True))]), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_60(self):
        input = """
        Function: memory
        Body:   
            For (i = 0, i < 10, 2) Do
                Break;
            EndFor.
            writeln(i);
            If True Then
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("memory"), [], ([], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(
            2), ([], [Break()])), CallStmt(Id("writeln"), [Id("i")]), If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_61(self):
        input = """
        Function: testing
        Body:
            While i < 10 Do
                Break;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("testing"), [], ([], [While(
            BinaryOp("<", Id("i"), IntLiteral(10)), ([], [Break(), Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_62(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            Do
                a[1][2] = 1;
                Continue;
            While !x EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("x"), [], IntLiteral(1))], [Dowhile(([], [Assign(
            ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), IntLiteral(1)), Continue()]), UnaryOp("!", Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_63(self):
        input = """
        Function: test
        Body:
            While !x Do
                Continue;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(
            Id("test"), [], ([], [While(UnaryOp("!", Id("x")), ([], [Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_64(self):
        input = """
        Function: test
        Body:
            foo (1+2+3+4,2345);
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([], [CallStmt(Id("foo"), [BinaryOp("+", BinaryOp("+", BinaryOp("+", IntLiteral(1), IntLiteral(2)),
                                                                                                     IntLiteral(3)), IntLiteral(4)), IntLiteral(2345)])])), FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_65(self):
        input = """
        Function: test
        Body:
            foo(foo());
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id("test"), [], ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_66(self):
        input = """
        Function: test
        Body:
            foo("@#@!#R#$@", {1} , 1.5 \\ 5.e2);
            foo(3,2,1);
            foo();
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([], [CallStmt(Id("foo"), [StringLiteral("@#@!#R#$@"), ArrayLiteral([IntLiteral(1)]), BinaryOp(
            "\\", FloatLiteral(1.5), FloatLiteral(500.0))]), CallStmt(Id("foo"), [IntLiteral(3), IntLiteral(2), IntLiteral(1)]), CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_67(self):
        input = """
        Function: test
        Body:
            Return ;
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_68(self):
        input = """
        Function: test
        Body:
            Return ("hello there");
        EndBody.
        """
        expect = Program(
            [FuncDecl(Id("test"), [], ([], [Return(StringLiteral("hello there"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_69(self):
        input = """
        Function: test
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return superman();
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("n"), [], None)], ([], [If([(BinaryOp("==", Id(
            "n"), IntLiteral(0)), [], [Return(IntLiteral(0))])], ([], [])), Return(CallExpr(Id("superman"), []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_70(self):
        input = """
                Function: test
                Body:
                    foo(3+y(5+z(4)));
                    If !foo Then
                        Return False;
                    EndIf.
                    For (i = 0, i < 100, 2) Do
                        writeln(i * test[1+2][foo(4)]);
                    EndFor.
                EndBody.
            """
        expect = Program([FuncDecl(Id("test"), [], ([], [CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(3), CallExpr(Id("y"), [BinaryOp("+", IntLiteral(5), CallExpr(Id("z"), [IntLiteral(4)]))]))]), If([(UnaryOp("!", Id("foo")), [], [Return(BooleanLiteral(False))])], ([], [])),
                                                         For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(2), ([], [CallStmt(Id("writeln"), [BinaryOp("*", Id("i"), ArrayCell(Id("test"), [BinaryOp("+", IntLiteral(1), IntLiteral(2)), CallExpr(Id("foo"), [IntLiteral(4)])]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_71(self):
        input = """
                Var: a, b[1], c[1][1], d = 1, e = 1e1, f = "Hello", g = True, i = {{1,2}};
                Function: main
                    Body:
                        While a < 10 Do
                            While b < 10 Do
                                prod = prod * b;
                            EndWhile.
                        EndWhile.
                        Return;
                    EndBody.
                """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [1], None), VarDecl(Id("c"), [1, 1], None), VarDecl(Id("d"), [], IntLiteral(1)), VarDecl(Id("e"), [], FloatLiteral(10.0)), VarDecl(Id("f"), [], StringLiteral("Hello")), VarDecl(Id("g"), [], BooleanLiteral(True)), VarDecl(
            Id("i"), [], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)])])), FuncDecl(Id("main"), [], ([], [While(BinaryOp("<", Id("a"), IntLiteral(10)), ([], [While(BinaryOp("<", Id("b"), IntLiteral(10)), ([], [Assign(Id("prod"), BinaryOp("*", Id("prod"), Id("b")))]))])), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_72(self):
        input = """
            Var: a = "Vu Nguyen Minh Dat";
            Function: check
            Parameter: b
            Body:
            EndBody.
            Function: main
            Body:
                Var: s, k, result;
                input(s);
                input(k);
                result = string(s) + string(k);
                If check(result) Then
                    writeln(result);
                Else
                    writeln("Nothing");
                EndIf.
            EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], StringLiteral("Vu Nguyen Minh Dat")), FuncDecl(Id("check"), [VarDecl(Id("b"), [], None)], ([], [])), FuncDecl(Id("main"), [], ([VarDecl(Id("s"), [], None), VarDecl(Id("k"), [], None), VarDecl(Id("result"), [], None)], [CallStmt(Id("input"), [Id("s")]), CallStmt(
            Id("input"), [Id("k")]), Assign(Id("result"), BinaryOp("+", CallExpr(Id("string"), [Id("s")]), CallExpr(Id("string"), [Id("k")]))), If([(CallExpr(Id("check"), [Id("result")]), [], [CallStmt(Id("writeln"), [Id("result")])])], ([], [CallStmt(Id("writeln"), [StringLiteral("Nothing")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_73(self):
        input = """
                Function: geiiiiiiiiiii
                Parameter: n
                Body:
                    If n < 2 Then
                        Return False;
                    EndIf.
                    If (n == 2) || (n == 3) Then
                        Return True;
                    EndIf.
                    For (i = 2, i < n, 1) Do
                        If (n % i == 0) Then
                            Return False;
                        EndIf.
                    EndFor.
                    Return True;
                EndBody.
                Function: main
                Body:
                    Var: a[100];
                    For (i = 0, i < 100, 1) Do
                    EndFor.
                EndBody.
            """
        expect = Program([FuncDecl(Id("geiiiiiiiiiii"), [VarDecl(Id("n"), [], None)], ([], [If([(BinaryOp("<", Id("n"), IntLiteral(2)), [], [Return(BooleanLiteral(False))])], ([], [])), If([(BinaryOp("||", BinaryOp("==", Id("n"), IntLiteral(2)), BinaryOp("==", Id("n"), IntLiteral(3))), [], [Return(BooleanLiteral(True))])], ([], [])), For(Id("i"), IntLiteral(2), BinaryOp(
            "<", Id("i"), Id("n")), IntLiteral(1), ([], [If([(BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), IntLiteral(0)), [], [Return(BooleanLiteral(False))])], ([], []))])), Return(BooleanLiteral(True))])), FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [100], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_74(self):
        input = """
                Var: m, n[10];
                Function: test___
                Parameter: n, a[1][2][3]
                Body:
                    Var: a[12][12] = {1,2};
                    If n == 0 Then
                        a[foo(2)*4+1] = 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
                Function: main
                Body:
                ** This is a single-line comment. **
                ** This is a
                * multi-line
                * comment.
                **
                    Var: r = 10., v;
                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                    If True Then
                        a = int_of_string (read ());
                        b = float_of_int (a) +. 2.0;
                    EndIf.
                    For (i = 0, i < 10, 2) Do
                        writeln(i);
                    EndFor.
                    fact (x);
                EndBody.
            """
        expect = Program([VarDecl(Id("m"), [], None), VarDecl(Id("n"), [10], None), FuncDecl(Id("test___"), [VarDecl(Id("n"), [], None), VarDecl(Id("a"), [1, 2, 3], None)], ([VarDecl(Id("a"), [12, 12], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))], [If([(BinaryOp("==", Id("n"), IntLiteral(0)), [], [Assign(ArrayCell(Id("a"), [BinaryOp("+", BinaryOp("*", CallExpr(Id("foo"), [IntLiteral(2)]), IntLiteral(4)), IntLiteral(1))]), IntLiteral(1))])], ([], [Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]))])), FuncDecl(Id("main"), [], ([VarDecl(Id("r"), [], FloatLiteral(
            10.0)), VarDecl(Id("v"), [], None)], [Assign(Id("v"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("\.", FloatLiteral(4.0), FloatLiteral(3.0)), FloatLiteral(3.14)), Id("r")), Id("r")), Id("r"))), If([(BooleanLiteral(True), [], [Assign(Id("a"), CallExpr(Id("int_of_string"), [CallExpr(Id("read"), [])])), Assign(Id("b"), BinaryOp("+.", CallExpr(Id("float_of_int"), [Id("a")]), FloatLiteral(2.0)))])], ([], [])), For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id("writeln"), [Id("i")])])), CallStmt(Id("fact"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_75(self):
        input = """
                    Function: main
                        Body:
                            Var: x =5;
                            If True Then  
                                Do 
                                    While True Do
                                        For (i = 0, i<10 , 1) Do
                                        EndFor.
                                    EndWhile.
                                While (True) 
                                EndDo.
                            EndIf.
                            a = { 1, 2, 3, 4 };
                            a = { 1.0, 2.0, 3.0, 4.0 };
                            a = { True, False };
                            a = { {1,2}, {3,4} };
                            a = {{{{{1}}}}};
                            a = {{{{{1}}}}, {1}, 1};
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(5))], [If([(BooleanLiteral(True), [], [Dowhile(([], [While(BooleanLiteral(True), ([], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(1), ([], []))]))]), BooleanLiteral(True))])], ([], [])), Assign(Id("a"), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])), Assign(Id("a"), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0), FloatLiteral(
            4.0)])), Assign(Id("a"), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])), Assign(Id("a"), ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])])), Assign(Id("a"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])])), Assign(Id("a"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])]), ArrayLiteral([IntLiteral(1)]), IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_76(self):
        input = """
Var: a, b = "abc";
Function: test
    Body:
        While a Do
            Var: c = {{{1}}};
            Do
                Var: c = {{1}, {2}};
                For (i = 10, i < 10, --i)
                Do
                    Var: a = 0, b;
                    If c Then
                        Var: a, b;
                        foo();
                    ElseIf d Then
                        Var: a, b;
                        a = foo()[foo(foo())];
                    Else
                        Var: a, b;
                        Var: c;
                        While abcd Do
                            Var: a, b = 2;
                            Var: a[1][2] = {1, 2};
                            Break;
                        EndWhile.
                        Return;
                    EndIf.
                EndFor.
                Continue;
            While b
            EndDo.
            Return 1;
        EndWhile.
        Return 0;
    EndBody.
"""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],StringLiteral("abc")),FuncDecl(Id("test"),[],([],[While(Id("a"),([VarDecl(Id("c"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))],[Dowhile(([VarDecl(Id("c"),[],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))],[For(Id("i"),IntLiteral(10),BinaryOp("<",Id("i"),IntLiteral(10)),UnaryOp("-",UnaryOp("-",Id("i"))),([VarDecl(Id("a"),[],IntLiteral(0)),VarDecl(Id("b"),[],None)],[If([(Id("c"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],[CallStmt(Id("foo"),[])]),(Id("d"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],[Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])]))])],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],[While(Id("abcd"),([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("a"),[1,2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[Break()])),Return(None)]))])),Continue()]),Id("b")),Return(IntLiteral(1))])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_77(self):
        input = """
                    Function: main
                        Body:
                            a = b;
                            a = fyes();
                            a = fyes(1,True);
                            a = f[1];
                            a = fyes()[1];
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("b")), Assign(Id("a"), CallExpr(Id("fyes"), [])), Assign(Id("a"), CallExpr(Id("fyes"), [IntLiteral(
            1), BooleanLiteral(True)])), Assign(Id("a"), ArrayCell(Id("f"), [IntLiteral(1)])), Assign(Id("a"), ArrayCell(CallExpr(Id("fyes"), []), [IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_78(self):
        input = """
        Function: memory
            Body:
                Var: answer, length, jump_max, arr[10], a , j;
                For (i = 0, i < length, 1) Do
                    arr[i] = input();
                EndFor.
                For (j = 0, j < length, 1) Do
                    If (a + jump_max >= arr[i]) && (a + jump_max < arr[i + 1]) Then
                        a = arr[i];
                        answer = answer + 1;
                    EndIf.
                EndFor.
                If (j != length - 1) Then
                    answer = -1;
                EndIf.
                If (a + jump_max >= arr[length - 1]) Then
                    answer = answer + 1;
                Else answer = -1;
                EndIf.
	            writeln(answer);
            EndBody.
        """
        expect = Program([FuncDecl(Id("memory"), [], ([VarDecl(Id("answer"), [], None), VarDecl(Id("length"), [], None), VarDecl(Id("jump_max"), [], None), VarDecl(Id("arr"), [10], None), VarDecl(Id("a"), [], None), VarDecl(Id("j"), [], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("length")), IntLiteral(1), ([], [Assign(ArrayCell(Id("arr"), [Id("i")]), CallExpr(Id("input"), []))])), For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("length")), IntLiteral(1), ([], [If([(BinaryOp("&&", BinaryOp(">=", BinaryOp("+", Id("a"), Id("jump_max")), ArrayCell(Id("arr"), [Id("i")])), BinaryOp("<", BinaryOp("+", Id("a"), Id("jump_max")), ArrayCell(
            Id("arr"), [BinaryOp("+", Id("i"), IntLiteral(1))]))), [], [Assign(Id("a"), ArrayCell(Id("arr"), [Id("i")])), Assign(Id("answer"), BinaryOp("+", Id("answer"), IntLiteral(1)))])], ([], []))])), If([(BinaryOp("!=", Id("j"), BinaryOp("-", Id("length"), IntLiteral(1))), [], [Assign(Id("answer"), UnaryOp("-", IntLiteral(1)))])], ([], [])), If([(BinaryOp(">=", BinaryOp("+", Id("a"), Id("jump_max")), ArrayCell(Id("arr"), [BinaryOp("-", Id("length"), IntLiteral(1))])), [], [Assign(Id("answer"), BinaryOp("+", Id("answer"), IntLiteral(1)))])], ([], [Assign(Id("answer"), UnaryOp("-", IntLiteral(1)))])), CallStmt(Id("writeln"), [Id("answer")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_79(self):
        input = """
                Function: reheapUp
                Body:
                If !node == 0 Then
                    parent = (node - 1) \\. 2 ;  ** Division **
                    If heap[node] > heap[parent] Then
                        swap(heap[parent], heap[node]);
                        reheapUp(parent);
                    EndIf.
                EndIf.
                EndBody."""
        expect = Program([FuncDecl(Id("reheapUp"), [], ([], [If([(BinaryOp("==", UnaryOp("!", Id("node")), IntLiteral(0)), [], [Assign(Id("parent"), BinaryOp("\.", BinaryOp("-", Id("node"), IntLiteral(1)), IntLiteral(2))), If([(BinaryOp(">", ArrayCell(
            Id("heap"), [Id("node")]), ArrayCell(Id("heap"), [Id("parent")])), [], [CallStmt(Id("swap"), [ArrayCell(Id("heap"), [Id("parent")]), ArrayCell(Id("heap"), [Id("node")])]), CallStmt(Id("reheapUp"), [Id("parent")])])], ([], []))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_80(self):
        input = """
        Function: greatest_common_divisor
        Parameter: a, b
        Body:
                If (a == b) Then
                    Return a;
                EndIf.
	            If (a > b) Then
		            a = a % b;
                EndIf.
	            If (a == 0) Then
                    Return b;
                EndIf.
	            Return greatest_common_divisor(b, a);
        EndBody.
        """
        expect = Program([FuncDecl(Id("greatest_common_divisor"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([], [If([(BinaryOp("==", Id("a"), Id("b")), [], [Return(Id("a"))])], ([], [])), If([(BinaryOp(">", Id("a"), Id(
            "b")), [], [Assign(Id("a"), BinaryOp("%", Id("a"), Id("b")))])], ([], [])), If([(BinaryOp("==", Id("a"), IntLiteral(0)), [], [Return(Id("b"))])], ([], [])), Return(CallExpr(Id("greatest_common_divisor"), [Id("b"), Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_81(self):
        input = """
Function: test
    Body:
        x = (x) + (x) + (x) + (x);
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("x"), BinaryOp(
            "+", BinaryOp("+", BinaryOp("+", Id("x"), Id("x")), Id("x")), Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_82(self):
        input = """
Function: test
    Body:
        a[foo(1)+ {1,2}] = ((((((a))))));
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(ArrayCell(Id("a"), [BinaryOp(
            "+", CallExpr(Id("foo"), [IntLiteral(1)]), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))]), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_83(self):
        input = """
Function: test
    Body:
        a = test(test(test()));
        a = foo(1, True, "", 1.);
        a = test(test()+1,test({1,2}));
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("a"), CallExpr(Id("test"), [CallExpr(Id("test"), [CallExpr(Id("test"), [])])])), Assign(Id("a"), CallExpr(Id("foo"), [IntLiteral(1), BooleanLiteral(
            True), StringLiteral(""), FloatLiteral(1.0)])), Assign(Id("a"), CallExpr(Id("test"), [BinaryOp("+", CallExpr(Id("test"), []), IntLiteral(1)), CallExpr(Id("test"), [ArrayLiteral([IntLiteral(1), IntLiteral(2)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_84(self):
        input = """
Function: test
    Body:
        x = x[1][2*x];
        a = a[a][-1];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("x"), ArrayCell(Id("x"), [IntLiteral(1), BinaryOp(
            "*", IntLiteral(2), Id("x"))])), Assign(Id("a"), ArrayCell(Id("a"), [Id("a"), UnaryOp("-", IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_85(self):
        input = """
Function: test
    Body:
        a = foo()[1];
        a = foo(a[1])[-1];
        a = foo(1, True, 1., "abcd",False)[1][2][3][4];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(1)])), Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), [ArrayCell(Id("a"), [IntLiteral(1)])]), [UnaryOp("-", IntLiteral(1))])),
                                                         Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), [IntLiteral(1), BooleanLiteral(True), FloatLiteral(1.0), StringLiteral("abcd"), BooleanLiteral(False)]), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_86(self):
        input = """
Function: test
    Body:
        x = 3 * 4;
        x = 3 *. 4;
        x = 3 \ 4;
        x = a \. b;
        x = foo() % 2;
        x = 1 + 2;
        x = 5 +. 6;
        x = 1 - 2;
        x = 1 -. 2;
        x = 1 && 2;
        x = 1 || 2;
        x = 1 == 2;
        x = 1 != 2;
        x = 1 =/= 2;
        x = 1 < 2;
        x = 12 <. 23;
        x = 1 > 2;
        x = 11 >. 2;
        x = 1 <= 2;
        x = 123 <=. 2;
        x = 1 >= 2;
        x = 14 >=. 2;
        x = !1;
        x = -1;
        x = -.1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("x"), BinaryOp("*", IntLiteral(3), IntLiteral(4))), Assign(Id("x"), BinaryOp("*.", IntLiteral(3), IntLiteral(4))), Assign(Id("x"), BinaryOp("\\", IntLiteral(3), IntLiteral(4))), Assign(Id("x"), BinaryOp("\.", Id("a"), Id("b"))), Assign(Id("x"), BinaryOp("%", CallExpr(Id("foo"), []), IntLiteral(2))), Assign(Id("x"), BinaryOp("+", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("+.", IntLiteral(5), IntLiteral(6))), Assign(Id("x"), BinaryOp("-", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("-.", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("&&", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("||", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("==", IntLiteral(1), IntLiteral(2))),
                                                         Assign(Id("x"), BinaryOp("!=", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("=/=", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("<", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("<.", IntLiteral(12), IntLiteral(23))), Assign(Id("x"), BinaryOp(">", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp(">.", IntLiteral(11), IntLiteral(2))), Assign(Id("x"), BinaryOp("<=", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp("<=.", IntLiteral(123), IntLiteral(2))), Assign(Id("x"), BinaryOp(">=", IntLiteral(1), IntLiteral(2))), Assign(Id("x"), BinaryOp(">=.", IntLiteral(14), IntLiteral(2))), Assign(Id("x"), UnaryOp("!", IntLiteral(1))), Assign(Id("x"), UnaryOp("-", IntLiteral(1))), Assign(Id("x"), UnaryOp("-.", IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    """ Associative """

    def test_87(self):
        input = """
        Function: test
        Body:
            Var: arr[100][100][100];
            For (i = 0, i < 100, 1) Do  
                For (j = 0, j < 100, 1) Do
                    For (k =0,k < 100,1) Do
                    arr[i][j] = 0;
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([VarDecl(Id("arr"), [100, 100, 100], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1), ([], [For(Id("j"), IntLiteral(0), BinaryOp(
            "<", Id("j"), IntLiteral(100)), IntLiteral(1), ([], [For(Id("k"), IntLiteral(0), BinaryOp("<", Id("k"), IntLiteral(100)), IntLiteral(1), ([], [Assign(ArrayCell(Id("arr"), [Id("i"), Id("j")]), IntLiteral(0))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_88(self):
        input = """
        Function: test
        Parameter: w
        Body:
            Var: x;
            While (m <= 2) Do
                While (n >= 1) Do
                    While (o <= n) Do
                        o = o - 1;
                    EndWhile.
                    x = True;
                    n = n - 1;
                EndWhile.
                x = m * n * p * o;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [VarDecl(Id("w"), [], None)], ([VarDecl(Id("x"), [], None)], [While(BinaryOp("<=", Id("m"), IntLiteral(2)), ([], [While(BinaryOp(">=", Id("n"), IntLiteral(1)), ([], [While(BinaryOp("<=", Id("o"), Id("n")), ([], [Assign(
            Id("o"), BinaryOp("-", Id("o"), IntLiteral(1)))])), Assign(Id("x"), BooleanLiteral(True)), Assign(Id("n"), BinaryOp("-", Id("n"), IntLiteral(1)))])), Assign(Id("x"), BinaryOp("*", BinaryOp("*", BinaryOp("*", Id("m"), Id("n")), Id("p")), Id("o")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_89(self):
        input = """
Function: test
    Body:
        a = a || b == c && d +. !x;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("a"), BinaryOp("==", BinaryOp("||", Id(
            "a"), Id("b")), BinaryOp("&&", Id("c"), BinaryOp("+.", Id("d"), UnaryOp("!", Id("x"))))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_90(self):
        input = """
Function: test
    Body:
        a[1][2][3][4][foo()+abc* "str"] = a + b || c - d;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), BinaryOp(
            "+", CallExpr(Id("foo"), []), BinaryOp("*", Id("abc"), StringLiteral("str")))]), BinaryOp("||", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_91(self):
        input = """
Function: test
    Body:
        a = a[1] * b + 1.05 % d;
        If 1 Then
        ElseIf True Then
        ElseIf False Then
        ElseIf (1+1) Then
        Else 
            x = 2;
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("a"), BinaryOp("+", BinaryOp("*", ArrayCell(Id("a"), [IntLiteral(1)]), Id("b")), BinaryOp("%", FloatLiteral(1.05), Id("d")))), If(
            [(IntLiteral(1), [], []), (BooleanLiteral(True), [], []), (BooleanLiteral(False), [], []), (BinaryOp("+", IntLiteral(1), IntLiteral(1)), [], [])], ([], [Assign(Id("x"), IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_92(self):
        input = """
Function: test
    Body:
        x = ! x * y;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(
            Id("x"), BinaryOp("*", UnaryOp("!", Id("x")), Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_93(self):
        input = """
Function: test
    Body:
        a = -a[b];
        If True Then
            Var: a[1][2][3][4][5];
            Var: x[1];
            Var: y[2];
            x = 1+1;
            y = 2*1;
            z = 3+3+3+3+3;
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("a"), UnaryOp("-", ArrayCell(Id("a"), [Id("b")]))), If([(BooleanLiteral(True), [VarDecl(Id("a"), [1, 2, 3, 4, 5], None), VarDecl(Id("x"), [1], None), VarDecl(Id("y"), [2], None)], [Assign(Id("x"), BinaryOp(
            "+", IntLiteral(1), IntLiteral(1))), Assign(Id("y"), BinaryOp("*", IntLiteral(2), IntLiteral(1))), Assign(Id("z"), BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", IntLiteral(3), IntLiteral(3)), IntLiteral(3)), IntLiteral(3)), IntLiteral(3)))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_94(self):
        input = """
Function: test
    Body:
        x = !x[y];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(
            Id("x"), UnaryOp("!", ArrayCell(Id("x"), [Id("y")])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_95(self):
        input = """
Function: test
    Body:
        x = x * s [c];
        Break;
        Return x+1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"), [], ([], [Assign(Id("x"), BinaryOp(
            "*", Id("x"), ArrayCell(Id("s"), [Id("c")]))), Break(), Return(BinaryOp("+", Id("x"), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_96(self):
        input = """
Function: main
    Body:
        a = (a < b) && (d >= d);
        Break;
        Return a;
        Continue;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("&&", BinaryOp("<", Id(
            "a"), Id("b")), BinaryOp(">=", Id("d"), Id("d")))), Break(), Return(Id("a")), Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_97(self):
        input = """
Function: main
    Body:
        a = !(a + b);
        Return a+b;
        Return 1;
        Return True;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), UnaryOp("!", BinaryOp("+", Id("a"), Id("b")))),
                                                         Return(BinaryOp("+", Id("a"), Id("b"))), Return(IntLiteral(1)), Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_98(self):
        input = """
Function: main
    Body:
        a = 1+-1;
        zed = "Weak";
        If True Then
        zed = "Strong";
        Else
        zed = "Weak";
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1)))), Assign(Id("zed"), StringLiteral(
            "Weak")), If([(BooleanLiteral(True), [], [Assign(Id("zed"), StringLiteral("Strong"))])], ([], [Assign(Id("zed"), StringLiteral("Weak"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_99(self):
        input = """
Function: main
    Body:
        a = a--b--c--d+-e;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("+", BinaryOp("-", BinaryOp("-", BinaryOp(
            "-", Id("a"), UnaryOp("-", Id("b"))), UnaryOp("-", Id("c"))), UnaryOp("-", Id("d"))), UnaryOp("-", Id("e"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_100(self):
        input = """
Function: main
    Body:
        a = !a[1] > b || c + foo() * -e[2][abcd] % foo(1)[1] \ True;
        Do
            a = a +1;
        While 1
        EndDo.
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp(">", UnaryOp("!", ArrayCell(Id("a"), [IntLiteral(1)])), BinaryOp("||", Id("b"), BinaryOp("+", Id("c"), BinaryOp("\\", BinaryOp("%", BinaryOp("*", CallExpr(Id("foo"), []), UnaryOp(
            "-", ArrayCell(Id("e"), [IntLiteral(2), Id("abcd")]))), ArrayCell(CallExpr(Id("foo"), [IntLiteral(1)]), [IntLiteral(1)])), BooleanLiteral(True)))))), Dowhile(([], [Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
