from functools import reduce
from abc import ABCMeta


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class InferredType(Type):
    pass


class StaticCheck(Visitor):

    def updateType(self, name, new_type, o):
        if name in o[0]:
            o[0][name] = new_type
        else:
            o[1][name] = new_type

        return o

    def getType(self, name, o):
        return o[0][name] if name in o[0] else o[1][name]

    def visitProgram(self, ctx: Program, o):
        reduce(lambda env, ele: self.visit(
            ele, env), ctx.decl+ctx.stmts, ({}, {}))

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        else:
            o[0][ctx.name] = InferredType()
        return o

    def visitAssign(self, ctx: Assign, o):

        if type(self.visit(ctx.lhs, o)) == InferredType and type(self.visit(ctx.rhs, o)) == InferredType:
            raise TypeCannotBeInferred(ctx)
        elif type(self.visit(ctx.lhs, o)) == InferredType and type(self.visit(ctx.rhs, o)) != InferredType:
            o[0][ctx.lhs.name] = self.visit(ctx.rhs, o)
        elif type(self.visit(ctx.rhs, o)) == InferredType and type(self.visit(ctx.lhs, o)) != InferredType:
            o[0][ctx.rhs.name] = self.visit(ctx.lhs, o)
        if not(type(self.visit(ctx.lhs, o)) == type(self.visit(ctx.rhs, o))):
            raise TypeMismatchInStatement(ctx)
        return o

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
        if ctx.name in o[0]:
            raise Redeclared(ctx)

        outer_env = o[1].copy()
        outer_env.update(o[0])

        new_env = ({}, outer_env)
        reduce(lambda env, elem: self.visit(elem, env),
               ctx.param + ctx.local + ctx.stmts, new_env)

        param_type = [self.getType(var.name, new_env) for var in ctx.param]
        o[0][ctx.name] = param_type

        for name in outer_env:
            if name in new_env[0]:
                continue

            if (not self.getType(name, o)) and (outer_env[name]):
                self.updateType(name, outer_env[name], o)

        return o

    def visitCallStmt(self, ctx: CallStmt, o):
        # name:str,args:List[Exp]
        if (ctx.name not in o[0]):
            raise UndeclaredIdentifier(ctx.name)

        param_type = self.getType(ctx.name, o)
        arg_type = [self.visit(arg, o) for arg in ctx.args]

        if (type(param_type) is not list) or (len(arg_type) != len(param_type)):
            raise TypeMismatchInStatement(ctx)

        for i in range(len(arg_type)):
            if (type(param_type[i]) == InferredType) and (type(arg_type[i]) == InferredType):
                raise TypeCannotBeInferred(ctx)
            elif type(param_type[i]) == InferredType:
                param_type[i] = arg_type[i]
            elif (type(arg_type[i]) == InferredType):
                self.updateType(ctx.args[i].name, param_type[i], o)
            elif type(arg_type[i]) != type(param_type[i]):
                raise TypeMismatchInStatement(ctx)

        self.updateType(ctx.name, param_type, o)

        return o

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx: FloatLit, o):
        return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o):
        return BoolType()

    def visitId(self, ctx: Id, o):
        if ctx.name not in o[0] and ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        return o[0][ctx.name] if ctx.name in o[0] else o[1][ctx.name]
