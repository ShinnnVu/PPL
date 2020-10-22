import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_var_declare_1(self):
        """Simple program: int main() {} """
        input = """Var: b[1] = {{1,2,3},{4,5,6},{}};
                        Var: x;
                        Var: x[1][2][3][4][5];
                        Var: m,n[10];
                        Var: a, b = 1, c, d,e ={1};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_var_declare_2(self):
        input = """Var: x, w = ;"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_var_declare_3(self):
        input = """Var   :   x,b="bla bla" ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_var_declare_4(self):
        input = """Var: x="This is John:'"Where you?'"";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_var_declare_5(self):
        input = """Var: x= {{1} ; """
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_var_declare_6(self):
        input = """Var: x[1] = {{"ga","@#@#!@"}, {1,2,3}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var_declare_7(self):
        """Miss variable"""
        input = """Var: x[];"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_var_declare_8(self):
        input = """Var: x = " '"this is a string'". ", y =0X1234, z = 0O1234 , a= 123 , b= 12.e-5; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_declare_9(self):
        input = """Var: x[1+2];"""
        expect = "Error on line 1 col 8: +"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_var_declare_10(self):
        input = """Var: x[1][2][3][4][5 = 5;"""
        expect = "Error on line 1 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_var_declare_11(self):
        input = """Var: x = {{{1}}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_var_declare_12(self):
        input = """ Var: x[3][5] = 4, x[] = 2;"""
        expect = "Error on line 1 col 21: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_var_declare_13(self):
        input = """ Var: x[1][2][3][4] = {{{"abc","\\r\\n"},"abc"},1234};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_function_declare_1(self):
        input = """
            Function: function
            Parameter: a,b,c,d, e[10], f[1][2][3][4]
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_function_declare_2(self):
        input = """
            Function: test
            Body:
                Var: arr[2][3] = {{"Hi","Hello"},"Bai","Bye",{}};
                a= 10e2;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_function_declare_3(self):
        input = """
            Function: boo
            Body:
                Var: x, b =5 , c[1][2][3] = {{1,2},{3,4},{5,6}};
                a =  1 \\ 2 \\ 3 \\ 4 \\ 5 \\6 \\.7;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_function_declare_4(self):
        input = """
            Function:
            Body:
            a = b;
            EndBody.
            """
        expect = "Error on line 3 col 12: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_function_declare_5(self):
        input = """
            Function: empty
            Body:
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_function_declare_6(self):
        input = """
                Function: empty
                Body:
                """
        expect = "Error on line 4 col 16: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 21))

    def test_function_declare_7(self):
        input = """
                Function:  test
                Parameter: Var: x = 5
                Body:
                    Var h = a*b;
                EndBody.
                """
        expect = "Error on line 3 col 27: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_function_declare_8(self):
        input = """
            Function:  test___1
            Parameter: n = 1 , b,c,d
            Body:
                Var: c = 5;
            EndBody.
            """
        expect = "Error on line 3 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_function_declare_9(self):
        input = """
            Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Return 1;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_function_declare_10(self):
        input = """
            Function: foo
            Parameter: a[10], b, c, d
            Body:
                Var: i = {12.,{2,{{2.e5},"hi"},4.}};
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_function_declare_11(self):
        input = """
            Function: test___
            Parameter: x[10], a[2][3][2][9]
            Body:
                Return test({1,2,3,4,5,6,7,8,9,10}, {"abcd","efgh"});
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_local_var_declare_1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_local_var_declare_2(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
              Var: x_ = "a", y_ = a;
            EndBody.
            """
        expect = "Error on line 5 col 34: a"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_local_var_declare_3(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
              Var: x_ = ;
            EndBody.
            """
        expect = "Error on line 5 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_local_var_declare_4(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
              Var: x_ = 5 = z ;
            EndBody.
            """
        expect = "Error on line 5 col 26: ="
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_local_var_declare_5(self):
        input = """
            Function: test____
            Parameter: x[1], a[2]
            Body:
              Var: x_ = 5 , z = " \\n \\t  ";
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_assign_statement_1(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[5] = 1+2;
            EndBody.
             """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_assign_statement_2(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[5][1+2*3\\6%3*(1+2)] = 1;
            EndBody.
             """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_assign_statement_3(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
              a[1+foo(2)] = 1+2;
            EndBody.
             """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_assignment_statement_4(self):
        input = """
            Var: x, y = 5e3, z;
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = (x\\x\\x\\x\\x\\x\\x\\x\\x\\x) * (True || False) * (2.*.y + test___(2)- test());
                x = x -. 20.5;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_assignment_statement_5(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = {{1,2}+{3,4}} || (1+2);
                x[foo()] = x[foo()];
            EndBody.
            """
        expect = "Error on line 5 col 26: +"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_assignment_statement_6(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = y = x;
                x = x -. 20.5;
            EndBody.
            """
        expect = "Error on line 5 col 22: ="
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_assignment_statement_7(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = a[1]+ a[2];
                y = a[2] + 0.;
                b = z*y;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_assignment_statement_8(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = " This is a string {1} ";
                y = this_is_not;
                b = this_a_function("this_a_string");
                t = z+y+b;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_assignment_statement_9(self):
        input = """
            Function: test____
            Parameter: x[1],a[2]
            Body:
                z = !foo(2) && ( a|| b);
                y = z+a;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_if_statement1(self):
        input = """
            Function: test
            Body:
                Var: x;
                If (1) Then x= x+3;
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_if_statement2(self):
        input = """
            Function: test
            Body:
                If ( i < 200) Then  x = y+1;
                ElseIf i >= 200 Then x =y;
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_if_statement3(self):
        input = """
            Function: test
            Body:
                If a>1 Then a = "a " ;
                ElseIf   Then b = "b";
                Else c ="c";
                EndIf.
            EndBody.
            """
        expect = "Error on line 5 col 25: Then"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_if_statement4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_if_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_if_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_if_statement7(self):
        input = """
            Function: test
            Body:
                Var: arr[2] = {2,4}, x = 4.5, y = 5.;
                If arr[1] >. x Then arr[1] = y;
                ElseIf Return 2;
                EndIf
            EndBody.
            """
        expect = "Error on line 6 col 23: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_if_statement8(self):
        input = """
            Function: test
            Body:
                Var: abc = 1, cde = 2, efg = 3;
                If abc + cde == efg Then Else efg = 3;
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_if_statement9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_if_statement10(self):
        input = """
            Function: test
            Body:
                Var: i = 21;
                If i == 10 Then
                ElseIf i == 15 Then
                ElseIf i == 20 Then
                Else
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_if_statement_11(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_if_statement_12(self):
        input = """
                    Function: test
                    Body:
                        If True Then
                        EndIf.
                    EndBody.
                    """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_for_statement1(self):
        input = """
            Function: test
            Body:
                For (i = 0, i < 100, i+1) Do
                    print("i");
                EndFor.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_for_statement2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_for_statement3(self):
        input = """
            Function: test
            Body:
                For (i = 0.5, i <= 1000, 1) Do
                    If i%2 == 0 Then writeln(i\\2);
                    EndIf.
                EndFor.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_for_statement4(self):
        input = """
            Function: test
            Parameter: n
            Body:
                For (i, i <= ((n*n - 2*n + 1) \\ 2), 1) Do
                    print(n);
                EndFor.
            EndBody.
            """
        expect = "Error on line 5 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_for_statement5(self):
        input = """
            Function: test
            Body:
                For (i = 2, flag = c, 1) Do
                    flag = True;
                EndFor.
            EndBody.
            """
        expect = "Error on line 4 col 33: ="
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_for_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_for_statement7(self):
        input = """
            Function: test
            Body:
                For (i = 0, True, False) Do
                EndFor.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_for_statement8(self):
        input = """
            Function: test
            Body:
                Var: a = 2;
                For (i = 10 - foo(2), a < 100, a + 1) Do
                    i = i + 1;
                EndFor.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_while_statement1(self):
        input = """
            Function: test_____
            Body:
                While False Do
                EndWhile.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_while_statement2(self):
        input = """
            Function: test
            Body:
                Var: x = 0;
                While  Do
                EndWhile.
            EndBody.
            """
        expect = "Error on line 5 col 16: While"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_while_statement3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_while_statement4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_while_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_while_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_while_statement7(self):
        input = """
            Function: test
            Body:
                Var: i, arr[100];
                While (i < 100) Do
                    For (j = 1, j < 100, 1) Do
                        arr[i][k] = 1;
                    EndFor.
                    If i<1 Then
                        While (i<100) Do
                        arr[i][k] =1;
                        EndFor.
                EndWhile.
                EndIf.
            EndBody.
            """
        expect = "Error on line 12 col 24: EndFor"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_while_statement8(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_while_statement9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_while_statement10(self):
        input = """
            Function: test
            Parameter: n
            Body:
                Var: i = 0;
                While 1 Do
                    If (i == 10) Then
            EndBody.
                EndWhile.
            """
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_do_while_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_do_while_statement2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_do_while_statement3(self):
        input = """
            Function: test
            Body:
                Var: n = 0, s = 0;
                Do
                  Do 
                  While True EndDo.
            EndBody.
            """
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_do_while_statement4(self):
        input = """
            Function: test
            Body:
                Do
                    i = i + 1;
                    While (j < 100) Do
                        Do
                            While (l < 100) Do
                                l = l + 2;
                            EndWhile.
                        While (k < 100) EndDo.
                        j = j + 3;
                    EndWhile.
                While () EndDo.
            EndBody.
            """
        expect = "Error on line 14 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_do_while_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_do_while_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_do_while_statement_7(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_break_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_break_statement2(self):
        input = """
        Function: testing
        Body:
            While i < 10 Do
                Break;
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_break_statement3(self):
        input = """
        Function: test
        Body:
          Do
            Var: x;
            Break.
        EndBody.
        """
        expect = "Error on line 6 col 17: ."
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_continue_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_continue_statement2(self):
        input = """
        Function: test
        Body:
            While !x Do
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_continue_statement3(self):
        input = """
        Function: test
        Body:
            For (i = 1, i < 100, 1) Do
                If (i%2 !=0) Then Continue
                EndIf.
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_call_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_call_statement2(self):
        input = """
        Function: test
        Body:
            foo(foo());
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_call_statement3(self):
        input = """
        Function: test
        Body:
            foo(2)-5;
        EndBody.
        """
        expect = "Error on line 4 col 18: -"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_call_statement4(self):
        input = """
        Function: test
        Body:
            foo("@#@!#R#$@", {1} , 1.5 \\ 5.e2);
            foo(3,2,1);
            foo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_return_statement1(self):
        input = """
        Function: test
        Body:
            Return ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_return_statement2(self):
        input = """
        Function: test
        Body:
            Return ("hello there");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_return_statement3(self):
        input = """
        Function: test
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return superman();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_all_1(self):
        input = """
                Function: main
                    Body:
                    EndBody.
                Var: a;
                """
        expect = "Error on line 5 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_all_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_all_3(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_all_4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_all_5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_all_6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_all_7(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_all_8(self):
        input = """
                    Var: a,b,c,x,y,z;
                    Function: main
                        Body:
                            a = { -1 };
                            If True Then
                            Var: x;
                            Returnl
                            EndIf.
                        EndBody.
                    """
        expect = "Error on line 5 col 34: -"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_all_9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_all_10(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_all_11(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_all_12(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
