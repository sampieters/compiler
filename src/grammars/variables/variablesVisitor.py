# Generated from src/grammars/variables/variables.g4 by ANTLR 4.9.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by variablesParser.

class variablesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#DefinitionStatement.
    def visitDefinitionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOp.
    def visitUnaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Brackets.
    def visitBrackets(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpIdentifierSuffix.
    def visitUnaryOpIdentifierSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpPointer.
    def visitUnaryOpPointer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#LiteralExpr.
    def visitLiteralExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpIdentifierPrefix.
    def visitUnaryOpIdentifierPrefix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#BinaryOp.
    def visitBinaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#type_specifier.
    def visitType_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Float.
    def visitFloat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#String.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Character.
    def visitCharacter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#definition.
    def visitDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#PrintF.
    def visitPrintF(self, ctx):
        return self.visitChildren(ctx)


