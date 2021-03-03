from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        reduce(lambda acc,lee: self.visit(acc,lee),ctx.decl,)

    def visitVarDecl(self, ctx: VarDecl, o):
        return ctx

    def visitBinOp(self, ctx: BinOp, o):)
        type1 = self.visit(ctx.e1, o)
        type2 = self.visit(ctx.e2, o)
        if (ctx.op == "+" or ctx.op == "-" or ctx.op == "*"):
            if type1 == "bool" or type2 == "bool":
                raise TypeMismatchInExpression(ctx)
            if type1 == "float" or type2 == "float":
                return "float"
            return "int"
        if (ctx.op == "/"):
            if type1 == "bool" or type2 == "bool":
                raise TypeMismatchInExpression(ctx)
            return "float"
        if (ctx.op == "&&" or ctx.op == "||"):
            if type1 == "bool" and type2 == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if (ctx.op == ">" or ctx.op == "<" or ctx.op == "==" or ctx.op == "!="):
            if type1 != type2:
                raise TypeMismatchInExpression(ctx)
            return "bool"

    def visitUnOp(self, ctx: UnOp, o):
        type1 = self.visit(ctx.e, o)
        if (ctx.op == "-"):
            if (type1 == "bool"):
                raise TypeMismatchInExpression(ctx)
            if (type1 == "float"):
                return "float"
            if (type1 == "int"):
                return "int"
        if (ctx.op == "!"):
            if (type1 == "bool"):
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"

    def visitId(self, ctx, o):
        for decl in o:
            if (decl.name == ctx.name):
                type1 = decl.typ
                if isinstance(type1, IntType()):
                    return "int"
                if isinstance(type1, FloatType()):
                    return "float"
                if isinstance(type1, BoolType()):
                    return "bool"
        raise UndeclaredIdentifier(ctx.name)
