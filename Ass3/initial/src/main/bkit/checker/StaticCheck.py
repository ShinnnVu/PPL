
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import FrozenInstanceError, dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *
from functools import reduce


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    pass


class FloatType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


class CannotInferred(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType([FloatType()], IntType())),
            Symbol("float_to_int", MType([IntType()], FloatType())),
            Symbol("int_of_string", MType([StringType()], IntType())),
            Symbol("string_of_int", MType([IntType()], StringType())),
            Symbol("float_of_string", MType([StringType()], FloatType())),
            Symbol("string_of_float", MType([FloatType()], StringType())),
            Symbol("bool_of_string", MType([StringType()], BoolType())),
            Symbol("string_of_bool", MType([BoolType()], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printStrLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def lookup(self, compare, lst, func):
        for x in lst:
            if compare == func(x):
                return x
        return None

    def raise_(self, name):  # To raise exception in lambda funcion
        raise Redeclared(Parameter(), name)

    def updateTypeInEnv(self, nameType, updateType, env):
        name = ""
        if type(nameType) == ArrayCell:
            if type(nameType.arr) == Id:
                name = nameType.arr.name
            elif type(nameType.arr) == CallExpr:
                name = nameType.arr.method.name
        elif type(nameType) == Id:
            name = nameType.name
        elif type(nameType) == CallExpr:
            name = nameType.method.name
        else:
            name = nameType

        for x in env:
            if x.name == name:
                if type(x.mtype) == MType:  # Xét cho function
                    if type(updateType) is list:
                        x.mtype.intype = updateType
                    else:
                        if type(x.mtype.restype) == ArrayType:
                            if type(updateType) != ArrayType:
                                x.mtype.restype.eletype = updateType
                            elif type(updateType) == ArrayType:
                                x.mtype.restype.eletype = updateType.eletype
                        else:
                            x.mtype.restype = updateType
                elif type(x.mtype) == ArrayType:
                    if type(updateType) != ArrayType:
                        x.mtype.eletype = updateType
                    elif type(updateType) == ArrayType:
                        x.mtype.eletype = updateType.eletype
                else:
                    x.mtype = updateType
        if (self.lookup("ParameterCheck", env, lambda x: x.name)):
            param = self.lookup(
                "ParameterCheck", env, lambda x: x.name).mtype.intype
            if param:
                for i in range(len(env[-1].mtype.intype)):
                    if type(env[-1].mtype.intype[i]) == Unknown:
                        env[-1].mtype.intype[i] = param[i].mtype
                    else:
                        param[i].mtype = env[-1].mtype.intype[i]

    def createEnv(self, in_env, out_env):
        env = [] + in_env
        for x in out_env:
            if (self.lookup(x.name, in_env, lambda x: x.name)) == None:
                env += [x]
        return env

    def updateEnv(self, local, new_env, out_env):
        symbol_update = []
        for x in new_env:
            check = self.lookup(x.name, local, lambda x: x.name)
            if check == None:
                symbol_update += [x]
        for x in out_env:
            check = self.lookup(x.name, symbol_update, lambda x: x.name)
            if check and type(x.mtype) == Unknown:
                x.mtype = check.mtype

    def traverseFunc(self, ast, o):
        func_name = ast.name.name
        check = self.lookup(func_name, o, lambda x: x.name)
        if check:
            raise Redeclared(Function(), func_name)

        paramCheck = reduce(lambda env, elem: env + [self.visit(elem, env)]
                            if self.lookup(elem.variable.name, env, lambda x: x.name) == None
                            else self.raise_(elem.variable.name), ast.param, [])

        paramType = reduce(lambda env, elem: env +
                           [self.visit(elem, env)], ast.param, [])
        param = [x.mtype for x in paramType]
        return Symbol(func_name, MType(param, Unknown()))

    def checkInfer(self, inner, o):
        for x in inner:
            check = self.lookup(x.name, o, lambda x: x.name)
            if type(check.mtype) == Unknown:
                return True
            if (type(check.mtype) == ArrayType) and (type(check.mtype.eletype) == Unknown):
                return True
        return False
    # decl : List[Decl]

    def visitProgram(self, ast, o):
        in_env = []
        in_env += o
        program_env = reduce(lambda env, ele: env + [self.visit(ele, env)] if isinstance(
            ele, VarDecl) else env + [self.traverseFunc(ele, env)], ast.decl, in_env)
        [self.visit(x, program_env)
         for x in ast.decl if isinstance(x, FuncDecl)]
        if (self.lookup('main', program_env, lambda x: x.name) == None) \
                or type((self.lookup('main', program_env, lambda x: x.name)).mtype) != MType:
            raise NoEntryPoint()

    # variable : Id
    # varDimen : List[int]
    # varInit  : Literal
    def visitVarDecl(self, ast, o):
        var_name = ast.variable.name
        check = self.lookup(var_name, o, lambda x: x.name)
        if check:
            raise Redeclared(Variable(), var_name)
        if ast.varDimen:
            symbol_type = ArrayType(ast.varDimen, self.visit(
                ast.varInit, o).eletype if ast.varInit else Unknown())
        else:
            symbol_type = self.visit(
                ast.varInit, o) if ast.varInit else Unknown()
        return Symbol(var_name, symbol_type)
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]

    def visitFuncDecl(self, ast, o):
        func_name = ast.name.name
        param = reduce(lambda env, ele: env +
                       [self.visit(ele, env)], ast.param, [])
        param_env = self.lookup(
            func_name, o, lambda x: x.name).mtype.intype
        for i in range(len(param)):
            param[i].mtype = param_env[i]
        local_var = reduce(lambda env, ele: env +
                           [self.visit(ele, env)], ast.body[0], param)
        if self.lookup(func_name, local_var, lambda x: x.name) == None:
            local_var += [Symbol("ParameterCheck", MType(param,
                                                         self.lookup(func_name, o, lambda x:x.name).mtype.restype))]
        new_env = self.createEnv(local_var, o)
        new_env.append(new_env.pop(new_env.index(
            self.lookup(func_name, new_env, lambda x: x.name))))
        [self.visit(x, new_env) for x in ast.body[1]]
        self.updateEnv(local_var, new_env, o)

    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, o):
        if ast.op in ['+', '-', '*', '\\', '%']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(ast.left, IntType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(ast.right, IntType(), o)
            if CannotInferred in [type(self.visit(ast.left, o)), type(self.visit(ast.right, o))]:
                return CannotInferred()
            if type(self.visit(ast.left, o)) == IntType and type(self.visit(ast.right, o)) == IntType:
                return IntType()
        elif ast.op in ['+.', '-.', '*.', '\\.']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(ast.left, FloatType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(ast.right, FloatType(), o)
            if CannotInferred in [type(self.visit(ast.left, o)), type(self.visit(ast.right, o))]:
                return CannotInferred()
            if type(self.visit(ast.left, o)) == FloatType and type(self.visit(ast.right, o)) == FloatType:
                return FloatType()
        elif ast.op in ['&&', '||']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(ast.left, BoolType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(ast.right, BoolType(), o)
            if CannotInferred in [type(self.visit(ast.left, o)), type(self.visit(ast.right, o))]:
                return CannotInferred()
            if type(self.visit(ast.left, o)) == BoolType and type(self.visit(ast.right, o)) == BoolType:
                return BoolType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(ast.left, IntType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(ast.right, IntType(), o)
            if CannotInferred in [type(self.visit(ast.left, o)), type(self.visit(ast.right, o))]:
                return CannotInferred()
            if type(self.visit(ast.left, o)) == IntType and type(self.visit(ast.right, o)) == IntType:
                return BoolType()
        elif ast.op in ['=/=', '<.', '>.', '<=.', '>=.']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(ast.left, FloatType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(ast.right, FloatType(), o)
            if CannotInferred in [type(self.visit(ast.left, o)), type(self.visit(ast.right, o))]:
                return CannotInferred()
            if type(self.visit(ast.left, o)) == FloatType and type(self.visit(ast.right, o)) == FloatType:
                return BoolType()
        raise TypeMismatchInExpression(ast)
    # op:str
    # body:Expr

    def visitUnaryOp(self, ast, o):
        if ast.op in ['-']:
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(ast.body, IntType(), o)
            if type(self.visit(ast.body, o)) == CannotInferred:
                return CannotInferred()
            if type(self.visit(ast.body, o)) == IntType:
                return IntType()
        elif ast.op in ['-.']:
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(ast.body, FloatType(), o)
            if type(self.visit(ast.body, o)) == CannotInferred:
                return CannotInferred()
            if type(self.visit(ast.body, o)) == FloatType:
                return FloatType()
        elif ast.op in ['!']:
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(ast.body, BoolType(), o)
            if type(self.visit(ast.body, o)) == CannotInferred:
                return CannotInferred()
            if type(self.visit(ast.body, o)) == BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    # method:Id
    # param:List[Expr]
    def visitCallExpr(self, ast, o):
        func_name = ast.method.name
        check = self.lookup(ast.method.name, o, lambda x: x.name)
        if check == None or type(check.mtype) != MType:
            raise Undeclared(Function(), func_name)
        arg = [self.visit(ele, o) for ele in ast.param]
        param = [x for x in (self.lookup(
            func_name, o, lambda x: x.name).mtype.intype)]

        if len(arg) != len(param):
            raise TypeMismatchInExpression(ast)
        for i in range(len(arg)):
            if type(arg[i]) == CannotInferred:
                return CannotInferred()
            elif type(arg[i]) == Unknown and type(param[i]) == Unknown:
                return CannotInferred()
            elif type(arg[i]) == ArrayType and type(param[i]) == ArrayType:
                if arg[i].dimen == param[i].dimen:
                    if type(arg[i].eletype) == Unknown and type(param[i]) == Unknown:
                        return CannotInferred()
                    elif type(arg[i].eletype) == Unknown:
                        self.updateTypeInEnv(ast.param[i], param[i], o)
                    elif type(param[i].eletype) == Unknown:
                        param[i].eletype = arg[i].eletype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(arg[i]) == Unknown and type(param[i]) not in [ArrayType, Unknown]:
                self.updateTypeInEnv(ast.param[i], param[i], o)
            elif type(param[i]) == Unknown and type(arg[i]) not in [ArrayType, Unknown]:
                param[i] = arg[i]
            elif type(arg[i]) == Unknown and type(param[i]) == ArrayType and isinstance(ast.param[i], CallExpr):
                if param[i].eletype != Unknown:
                    self.updateTypeInEnv(ast.param[i], param[i], o)
            elif type(arg[i]) != type(param[i]):
                raise TypeMismatchInExpression(ast)
        self.updateTypeInEnv(ast.method, param, o)
        return check.mtype.restype

    # name : str
    def visitId(self, ast, o):
        var_name = ast.name
        check = self.lookup(var_name, o, lambda x: x.name)
        if check == None or type(check.mtype) == MType:
            raise Undeclared(Identifier(), var_name)
        else:
            return check.mtype

    # arr:Expr
    # idx:List[Expr]
    def visitArrayCell(self, ast, o):
        for x in ast.idx:
            if type(self.visit(x, o)) == Unknown:
                self.updateTypeInEnv(x, IntType(), o)
            elif type(self.visit(x, o)) == CannotInferred:
                return CannotInferred()
            elif type(self.visit(x, o)) != IntType:
                raise TypeMismatchInExpression(ast)
        if type(self.visit(ast.arr, o)) == Unknown:
            if isinstance(ast.arr, CallExpr):
                return CannotInferred()
            else:
                raise TypeMismatchInExpression(ast)
        if type(self.visit(ast.arr, o)) == CannotInferred:
            return CannotInferred()
        if type(self.visit(ast.arr, o)) == ArrayType:
            if len(self.visit(ast.arr, o).dimen) == len(ast.idx):
                return self.visit(ast.arr, o).eletype
            else:
                raise TypeMismatchInExpression(ast)

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        if type(lhs) == CannotInferred or type(rhs) == CannotInferred:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) == VoidType or type(rhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) == Unknown and type(rhs) == Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) == ArrayType and type(rhs) == ArrayType:
            if lhs.dimen != rhs.dimen:
                raise TypeMismatchInStatement(ast)
            else:
                if type(lhs.eletype) == Unknown and type(rhs.eletype) == Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(lhs.eletype) == Unknown:
                    self.updateTypeInEnv(ast.lhs, rhs, o)
                elif type(rhs.eletype) == Unknown:
                    self.updateTypeInEnv(ast.rhs, lhs, o)
        elif type(lhs) == Unknown and type(rhs) == ArrayType:
            if isinstance(ast.lhs, CallExpr):
                if type(rhs.eletype) != Unknown:
                    self.updateTypeInEnv(ast.lhs, rhs, o)
                else:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(rhs) == Unknown and type(lhs) == ArrayType:
            if isinstance(ast.rhs, CallExpr):
                if type(lhs.eletype) != Unknown:
                    self.updateTypeInEnv(ast.rhs, lhs, o)
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(lhs) == Unknown:
            if type(rhs) not in [Unknown, ArrayType]:
                self.updateTypeInEnv(ast.lhs, rhs, o)
        elif type(rhs) == Unknown:
            if type(lhs) not in [Unknown, ArrayType]:
                self.updateTypeInEnv(ast.rhs, lhs, o)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)

    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]]

    def visitIf(self, ast, o):
        for x in ast.ifthenStmt:
            if type(self.visit(x[0], o)) == CannotInferred:
                raise TypeCannotBeInferred(ast)
            elif type(self.visit(x[0], o)) == Unknown:
                self.updateTypeInEnv(x[0], BoolType(), o)
            elif type(self.visit(x[0], o)) != BoolType:
                raise TypeMismatchInStatement(ast)
            local_var = reduce(lambda env, ele: env +
                               [self.visit(ele, env)], x[1], [])
            new_env = self.createEnv(local_var, o)
            [self.visit(y, new_env) for y in x[2]]
            if self.checkInfer(local_var, new_env):
                raise TypeCannotBeInferred(ast)
            self.updateEnv(local_var, new_env, o)
        if ast.elseStmt:
            local_var = reduce(lambda env, ele: env +
                               [self.visit(ele, env)], ast.elseStmt[0], [])
            new_env = self.createEnv(local_var, o)
            [self.visit(x, new_env) for x in ast.elseStmt[1]]
            if self.checkInfer(local_var, new_env):
                raise TypeCannotBeInferred(ast)
            self.updateEnv(local_var, new_env, o)

    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, o):
        if type(self.visit(ast.idx1, o)) == Unknown:
            self.updateTypeInEnv(ast.idx1, IntType(), o)
        if type(self.visit(ast.expr1, o)) == Unknown:
            self.updateTypeInEnv(ast.expr1, IntType(), o)
        if type(self.visit(ast.expr2, o)) == Unknown:
            self.updateTypeInEnv(ast.expr2, BoolType(), o)
        if type(self.visit(ast.expr3, o)) == Unknown:
            self.updateTypeInEnv(ast.expr3, IntType(), o)
        if CannotInferred in [type(self.visit(ast.idx1, o)), type(self.visit(ast.expr1, o)), type(self.visit(ast.expr2, o)), type(self.visit(ast.expr3, o))]:
            raise TypeCannotBeInferred(ast)
        if type(self.visit(ast.idx1, o)) != IntType or type(self.visit(ast.expr1, o)) != IntType or type(self.visit(ast.expr3, o)) != IntType or type(self.visit(ast.expr2, o)) != BoolType:
            raise TypeMismatchInStatement(ast)
        local_var = reduce(lambda env, ele: env +
                           [self.visit(ele, env)], ast.loop[0], [])
        new_env = self.createEnv(local_var, o)
        [self.visit(x, new_env) for x in ast.loop[1]]
        if self.checkInfer(local_var, new_env):
            raise TypeCannotBeInferred(ast)
        self.updateEnv(local_var, new_env, o)

    def visitContinue(self, ast, o):
        return None

    def visitBreak(self, ast, o):
        return None

    # expr:Expr
    def visitReturn(self, ast, o):
        func_return = o[-1].mtype.restype
        if type(func_return) == VoidType:
            if ast.expr:
                raise TypeMismatchInStatement(ast)
        if ast.expr:
            return_type = self.visit(ast.expr, o)
        else:
            return_type = VoidType()
        if type(return_type) == CannotInferred:
            raise TypeCannotBeInferred(ast)
        elif type(return_type) == Unknown and type(func_return) == Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(return_type) == ArrayType and type(func_return) == ArrayType:
            if return_type.dimen == func_return.dimen:
                if type(return_type.eletype) == Unknown and type(func_return.eletype) == Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(return_type.eletype) == Unknown:
                    self.updateTypeInEnv(ast.expr, func_return, o)
                elif type(return_type.eletype) != type(func_return.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(func_return) == Unknown:
            if type(return_type) == ArrayType:
                if type(return_type.eletype) == Unknown:
                    raise TypeCannotBeInferred(ast)
            self.updateTypeInEnv(o[-1].name, return_type, o)
        elif type(return_type) == Unknown:
            if type(func_return) != VoidType:
                self.updateTypeInEnv(ast.expr, func_return, o)
            else:
                raise TypeCannotBeInferred(ast)
        elif type(func_return) != type(return_type):
            raise TypeMismatchInStatement(ast)

    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr

    def visitDowhile(self, ast, o):
        local_var = reduce(lambda env, ele: env +
                           [self.visit(ele, env)], ast.sl[0], [])
        new_env = self.createEnv(local_var, o)
        [self.visit(x, new_env) for x in ast.sl[1]]
        if type(self.visit(ast.exp, o)) == CannotInferred:
            raise TypeCannotBeInferred(ast)
        elif type(self.visit(ast.exp, o)) == Unknown:
            self.updateTypeInEnv(ast.exp, BoolType(), o)
        elif type(self.visit(ast.exp, o)) != BoolType:
            raise TypeMismatchInStatement(ast)
        if self.checkInfer(local_var, new_env):
            raise TypeCannotBeInferred(ast)
        self.updateEnv(local_var, new_env, o)

    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, o):
        if type(self.visit(ast.exp, o)) == CannotInferred:
            raise TypeCannotBeInferred(ast)
        elif type(self.visit(ast.exp, o)) == Unknown:
            self.updateTypeInEnv(ast.exp, BoolType(), o)
        elif type(self.visit(ast.exp, o)) != BoolType:
            raise TypeMismatchInStatement(ast)
        local_var = reduce(lambda env, ele: env +
                           [self.visit(ele, env)], ast.sl[0], [])
        new_env = self.createEnv(local_var, o)
        [self.visit(x, new_env) for x in ast.sl[1]]
        if self.checkInfer(local_var, new_env):
            raise TypeCannotBeInferred(ast)
        self.updateEnv(local_var, new_env, o)

    # method:Id
    # param:List[Expr]
    def visitCallStmt(self, ast, o):
        func_name = ast.method.name
        check = self.lookup(func_name, o, lambda x: x.name)
        if check == None or type(check.mtype) != MType:
            raise Undeclared(Function(), func_name)
        return_type = check.mtype.restype
        if type(return_type) not in [VoidType, Unknown]:
            raise TypeMismatchInStatement(ast)
        if type(return_type) == CannotInferred:
            raise TypeCannotBeInferred(ast)
        param_type = check.mtype.intype
        arg_type = [self.visit(arg, o) for arg in ast.param]

        if len(param_type) != len(ast.param):
            raise TypeMismatchInStatement(ast)
        for i in range(len(param_type)):
            if (type(param_type[i]) == ArrayType and type(arg_type[i]) == ArrayType):
                if (param_type[i].dimen == arg_type[i].dimen):
                    if (type(param_type[i].eletype) == Unknown) and (type(arg_type[i].eletype) == Unknown):
                        raise TypeCannotBeInferred(ast)
                    elif (type(param_type[i].eletype) == Unknown):
                        param_type[i].eletype = arg_type[i].eletype
                        self.updateTypeInEnv(ast.method, param_type, o)
                    elif (type(arg_type[i].eletype) == Unknown):
                        self.updateTypeInEnv(ast.param[i], param_type[i], o)
                    elif (type(param_type[i].eletype) != type(arg_type[i].eletype)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif (type(param_type[i]) == ArrayType and type(arg_type[i]) == Unknown):
                if (type(param_type[i].eletype) != Unknown):
                    self.updateTypeInEnv(ast.param[i], param_type[i], o)
                else:
                    raise TypeMismatchInStatement(ast)
            elif (type(arg_type[i]) == ArrayType and type(param_type[i]) == Unknown):
                if (type(arg_type[i].eletype) != Unknown):
                    param_type[i] = arg_type[i]
                    self.updateTypeInEnv(ast.method, param_type, o)
                else:
                    raise TypeMismatchInStatement(ast)

            elif (type(param_type[i]) == Unknown) and (type(arg_type[i]) == Unknown):
                raise TypeCannotBeInferred(ast)
            elif (type(param_type[i]) == Unknown) and (type(arg_type[i]) != ArrayType):
                param_type[i] = arg_type[i]
                self.updateTypeInEnv(ast.method, param_type, o)
                # self.updateTypeInEnv(ast.param[i], arg_type[i],o)
            elif (type(arg_type[i]) == Unknown) and (type(param_type[i]) != ArrayType):
                self.updateTypeInEnv(ast.param[i], param_type[i], o)
            elif (type(param_type[i]) != type(arg_type[i])):
                raise TypeMismatchInStatement(ast)
        # self.updateTypeInEnv(ast.method,param_type,o)
        self.updateTypeInEnv(ast.method, VoidType(), o)

    # value:int

    def visitIntLiteral(self, ast, o):
        return IntType()

    # value:float
    def visitFloatLiteral(self, ast, o):
        return FloatType()

    # value:bool
    def visitBooleanLiteral(self, ast, o):
        return BoolType()

    # value:str
    def visitStringLiteral(self, ast, o):
        return StringType()

    # value:List[Literal]
    def visitArrayLiteral(self, ast, o):
        array = ast.value
        dimen = []
        temp = None
        while isinstance(array, list):
            dimen += [len(array)]
            temp = array[0] if array else None
            array = array[0].value if array else None
        eleType = self.visit(temp, []) if temp else Unknown()
        return ArrayType(dimen, eleType)
