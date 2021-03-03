from functools import reduce


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ctx.decl, [])

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        paramList = reduce(lambda x, y: [self.visit(y, x)] + x, ctx.param, [])
        declList = reduce(lambda x, y: [self.visit(
            y, x)] + x, ctx.body[0], paramList + [ctx.name])
        expList = reduce(lambda x, y: [self.visit(
            y, x)] + x, ctx.body[1], paramList + o + declList)
        return ctx.name

    def visitIntType(self, ctx: IntType, o: object): pass

    def visitFloatType(self, ctx: FloatType, o: object): pass

    def visitIntLit(self, ctx: IntLit, o: object): pass

    def visitId(self, ctx: Id, o: object):
        if ctx.name not in o:
            raise UndeclaredIndentifier(ctx.name)
