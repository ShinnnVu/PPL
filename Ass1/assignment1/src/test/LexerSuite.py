import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "abcIf Do ifIf", "abcIf,Do,ifIf,<EOF>", 101))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "co lam thi moi co an", "co,lam,thi,moi,co,an,<EOF>", 102))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1wqertyuiopasdfghjklzxcvbnm", "1,wqertyuiopasdfghjklzxcvbnm,<EOF>", 103))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "shinnVu was not an impostor", "shinnVu,was,not,an,impostor,<EOF>", 104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "hohoho_DiO", "hohoho_DiO,<EOF>", 105))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("aBcDd Doconga",
                                              "aBcDd,Do,conga,<EOF>", 106))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("wewewewewewA_@1",
                                              "wewewewewewA_,Error Token @", 107))

    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a = thay_giao_ba((0175)", "a,=,thay_giao_ba,(,(,0,175,),<EOF>", 108))

    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "meo meo Nibba", "meo,meo,Error Token N", 109))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "dien12 23123dien Ifyougay", "dien12,23123,dien,If,yougay,<EOF>", 110))

    def test_all_keyword(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Body Break Continue Do EndDo Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False", "Body,Break,Continue,Do,EndDo,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,<EOF>", 111))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "If Do thEn Else ", "If,Do,thEn,Else,<EOF>", 112))

    def test_keyword_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Continuee cOntinue ", "Continue,e,cOntinue,<EOF>", 113))

    def test_keyword_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: variable_list;", "Var,:,variable_list,;,<EOF>", 114))

    def test_keyword_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Body body bOdy boDy bodY BODY", "Body,body,bOdy,boDy,bodY,Error Token B", 115))

    def test_keyword_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "WhileWhDododododo", "While,Error Token W", 116))

    def test_keyword_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "EndFor ElseFor Endfor", "EndFor,Else,For,Error Token E", 117))

    def test_keyword_8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "string False True", "string,False,True,<EOF>", 118))

    def test_blockcomment_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ ** ** ** **  """, """<EOF>""", 119))

    def test_blockcomment_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ **b = (a=c+d*e)+f//5 || (True|False);**  """, """<EOF>""", 120))

    def test_blockcomment_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" **Nhau khong may!
                                                   *Ok nhau !
                                                   *O dau?
                                                   *quan dang sau KTX
                                                   *OK**""", """<EOF>""", 121))

    def test_blockcomment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""****""", """<EOF>""", 122))

    def test_blockcomment_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** ** ** *** ** ** **""", """*,Unterminated Comment""", 123))

    def test_blockcomment_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** Mot con ga \n xoe ra hai cai canh \b \r \n \t \\** """, """<EOF>""", 124))

    def test_blockcomment_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "***** *csGoCases*", "*,*,csGoCases,*,<EOF>", 125))

    def test_operators_1(self):
        self.assertTrue(TestLexer.checkLexeme("1+2=3", "1,+,2,=,3,<EOF>", 126))

    def test_operators_2(self):
        self.assertTrue(TestLexer.checkLexeme("(2+4)*3\\3\\3 <= ((2+3*5-2)\\9)%4",
                                              "(,2,+,4,),*,3,\,3,\,3,<=,(,(,2,+,3,*,5,-,2,),\,9,),%,4,<EOF>", 127))

    def test_operators_3(self):
        self.assertTrue(TestLexer.checkLexeme("+ +. - -. * *. \\ \\. % ! && || =  == != < <. > >. <= <=. >= >=. =/=",
                                              "+,+.,-,-.,*,*.,\,\.,%,!,&&,||,=,==,!=,<,<.,>,>.,<=,<=.,>=,>=.,=/=,<EOF>", 128))

    def test_operators_4(self):
        self.assertTrue(TestLexer.checkLexeme("(2++3=5) && ((2*3)\\0xAF21 && 9.*.x+ 29-.12%2-0O1234567",
                                              "(,2,+,+,3,=,5,),&&,(,(,2,*,3,),\,0xAF21,&&,9.,*.,x,+,29,-.,12,%,2,-,0O1234567,<EOF>", 129))

    def test_operators_5(self):
        self.assertTrue(TestLexer.checkLexeme("57e9 -%- == True  3.*.a+.5*x\\y!==\\.=98129>.1<.2020952.<=17",
                                              "57e9,-,%,-,==,True,3.,*.,a,+.,5,*,x,\,y,!=,=,\.,=,98129,>.,1,<.,2020952.,<=,17,<EOF>", 130))

    def test_operators_6(self):
        self.assertTrue(TestLexer.checkLexeme("!(!(!(!!!a,b)))) +-* 21\\2\\2\\2\\7.*.2*.7*.2.",
                                              "!,(,!,(,!,(,!,!,!,a,,,b,),),),),+,-,*,21,\,2,\,2,\,2,\,7.,*.,2,*.,7,*.,2.,<EOF>", 131))

    def test_operators_7(self):
        self.assertTrue(TestLexer.checkLexeme("(1234564 +878*231\\.51231 > 1231*89751) || ((True && False) || -999.999*a < -8.999b)",
                                              "(,1234564,+,878,*,231,\.,51231,>,1231,*,89751,),||,(,(,True,&&,False,),||,-,999.999,*,a,<,-,8.999,b,),<EOF>", 132))

    def test_operators_8(self):
        self.assertTrue(TestLexer.checkLexeme("s > b < c >= e <=. a\\.b + c - d * e && z +. l -. x *. f \\ s",
                                              "s,>,b,<,c,>=,e,<=.,a,\.,b,+,c,-,d,*,e,&&,z,+.,l,-.,x,*.,f,\,s,<EOF>", 133))

    def test_operators_9(self):
        self.assertTrue(TestLexer.checkLexeme("!a%5&&b||c +.0.e05*.>.0e05>.",
                                              "!,a,%,5,&&,b,||,c,+.,0.e05,*.,>.,0e05,>.,<EOF>", 134))

    def test_operators_10(self):
        self.assertTrue(TestLexer.checkLexeme("!(ve && a * (ccc || \\0.e1\\\\\\\\\\\\\\\\ ",
                                              "!,(,ve,&&,a,*,(,ccc,||,\,0.e1,\,\,\,\,\,\,\,\,<EOF>", 135))

    def test_all_separators(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("()[]{}:.,; ",
                                              "(,),[,],{,},:,.,,,;,<EOF>", 136))

    def test_separators_1(self):
        self.assertTrue(TestLexer.checkLexeme("123fdf[[[asdsad]]; {{{,,;:.asds; d, ]][[qwewqr[",
                                              "123,fdf,[,[,[,asdsad,],],;,{,{,{,,,,,;,:,.,asds,;,d,,,],],[,[,qwewqr,[,<EOF>", 137))

    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(
            "0200021230XAB", "0,200021230,Error Token X", 138))

    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x01 0o0FF", "0,x01,0,o0FF,<EOF>", 139))

    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "000 1999 0XFF 0xFF 0o1234567 0O1234567 0o01", "0,0,0,1999,0XFF,0xFF,0o1234567,0O1234567,0,o01,<EOF>", 140))

    def test_integer4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "20398723819290132 0942112212", "20398723819290132,0,942112212,<EOF>", 141))

    def test_integer5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x123456789ABCDEF", "0x123456789ABCDEF,<EOF>", 142))

    def test_integer6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x09876543210ABCDEF 0X9876543210abcdef", "0,x09876543210ABCDEF,0X9876543210,abcdef,<EOF>", 143))

    def test_integer7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o12345670 Oo01234567", "0o12345670,Error Token O", 144))

    def test_integer8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o1234567 0O012", "0o1234567,0,Error Token O", 145))

    def test_integer9(self):
        self.assertTrue(TestLexer.checkLexeme("12345 + 23456 \\ 0O1234567 0X123456789ABCDEF 0x0123",
                                              "12345,+,23456,\,0O1234567,0X123456789ABCDEF,0,x0123,<EOF>", 146))

    def test_integer10(self):
        self.assertTrue(TestLexer.checkLexeme("00123 . e 05 || x0AF1221",
                                              "0,0,123,.,e,0,5,||,x0AF1221,<EOF>", 147))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234e1234", "1234e1234,<EOF>", 148))

    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234.e1234", "1234.e1234,<EOF>", 149))

    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234.1234", "1234.1234,<EOF>", 150))

    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234.0e1234", "1234.0e1234,<EOF>", 151))

    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234. 1234", "1234.,1234,<EOF>", 152))

    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "1234e-1 1234e+1 1234e1", "1234e-1,1234e+1,1234e1,<EOF>", 153))

    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0e00 0x00.12e5 1234e-1234", "0e00,0,x00,.,12e5,1234e-1234,<EOF>", 154))

    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme(
            ".e5 .5 .5e5 01e2.2 ", ".,e5,.,5,.,5e5,01e2,.,2,<EOF>", 155))

    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("144.40230e55 12623.711561 1012321.e395564 25.123154157 20043.83e841 23405.313014",
                                              "144.40230e55,12623.711561,1012321.e395564,25.123154157,20043.83e841,23405.313014,<EOF>", 156))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b \\t \\n \\f \\r \\' \\\\" """,
                                              """\\b \\t \\n \\f \\r \\' \\\\,<EOF>""", 157))

    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "John asked me: '"Where is him?'"" """, """John asked me: '"Where is him?'",<EOF>""", 158))

    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\\\ \\\\ \\\\\\\\ \\b\\b\\'\\'"  """, """\\\\ \\\\ \\\\\\\\ \\b\\b\\'\\',<EOF>""", 159))

    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "\"\"\"yasuo\"\"\"\" " """, """,,yasuo,,,Unclosed String:  """, 160))

    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ " '" abcxyz '"'" \\\\ "  """, """ '" abcxyz '"'" \\\\ ,<EOF>""", 161))

    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ " This is it '"\\' "  """, """ This is it '"\\' ,<EOF>""", 162))

    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "~!@#@$#%$%(&$@#$!@)%#@!#@(!)#@!#~@`12123"  """, """~!@#@$#%$%(&$@#$!@)%#@!#@(!)#@!#~@`12123,<EOF>""", 163))

    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" " '"'"'"'"'"'"'"'" "  """,
                                              """ '"'"'"'"'"'"'"'" ,<EOF>""", 164))

    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "http://e-learning.hcmut.edu.vn/pluginfile.php?file=%2F1188196%2Fmod_resource%2Fcontent%2F3%2FBKIT2009%20Specification-2.2.pdf"  """,
                                              """http://e-learning.hcmut.edu.vn/pluginfile.php?file=%2F1188196%2Fmod_resource%2Fcontent%2F3%2FBKIT2009%20Specification-2.2.pdf,<EOF>""", 165))

    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "!@#@$#%#%$$#@324#$#$234234[{}.;,/qwlezoxchqweqwoezasgjfxzdae"  """, """!@#@$#%#%$$#@324#$#$234234[{}.;,/qwlezoxchqweqwoezasgjfxzdae,<EOF>""", 166))

    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "**this is a single-line comment**" """, """**this is a single-line comment**,<EOF>""", 167))

    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "****************** \\t ************** \\t \\t" """, """****************** \\t ************** \\t \\t,<EOF>""", 168))

    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" " \\t \'\" \'\" " """,
                                              """ \\t '" '" ,<EOF>""", 169))

    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\'\"'"-'"\'\" \'\"\'\" Tp.HCM" """,
                                              """'"'"-'"'" '"'" Tp.HCM,<EOF>""", 170))

    def test_unterminated_string1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 171))

    def test_unterminated_string2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "string1" "string2" "x """, """string1,string2,Unclosed String: x """, 172))

    def test_unterminated_string3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "string1 \n string2" """, """Unclosed String: string1 \n""", 173))

    def test_unterminated_string4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\b \\t \\n \\f \\r '\" """, """Unclosed String: \\b \\t \\n \\f \\r '" """, 174))

    def test_unterminated_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string1" "string2" \" string 3 \" \" string 4" \" """,
                                              """string1,string2, string 3 , string 4,Unclosed String:  """, 175))

    def test_unterminated_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" " "string1" \" a \"b \"c \" \n """,
                                              """ ,string1, ,a,b ,c,Unclosed String:  \n""", 176))

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "graph\\h def"  """, """Illegal Escape In String: graph\\h""", 177))

    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\ \\"  """,
                                              """Illegal Escape In String: abc\\\\ \\\"""", 178))

    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ " string \'" \' "  """, """Illegal Escape In String:  string '" ' """, 179))

    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "!@#@!#!@# \'\' "  """, """Illegal Escape In String: !@#@!#!@# ''""", 180))

    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"wqewqeqw" \" weqwewqeqwe\\$ " """,
                                              """wqewqeqw,Illegal Escape In String:  weqwewqeqwe\$""", 181))

    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "D:\\Works_HK5_PPL_assignment1_src\test\testcases" """, """Illegal Escape In String: D:\W""", 182))

    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\b \\n \\rr \\rr \\'\\$ ga " """, """Illegal Escape In String: \\b \\n \\rr \\rr \\'\\$""", 183))

    def test_unterminated_comment1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**2*3*""", """Unterminated Comment""", 184))

    def test_unterminated_comment2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ ** Skip ** **** ** 2*3*""", """Unterminated Comment""", 185))

    def test_unterminated_comment3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """******""", """Unterminated Comment""", 186))

    def test_unterminated_comment4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """******""", """Unterminated Comment""", 187))

    def test_unterminated_comment5(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** ** ** *""", """Unterminated Comment""", 188))

    def test_var_declare_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: b[1] = {{1,2,3},{4,5,6},{}};
                   Var: x;
                   Var: x[1][2][3][4][5];
                   Var: m,n[10];
                   Var: a, b = 1, c, d,e ={1};""",
                                              """Var,:,b,[,1,],=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},,,{,},},;,Var,:,x,;,Var,:,x,[,1,],[,2,],[,3,],[,4,],[,5,],;,Var,:,m,,,n,[,10,],;,Var,:,a,,,b,=,1,,,c,,,d,,,e,=,{,1,},;,<EOF>""", 189))

    def test_var_declare_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = 1+2;
                                                 Var: b[1][2][3] = ((True ||False))>.{{1,2}}""",
                                              """Var,:,a,=,1,+,2,;,Var,:,b,[,1,],[,2,],[,3,],=,(,(,True,||,False,),),>.,{,{,1,,,2,},},<EOF>""", 190))

    def test_var_declare_4(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a[1][2][3][4] = b[[1]],b;""",
                                              """Var,:,a,[,1,],[,2,],[,3,],[,4,],=,b,[,[,1,],],,,b,;,<EOF>""", 191))

    def test_var_declare_5(self):
        self.assertTrue(TestLexer.checkLexeme("""Var:a;
                                                 Var:b;
                                                 Var:c,d,e,f,g[1][2];""", """Var,:,a,;,Var,:,b,;,Var,:,c,,,d,,,e,,,f,,,g,[,1,],[,2,],;,<EOF>""", 192))

    def test_func_declare_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
                                                 Parameter: a,b;
                                                 Body:
                                                 EndBody.""",
                                              """Function,:,foo,Parameter,:,a,,,b,;,Body,:,EndBody,.,<EOF>""", 193))

    def test_func_declare_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: x;
                                                Function: fact
                                                Parameter: n
                                                Body:
                                                If n == 0 Then
                                                Return 1;
                                                Else
                                                Return n * fact (n - 1);
                                                EndIf.
                                                EndBody.
                                                Function: main
                                                Body:
                                                x = 10;
                                                fact (x);
                                                EndBody.""", """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""", 194))

    def test_full_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a[3 + foo(2)] = a[b[2][3]] + 4;
                                                 Function: boo
                                                 Parameter: a
                                                 Body:
                                                 EndBody.
""",
                                              """Var,:,a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,Function,:,boo,Parameter,:,a,Body,:,EndBody,.,<EOF>""", 195))

    def test_full_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: abc = 12*.2e5 - 0xEF12, st = "@gmail\\neqweqwe",  **var here** \\. 91.012e2""",
                                              """Var,:,abc,=,12,*.,2e5,-,0xEF12,,,st,=,@gmail\\neqweqwe,,,\\.,91.012e2,<EOF>""", 196))

    def test_full_3(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i< n, i+1) Do x= "Omeu wa mou shinderu" EndFor..""",
                                              """For,(,i,=,0,,,i,<,n,,,i,+,1,),Do,x,=,Omeu wa mou shinderu,EndFor,.,.,<EOF>""", 197))

    def test_full_4(self):
        self.assertTrue(TestLexer.checkLexeme("""If (x<5) Then
                                                 For (i = 0, i < 10, 2) Do
                                                    writeln(i);
                                                    EndFor.
                                                EndIf.""",
                                              """If,(,x,<,5,),Then,For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,EndIf,.,<EOF>""", 198))

    def test_full_5(self):
        self.assertTrue(TestLexer.checkLexeme("""Body:
                                                    Var: r = 10., v;
                                                    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                                                    foo (2 + x, 4. \. y);
                                                    goo ();
                                                    EndBody.
                                                    """,
                                              """Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,foo,(,2,+,x,,,4.,\.,y,),;,goo,(,),;,EndBody,.,<EOF>""", 199))

    def test_full_6(self):
        self.assertTrue(TestLexer.checkLexeme("""Body:
                                                    Var: r = 10., v;
                                                    goo ();
                                                    str ="String \\b \\t \\n " ** This is a comment **
                                                    EndBody.
                                                    """,
                                              """Body,:,Var,:,r,=,10.,,,v,;,goo,(,),;,str,=,String \\b \\t \\n ,EndBody,.,<EOF>""", 200))
