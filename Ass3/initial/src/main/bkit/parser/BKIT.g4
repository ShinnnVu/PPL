grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
	language = Python3;
}
/************************************************ Parser *************************************************/
program: var_declare* func_declare* EOF;
/*************************** var_declare ***************************/
var_declare: VAR CL var_list SM;
var_list: variable (ASSIGN initial_value)? (CM var_list)?;
variable: (scalar | composite);
scalar: ID;
composite: ID dime+;
dime: LS Intlit RS;
initial_value: literal;
literal: Intlit | boolean | FLOATLIT | STRINGLIT | arr;
boolean: TRUE | FALSE;
arr: LB arr_list? RB;
arr_list: literal ( CM literal)*;
/*************************** func_declare ***************************/
func_declare:
	FUNCTION CL ID (PAR CL par_list)? BODY CL statement ENDBODY DOT;
par_list: parameter (CM parameter)*;
parameter: (scalar | composite);
statement: local_var_declare* ( stmt)*;
stmt:
	assign_statement
	| if_statement
	| for_statement
	| while_statement
	| do_while_statement
	| break_statement
	| continue_statement
	| call_statement
	| return_statement;
local_var_declare: var_declare;
stmt_list: statement;
/** statement  **/
assign_statement: (exp6 | ID) ASSIGN expression SM;
if_statement:
	IF expression THEN stmt_list (
		ELSEIF expression THEN stmt_list
	)* (ELSE stmt_list)? ENDIF DOT;
for_statement:
	FOR LP scalar ASSIGN expression CM expression CM expression RP DO stmt_list ENDFOR DOT;
while_statement: WHILE expression DO stmt_list ENDWHILE DOT;
do_while_statement: DO stmt_list WHILE expression ENDDO DOT;
break_statement: BREAK SM;
continue_statement: CONT SM;
call_statement: ID LP (expression_list)? RP SM;
return_statement: RETURN expression? SM;
index_operators: (LS expression RS)+;
//** expression */
expression: exp1 rela_operator exp1 | exp1;
exp1: exp1 logic_operator exp2 | exp2;
exp2: exp2 add_operator exp3 | exp3;
exp3: exp3 mul_operator exp4 | exp4;
exp4: not_operator exp4 | exp5;
exp5: sign_operator exp5 | exp6;
exp6: exp6 index_operators | exp7;
exp7: func_call | LP expression RP | operands;
operands: literal | ID;
expression_list: expression (CM expression)*;
/** func_call **/
func_call: ID LP (expression_list)? RP;

//** Operators */
rela_operator:
	EQUAL
	| NOT_EQUAL
	| LT
	| GT
	| LE
	| GE
	| NOT_EQUALF
	| LTF
	| GTF
	| LEF
	| GEF;
logic_operator: AND | OR;
add_operator: ADD | ADDF | SUB | SUBF;
mul_operator: MUL | MULF | DIV | DIVF | MOD;
not_operator: NOT;
sign_operator: SUB | SUBF;

/************************************************ Lexer **************************************************/
/************************ KEYWORDS ************************/
BODY: 'Body';
ELSE: 'Else';
ENDFOR: 'EndFor';
IF: 'If';
VAR: 'Var';
ENDDO: 'EndDo';
BREAK: 'Break';
ELSEIF: 'ElseIf';
ENDWHILE: 'EndWhile';
PAR: 'Parameter';
WHILE: 'While';
CONT: 'Continue';
ENDBODY: 'EndBody';
FOR: 'For';
RETURN: 'Return';
TRUE: 'True';
FALSE: 'False';
DO: 'Do';
ENDIF: 'EndIf';
FUNCTION: 'Function';
THEN: 'Then';
// Skip comments
BLOCK_COMMENT: ('**' .*? '**') -> skip;
/************************ FRAGMENTS ************************/
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment Exp: [eE] [+-]? Digit+;
fragment STR_CHAR: ~[\n'"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [btnfr'\\] | '\'"';
fragment ILLEGAL_CHAR: (('\\' ~[btnfr'\\]) | '\'' ~'"');
/************************ LITERALS *************************/
Intlit: INTLIT | HEXALIT | OCTLIT;
INTLIT: '0' | NonZeroDigit Digit*;
HEXALIT: '0' [xX][1-9A-F][0-9A-F]*;
OCTLIT: '0' [oO][1-7][0-7]*;
FLOATLIT: Digit+ DOT Digit* Exp? | Digit+ DOT? Exp;
BOOLEAN: TRUE | FALSE;
STRINGLIT:
	'"' STR_CHAR* '"' {
		y = str(self.text)
		self.text = y[1:-1]
	};
/************************ OPERATORS ************************/
/****** Arithmetic operators ******/
/** INT **/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';
/** FLOAT **/
ADDF: '+.';
SUBF: '-.';
MULF: '*.';
DIVF: '\\.';
/****** Boolean operators ******/
NOT: '!';
AND: '&&';
OR: '||';
/****** Relational operators ******/
/** INT **/
EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
/** FLOAT **/
NOT_EQUALF: '=/=';
LTF: '<.';
GTF: '>.';
LEF: '<=.';
GEF: '>=.';
/****** Separators ******/
LP: '(';
RP: ')';
LS: '[';
RS: ']';
CL: ':';
DOT: '.';
CM: ',';
SM: ';';
LB: '{';
RB: '}';
ASSIGN: '=';
/* Else */
ID: [a-z]([a-zA-Z0-9_])*;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING:
	'"' STR_CHAR* ('\n' | EOF) {
    self.text = self.text[1:]
    if self.text[-1] == '\n':
        self.text = self.text[:-1]
};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ILLEGAL_CHAR {
    self.text = self.text[1:]
};
UNTERMINATED_COMMENT: '**' .*?;