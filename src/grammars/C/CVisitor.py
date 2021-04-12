# Generated from src/grammars/C/C.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#Program.
    def visitProgram(self, ctx:CParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#DefinitionStatement.
    def visitDefinitionStatement(self, ctx:CParser.DefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx:CParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx:CParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BreakStatement.
    def visitBreakStatement(self, ctx:CParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ContinueStatement.
    def visitContinueStatement(self, ctx:CParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ForStatement.
    def visitForStatement(self, ctx:CParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#WhileStatement.
    def visitWhileStatement(self, ctx:CParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#IfStatement.
    def visitIfStatement(self, ctx:CParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#SwitchStatement.
    def visitSwitchStatement(self, ctx:CParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionDeclarationStatement.
    def visitFunctionDeclarationStatement(self, ctx:CParser.FunctionDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionDefinitionStatement.
    def visitFunctionDefinitionStatement(self, ctx:CParser.FunctionDefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#ReturnStatement.
    def visitReturnStatement(self, ctx:CParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#EmptyStatement.
    def visitEmptyStatement(self, ctx:CParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOp.
    def visitUnaryOp(self, ctx:CParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Identifier.
    def visitIdentifier(self, ctx:CParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Brackets.
    def visitBrackets(self, ctx:CParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpIdentifierSuffix.
    def visitUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpPointer.
    def visitUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:CParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionCall.
    def visitFunctionCall(self, ctx:CParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpBoolean.
    def visitUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#UnaryOpIdentifierPrefix.
    def visitUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BinaryOp.
    def visitBinaryOp(self, ctx:CParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#BinaryOpBoolean.
    def visitBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#scope.
    def visitScope(self, ctx:CParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#for_stat.
    def visitFor_stat(self, ctx:CParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#while_stat.
    def visitWhile_stat(self, ctx:CParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#if_stat.
    def visitIf_stat(self, ctx:CParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#elif_stat.
    def visitElif_stat(self, ctx:CParser.Elif_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#else_stat.
    def visitElse_stat(self, ctx:CParser.Else_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#switch_stat.
    def visitSwitch_stat(self, ctx:CParser.Switch_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type_specifier.
    def visitType_specifier(self, ctx:CParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Float.
    def visitFloat(self, ctx:CParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Integer.
    def visitInteger(self, ctx:CParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#String.
    def visitString(self, ctx:CParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#Character.
    def visitCharacter(self, ctx:CParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#FunctionDeclaration.
    def visitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#definition.
    def visitDefinition(self, ctx:CParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_definition.
    def visitFunction_definition(self, ctx:CParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment.
    def visitAssignment(self, ctx:CParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#function_call.
    def visitFunction_call(self, ctx:CParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#arg_list.
    def visitArg_list(self, ctx:CParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#call_list.
    def visitCall_list(self, ctx:CParser.Call_listContext):
        return self.visitChildren(ctx)



del CParser