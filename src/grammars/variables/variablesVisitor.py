# Generated from src/grammars/variables/variables.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .variablesParser import variablesParser
else:
    from variablesParser import variablesParser

# This class defines a complete generic visitor for a parse tree produced by variablesParser.

class variablesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx:variablesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#DefinitionStatement.
    def visitDefinitionStatement(self, ctx:variablesParser.DefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx:variablesParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx:variablesParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:variablesParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOp.
    def visitUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Identifier.
    def visitIdentifier(self, ctx:variablesParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Brackets.
    def visitBrackets(self, ctx:variablesParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpPointer.
    def visitUnaryOpPointer(self, ctx:variablesParser.UnaryOpPointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:variablesParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpIdentifier.
    def visitUnaryOpIdentifier(self, ctx:variablesParser.UnaryOpIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx:variablesParser.UnaryOpBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#BinaryOp.
    def visitBinaryOp(self, ctx:variablesParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx:variablesParser.BinaryOpBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#type_specifier.
    def visitType_specifier(self, ctx:variablesParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Float.
    def visitFloat(self, ctx:variablesParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Integer.
    def visitInteger(self, ctx:variablesParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#String.
    def visitString(self, ctx:variablesParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#Character.
    def visitCharacter(self, ctx:variablesParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#declaration.
    def visitDeclaration(self, ctx:variablesParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#definition.
    def visitDefinition(self, ctx:variablesParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by variablesParser#assignment.
    def visitAssignment(self, ctx:variablesParser.AssignmentContext):
        return self.visitChildren(ctx)



del variablesParser