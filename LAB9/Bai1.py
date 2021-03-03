class StaticCheck(Visitor):

    def visitBinOp(self, ctx: BinOp, o):
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
