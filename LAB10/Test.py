def visitIntLiteral(self, ctx, o):
    code = self.emit.emitPUSHICONST(ctx.value, o.frame)
    return code, IntType()


def visitFloatLiteral(self, ctx, o):
    code = self.emit.emitPUSHFCONST(ctx.value, o.frame)
    return code, FloatType()

    def visitBinExpr(self, ctx, o):
        e1, e1type = self.visit(ctx.e1, o)
        e2, e2type = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*', '/']:
            if ctx.op in ['+', '-']:
                code = e1 + e2 + \
                    self.emit.emitADDOP(ctx.op, IntType(), o.frame)
            elif ctx.op in ['*', '/']:
                code = e1 + e2 + \
                    self.emit.emitMULOP(ctx.op, IntType(), o.frame)
            return code, IntType()
        else:
            if ctx.op in ['+.', '-.']:
                code = e1 + e2 + \
                    self.emit.emitADDOP(ctx.op[0], FloatType(), o.frame)
            elif ctx.op in ['*.', '/.']:
                code = e1 + e2 + \
                    self.emit.emitMULOP(ctx.op[0], FloatType(), o.frame)
            return code, FloatType()

    def visitBinExpr(self, ctx, o):
        e1, e1type = self.visit(ctx.e1, o)
        e2, e2type = self.visit(ctx.e2, o)
        if FloatType in [type(e1type), type(e2type)] or ctx.op == '/':
            returnType = FloatType()
        else:
            returnType = IntType()

        if type(e1type) == IntType and type(returnType) == FloatType:
            e1 = e1 + self.emit.emitI2F(o.frame)
        if type(e2type) == IntType and type(returnType) == FloatType:
            e2 = e2 + self.emit.emitI2F(o.frame)
        if ctx.op in ['+', '-']:
            code = e1 + e2 + self.emit.emitADDOP(ctx.op, returnType, o.frame)
            return code, returnType
        elif ctx.op in ['*', '/']:
            code = e1 + e2 + self.emit.emitMULOP(ctx.op, returnType, o.frame)
            return code, returnType
        else:
            code = e1 + e2 + self.emit.emitREOP(ctx.op, returnType, o.frame)
            return code, BoolType()

    def visitId(self, ctx, o):
        for x in o.sym:
            if ctx.name == x.name:
                if type(x.value.value) == int:
                    code = self.emit.emitREADVAR(
                        x.name, x.mtype, x.value.value, o.frame)
                    return code, x.mtype
                elif type(x.value.value) == str:
                    code = self.emit.emitGETSTATIC(
                        self.className + "/" + x.name, x.mtype, o.frame)
                    return code, x.mtype
