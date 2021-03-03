from functools import reduce
from abc import ABC


class Type(ABC):
    pass  # abstract class


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class InferredType(Type):
    pass


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        listDcl = reduce(lambda x, y: [self.visit(y, x)] + x, ctx.decl, [])
        varDecl = {}
        varDecl['varDecl'] = listDcl
        [self.visit(x, varDecl) for x in ctx.stmts]

    def visitVarDecl(self, ctx: VarDecl, o):
        return ctx

    def visitAssign(self, ctx: Assign, o):
        self.visit(ctx.lhs, o)
        self.visit(ctx.rhs, o)
        if type(self.visit(ctx.lhs, o)) == InferredType and type(self.visit(ctx.rhs, o)) == InferredType:
            raise TypeCannotBeInferred(ctx)
        elif type(self.visit(ctx.lhs, o)) == InferredType:
            o[ctx.lhs.name] = self.visit(ctx.rhs, o)
        elif type(self.visit(ctx.rhs, o)) == InferredType:
            o[ctx.rhs.name] = self.visit(ctx.lhs, o)
        if type(self.visit(ctx.lhs, o)) != type(self.visit(ctx.rhs, o)):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        if ctx.op in ['+', '-', '*', '/']:
            if type(self.visit(ctx.e1, o)) == InferredType:
                o[ctx.e1.name] = IntType()
            if type(self.visit(ctx.e2, o)) == InferredType:
                o[ctx.e2.name] = IntType()
            if type(self.visit(ctx.e1, o)) == IntType and type(self.visit(ctx.e2, o)) == IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if type(self.visit(ctx.e1, o)) == InferredType:
                o[ctx.e1.name] = FloatType()
            if type(self.visit(ctx.e2, o)) == InferredType:
                o[ctx.e2.name] = FloatType()
            if type(self.visit(ctx.e1, o)) == FloatType and type(self.visit(ctx.e2, o)) == FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>', '=']:
            if type(self.visit(ctx.e1, o)) == InferredType:
                o[ctx.e1.name] = IntType()
            if type(self.visit(ctx.e2, o)) == InferredType:
                o[ctx.e2.name] = IntType()
            if type(self.visit(ctx.e1, o)) == IntType and type(self.visit(ctx.e2, o)) == IntType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>.', '=.']:
            if type(self.visit(ctx.e1, o)) == InferredType:
                o[ctx.e1.name] = FloatType()
            if type(self.visit(ctx.e2, o)) == InferredType:
                o[ctx.e2.name] = FloatType()
            if type(self.visit(ctx.e1, o)) == FloatType and type(self.visit(ctx.e2, o)) == FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['&&', '||', '>b', '=b']:
            if type(self.visit(ctx.e1, o)) == InferredType:
                o[ctx.e1.name] = BoolType()
            if type(self.visit(ctx.e2, o)) == InferredType:
                o[ctx.e2.name] = BoolType()
            if type(self.visit(ctx.e1, o)) == BoolType and type(self.visit(ctx.e2, o)) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        if ctx.op == '-':
            if type(self.visit(ctx.e, o)) == InferredType:
                o[ctx.e.name] = IntType()
            if type(self.visit(ctx.e, o)) == IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ctx)

        if ctx.op == '-.':
            if type(self.visit(ctx.e, o)) == InferredType:
                o[ctx.e.name] = FloatType()
            if type(self.visit(ctx.e, o)) == FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ctx)

        elif ctx.op == '!':
            if type(self.visit(ctx.e, o)) == InferredType:
                o[ctx.e.name] = BoolType()
            if type(self.visit(ctx.e, o)) == BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ctx)

        elif ctx.op == 'i2f':
            if type(self.visit(ctx.e, o)) == InferredType:
                o[ctx.e.name] = IntType()
            if type(self.visit(ctx.e, o)) == IntType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ctx)

        elif ctx.op == 'floor':
            if type(self.visit(ctx.e, o)) == InferredType:
                o[ctx.e.name] = FloatType()
            if type(self.visit(ctx.e, o)) == FloatType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        for decl in o['varDecl']:
            if ctx.name == decl.name:
                try:
                    o[ctx.name]
                except:
                    o[ctx.name] = None
                if o[ctx.name] == None:
                    return InferredType()
                else:
                    return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
