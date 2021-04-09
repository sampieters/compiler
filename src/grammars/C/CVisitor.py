# Generated from src/grammars/C/C.g4 by ANTLR 4.9.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#Program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#DefinitionStatement.
    def visitDefinitionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BreakStatement.
    def visitBreakStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ContinueStatement.
    def visitContinueStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ForStatement.
    def visitForStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#IfStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#SwitchStatement.
    def visitSwitchStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionDeclarationStatement.
    def visitFunctionDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionDefinitionStatement.
    def visitFunctionDefinitionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ReturnStatement.
    def visitReturnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#EmptyReturnStatement.
    def visitEmptyReturnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#EmptyStatement.
    def visitEmptyStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOp.
    def visitUnaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Brackets.
    def visitBrackets(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpIdentifierSuffix.
    def visitUnaryOpIdentifierSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpPointer.
    def visitUnaryOpPointer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#LiteralExpr.
    def visitLiteralExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionCall.
    def visitFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpIdentifierPrefix.
    def visitUnaryOpIdentifierPrefix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BinaryOp.
    def visitBinaryOp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#scope.
    def visitScope(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#for_stat.
    def visitFor_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#while_stat.
    def visitWhile_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#if_stat.
    def visitIf_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#elif_stat.
    def visitElif_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#else_stat.
    def visitElse_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#switch_stat.
    def visitSwitch_stat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type_specifier.
    def visitType_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Float.
    def visitFloat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Integer.
    def visitInteger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#String.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Character.
    def visitCharacter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_declaration.
    def visitFunction_declaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#definition.
    def visitDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_definition.
    def visitFunction_definition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_call.
    def visitFunction_call(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#arg_list.
    def visitArg_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#call_list.
    def visitCall_list(self, ctx):
        return self.visitChildren(ctx)


