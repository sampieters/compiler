# Generated from src/grammars/loops/loops.g4 by ANTLR 4.9.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by loopsParser.

class loopsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by loopsParser#Program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#DefinitionStatement.
    def visitDefinitionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#UnaryOp.
    def visitUnaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#Identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#Brackets.
    def visitBrackets(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#UnaryOpIdentifierSuffix.
    def visitUnaryOpIdentifierSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#UnaryOpPointer.
    def visitUnaryOpPointer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#LiteralExpr.
    def visitLiteralExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#UnaryOpIdentifierPrefix.
    def visitUnaryOpIdentifierPrefix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#BinaryOp.
    def visitBinaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#loop_stat.
    def visitLoop_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#increment.
    def visitIncrement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#block_stat.
    def visitBlock_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#type_specifier.
    def visitType_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#Float.
    def visitFloat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#Integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#String.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#Character.
    def visitCharacter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#definition.
    def visitDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by loopsParser#PrintF.
    def visitPrintF(self, ctx):
        return self.visitChildren(ctx)


