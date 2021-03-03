from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):
    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        # program: var_declare* func_declare* EOF;
        programs = []
        for x in ctx.var_declare():
            inst = self.visit(x)
            if isinstance(inst, list):
                programs.extend(inst)
            else:
                programs.append(inst)
        for x in ctx.func_declare():
            inst = self.visit(x)
            if isinstance(inst, list):
                programs.extend(inst)
            else:
                programs.append(inst)
        return Program(programs)
    # Visit a parse tree produced by BKITParser#var_declare.

    def visitVar_declare(self, ctx: BKITParser.Var_declareContext):
        # var_declare: VAR CL var_list SM;
        return self.visit(ctx.var_list())

    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx: BKITParser.Var_listContext):
        # var_list: variable(ASSIGN initial_value)? (CM var_list)*
        if ctx.initial_value():
            initial_value = self.visit(ctx.initial_value())
        else:
            initial_value = None
        inst = self.visit(ctx.variable())
        if isinstance(inst, list):
            Ids = Id(str(inst[0]))
            dime = list(inst[1:])
        else:
            Ids = Id(str(inst))
            dime = []
        return [VarDecl(Ids, dime, initial_value)] + self.visit(ctx.var_list()) if ctx.var_list() else [VarDecl(Ids, dime, initial_value)]
        reversed()

    def visitVariable(self, ctx: BKITParser.VariableContext):
        if ctx.scalar():
            return self.visit(ctx.scalar())
        if ctx.composite():
            return self.visit(ctx.composite())
        # Visit a parse tree produced by BKITParser#scalar.

    def visitScalar(self, ctx: BKITParser.ScalarContext):
        return str(ctx.ID())
    # Visit a parse tree produced by BKITParser#composite.

    def visitComposite(self, ctx: BKITParser.CompositeContext):
        Id = str(ctx.ID())
        dime = []
        for x in ctx.dime():
            inst = self.visit(x)
            if isinstance(inst, list):
                dime.extend(inst)
            else:
                dime.append(inst)
        return list([Id]+dime)

    # Visit a parse tree produced by BKITParser#dime.
    def visitDime(self, ctx: BKITParser.DimeContext):
        return eval(str(ctx.Intlit()))

    # Visit a parse tree produced by BKITParser#initial_value.
    def visitInitial_value(self, ctx: BKITParser.Initial_valueContext):
        return self.visit(ctx.literal())

    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.Intlit():
            return IntLiteral(eval(str(ctx.Intlit())))
        if ctx.boolean():
            return self.visit(ctx.boolean())
        if ctx.FLOATLIT():
            return FloatLiteral(float(str(ctx.FLOATLIT())))
        if ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT()))
        if ctx.arr():
            return self.visit(ctx.arr())
    # Visit a parse tree produced by BKITParser#boolean.

    def visitBoolean(self, ctx: BKITParser.BooleanContext):
        if ctx.TRUE():
            value = True
        else:
            value = False
        return BooleanLiteral(value)

    # Visit a parse tree produced by BKITParser#arr.
    def visitArr(self, ctx: BKITParser.ArrContext):
        if ctx.arr_list():
            return ArrayLiteral(self.visit(ctx.arr_list()))
        else:
            return ArrayLiteral([])
    # Visit a parse tree produced by BKITParser#arr_list.

    def visitArr_list(self, ctx: BKITParser.Arr_listContext):
        array = []
        for x in ctx.literal():
            inst = self.visit(x)
            if isinstance(inst, list):
                array.extend(inst)
            else:
                array.append(inst)
        return array

    # Visit a parse tree produced by BKITParser#func_declare.
    def visitFunc_declare(self, ctx: BKITParser.Func_declareContext):
       # func_declare: FUNCTION CL ID(PAR CL par_list)? BODY CL statement ENDBODY DOT
        Ids = Id(str(ctx.ID()))
        if ctx.par_list():
            param = self.visit(ctx.par_list())
        else:
            param = []
        body = self.visit(ctx.statement())
        return [FuncDecl(Ids, param, body)]
        # Visit a parse tree produced by BKITParser#par_list.

    def visitPar_list(self, ctx: BKITParser.Par_listContext):
        # par_list: parameter(CM parameter)*
        par = []
        initial_value = None
        for x in ctx.parameter():
            inst = self.visit(x)
            if isinstance(inst, list):
                Ids = Id(str(inst[0]))
                dime = list(inst[1:])
            else:
                Ids = Id(str(inst))
                dime = []
            par.append(VarDecl(Ids, dime, initial_value))
        return par

    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx: BKITParser.ParameterContext):
        # parameter: (scalar | composite)
        if ctx.scalar():
            return self.visit(ctx.scalar())
        if ctx.composite():
            return self.visit(ctx.composite())
        # Visit a parse tree produced by BKITParser#statement.

    def visitStatement(self, ctx: BKITParser.StatementContext):
        # statement: local_var_declare * (stmt)*
        local_var = []
        for x in ctx.local_var_declare():
            inst = self.visit(x)
            if isinstance(inst, list):
                local_var.extend(inst)
            else:
                local_var.append(inst)
        stmt_list = []
        for x in ctx.stmt():
            inst = self.visit(x)
            if isinstance(inst, list):
                stmt_list.extend(inst)
            else:
                stmt_list.append(inst)
        return (local_var, stmt_list)

    # Visit a parse tree produced by BKITParser#stmt.

    def visitStmt(self, ctx: BKITParser.StmtContext):
        return [self.visit(ctx.getChild(0))]
    # Visit a parse tree produced by BKITParser#local_var_declare.

    def visitLocal_var_declare(self, ctx: BKITParser.Local_var_declareContext):
        #local_var_declare: var_declare;
        return self.visit(ctx.var_declare())

    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx: BKITParser.Stmt_listContext):
        #stmt_list: statement;
        return self.visit(ctx.statement())

    # Visit a parse tree produced by BKITParser#assign_statement.
    def visitAssign_statement(self, ctx: BKITParser.Assign_statementContext):
        # assign_statement: (exp6 | ID) ASSIGN expression SM;
        rhs = self.visit(ctx.expression())
        if ctx.ID():
            lhs = Id(str(ctx.ID()))
        else:
            lhs = self.visit(ctx.exp6())
        return Assign(lhs, rhs)
        # Visit a parse tree produced by BKITParser#if_statement.

    def visitIf_statement(self, ctx: BKITParser.If_statementContext):
        # if_statement:IF expression THEN stmt_list(ELSEIF expression THEN stmt_list)* (ELSE stmt_list)? ENDIF DOT
        ifthenStmt = []
        for x in range(len(ctx.expression())):
            stmt_list = self.visit(ctx.stmt_list(x))
            ifthenStmt.extend(
                [((self.visit(ctx.expression(x))), stmt_list[0], stmt_list[1])])
        if ctx.ELSE():
            elseStmt = self.visit(ctx.stmt_list()[-1])
        else:
            elseStmt = ([], [])
        return If(ifthenStmt, elseStmt)

    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx: BKITParser.For_statementContext):
        # for_statement:FOR LP scalar ASSIGN expression CM expression CM expression RP DO stmt_list ENDFOR DOT
        Ids = Id(self.visit(ctx.scalar()))
        exp1 = self.visit(ctx.expression(0))
        exp2 = self.visit(ctx.expression(1))
        exp3 = self.visit(ctx.expression(2))
        loop = self.visit(ctx.stmt_list())
        return For(Ids, exp1, exp2, exp3, loop)

    # Visit a parse tree produced by BKITParser#while_statement.

    def visitWhile_statement(self, ctx: BKITParser.While_statementContext):
        # while_statement: WHILE expression DO stmt_list ENDWHILE DOT;
        exp = self.visit(ctx.expression())
        sl = self.visit(ctx.stmt_list())
        return While(exp, sl)

    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx: BKITParser.Do_while_statementContext):
        # do_while_statement: DO stmt_list WHILE expression ENDDO DOT;
        sl = self.visit(ctx.stmt_list())
        exp = self.visit(ctx.expression())
        return Dowhile(sl, exp)

    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx: BKITParser.Break_statementContext):
        return Break()

    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return Continue()

    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx: BKITParser.Call_statementContext):
        # call_statement: ID LP (expression_list)? RP SM;
        method = Id(str(ctx.ID()))
        if ctx.expression_list():
            param = self.visit(ctx.expression_list())
        else:
            param = []
        return CallStmt(method, param)
    # Visit a parse tree produced by BKITParser#return_statement.

    def visitReturn_statement(self, ctx: BKITParser.Return_statementContext):
        # return_statement: RETURN expression? SM;
        if ctx.expression():
            exp = self.visit(ctx.expression())
        else:
            exp = None
        return Return(exp)

        # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx: BKITParser.Index_operatorsContext):
        idx = []
        for x in ctx.expression():
            inst = self.visit(x)
            if isinstance(inst, list):
                idx.extend(inst)
            else:
                idx.append(inst)
        return idx

    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = self.visit(ctx.rela_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp1(0))

    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            op = self.visit(ctx.logic_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp2())

    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            op = self.visit(ctx.add_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp3())

    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            op = self.visit(ctx.mul_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.exp4())

    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() > 1:
            op = self.visit(ctx.not_operator())
            body = self.visit(ctx.exp4())
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.exp5())

    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() > 1:
            op = self.visit(ctx.sign_operator())
            body = self.visit(ctx.exp5())
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.exp6())

    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.getChildCount() > 1:
            arr = self.visit(ctx.exp6())
            idx = self.visit(ctx.index_operators())
            return ArrayCell(arr, idx)
        else:
            return self.visit(ctx.exp7())

    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx: BKITParser.Exp7Context):
        if ctx.func_call():
            return self.visit(ctx.func_call())
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.operands():
            return self.visit(ctx.operands())

            # Visit a parse tree produced by BKITParser#operands.

    def visitOperands(self, ctx: BKITParser.OperandsContext):
        if ctx.ID():
            return Id(str(ctx.ID()))
        if ctx.literal():
            return self.visit(ctx.literal())

    # Visit a parse tree produced by BKITParser#expression_list.
    def visitExpression_list(self, ctx: BKITParser.Expression_listContext):
        exp = []
        for x in ctx.expression():
            inst = self.visit(x)
            if isinstance(inst, list):
                exp.extend(inst)
            else:
                exp.append(inst)
        return exp

    # Visit a parse tree produced by BKITParser#func_call.

    def visitFunc_call(self, ctx: BKITParser.Func_callContext):
        Ids = Id(str(ctx.ID()))
        if ctx.expression_list():
            param = self.visit(ctx.expression_list())
        else:
            param = []
        return CallExpr(Ids, param)

    # Visit a parse tree produced by BKITParser#rela_operator.
    def visitRela_operator(self, ctx: BKITParser.Rela_operatorContext):
        return str(ctx.getChild(0))

    # Visit a parse tree produced by BKITParser#logic_operator.

    def visitLogic_operator(self, ctx: BKITParser.Logic_operatorContext):
        return str(ctx.getChild(0))

    # Visit a parse tree produced by BKITParser#add_operator.
    def visitAdd_operator(self, ctx: BKITParser.Add_operatorContext):
        return str(ctx.getChild(0))

    # Visit a parse tree produced by BKITParser#mul_operator.
    def visitMul_operator(self, ctx: BKITParser.Mul_operatorContext):
        return str(ctx.getChild(0))
    # Visit a parse tree produced by BKITParser#not_operator.

    def visitNot_operator(self, ctx: BKITParser.Not_operatorContext):
        return str(ctx.getChild(0))

    # Visit a parse tree produced by BKITParser#sign_operator.
    def visitSign_operator(self, ctx: BKITParser.Sign_operatorContext):
        return str(ctx.getChild(0))
