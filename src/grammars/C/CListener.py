# Generated from ./src/grammars/C/C.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#Program.
    def enterProgram(self, ctx:CParser.ProgramContext):
        pass

    # Exit a parse tree produced by CParser#Program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass


    # Enter a parse tree produced by CParser#DefinitionStatement.
    def enterDefinitionStatement(self, ctx:CParser.DefinitionStatementContext):
        pass

    # Exit a parse tree produced by CParser#DefinitionStatement.
    def exitDefinitionStatement(self, ctx:CParser.DefinitionStatementContext):
        pass


    # Enter a parse tree produced by CParser#DeclarationStatement.
    def enterDeclarationStatement(self, ctx:CParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by CParser#DeclarationStatement.
    def exitDeclarationStatement(self, ctx:CParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by CParser#AssignmentStatement.
    def enterAssignmentStatement(self, ctx:CParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by CParser#AssignmentStatement.
    def exitAssignmentStatement(self, ctx:CParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by CParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:CParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CParser#BreakStatement.
    def enterBreakStatement(self, ctx:CParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by CParser#BreakStatement.
    def exitBreakStatement(self, ctx:CParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by CParser#ContinueStatement.
    def enterContinueStatement(self, ctx:CParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by CParser#ContinueStatement.
    def exitContinueStatement(self, ctx:CParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by CParser#ForStatement.
    def enterForStatement(self, ctx:CParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CParser#ForStatement.
    def exitForStatement(self, ctx:CParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CParser#WhileStatement.
    def enterWhileStatement(self, ctx:CParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CParser#WhileStatement.
    def exitWhileStatement(self, ctx:CParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CParser#IfStatement.
    def enterIfStatement(self, ctx:CParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CParser#IfStatement.
    def exitIfStatement(self, ctx:CParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CParser#SwitchStatement.
    def enterSwitchStatement(self, ctx:CParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by CParser#SwitchStatement.
    def exitSwitchStatement(self, ctx:CParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by CParser#FunctionDeclarationStatement.
    def enterFunctionDeclarationStatement(self, ctx:CParser.FunctionDeclarationStatementContext):
        pass

    # Exit a parse tree produced by CParser#FunctionDeclarationStatement.
    def exitFunctionDeclarationStatement(self, ctx:CParser.FunctionDeclarationStatementContext):
        pass


    # Enter a parse tree produced by CParser#FunctionDefinitionStatement.
    def enterFunctionDefinitionStatement(self, ctx:CParser.FunctionDefinitionStatementContext):
        pass

    # Exit a parse tree produced by CParser#FunctionDefinitionStatement.
    def exitFunctionDefinitionStatement(self, ctx:CParser.FunctionDefinitionStatementContext):
        pass


    # Enter a parse tree produced by CParser#ReturnStatement.
    def enterReturnStatement(self, ctx:CParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CParser#ReturnStatement.
    def exitReturnStatement(self, ctx:CParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CParser#EmptyReturnStatement.
    def enterEmptyReturnStatement(self, ctx:CParser.EmptyReturnStatementContext):
        pass

    # Exit a parse tree produced by CParser#EmptyReturnStatement.
    def exitEmptyReturnStatement(self, ctx:CParser.EmptyReturnStatementContext):
        pass


    # Enter a parse tree produced by CParser#EmptyStatement.
    def enterEmptyStatement(self, ctx:CParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by CParser#EmptyStatement.
    def exitEmptyStatement(self, ctx:CParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by CParser#UnaryOp.
    def enterUnaryOp(self, ctx:CParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by CParser#UnaryOp.
    def exitUnaryOp(self, ctx:CParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by CParser#Identifier.
    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CParser#Identifier.
    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CParser#Brackets.
    def enterBrackets(self, ctx:CParser.BracketsContext):
        pass

    # Exit a parse tree produced by CParser#Brackets.
    def exitBrackets(self, ctx:CParser.BracketsContext):
        pass


    # Enter a parse tree produced by CParser#UnaryOpIdentifierSuffix.
    def enterUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        pass

    # Exit a parse tree produced by CParser#UnaryOpIdentifierSuffix.
    def exitUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        pass


    # Enter a parse tree produced by CParser#UnaryOpPointer.
    def enterUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        pass

    # Exit a parse tree produced by CParser#UnaryOpPointer.
    def exitUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        pass


    # Enter a parse tree produced by CParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:CParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by CParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:CParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by CParser#FunctionCall.
    def enterFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CParser#FunctionCall.
    def exitFunctionCall(self, ctx:CParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CParser#UnaryOpBoolean.
    def enterUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        pass

    # Exit a parse tree produced by CParser#UnaryOpBoolean.
    def exitUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        pass


    # Enter a parse tree produced by CParser#UnaryOpIdentifierPrefix.
    def enterUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        pass

    # Exit a parse tree produced by CParser#UnaryOpIdentifierPrefix.
    def exitUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        pass


    # Enter a parse tree produced by CParser#BinaryOp.
    def enterBinaryOp(self, ctx:CParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by CParser#BinaryOp.
    def exitBinaryOp(self, ctx:CParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by CParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        pass

    # Exit a parse tree produced by CParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        pass


    # Enter a parse tree produced by CParser#scope.
    def enterScope(self, ctx:CParser.ScopeContext):
        pass

    # Exit a parse tree produced by CParser#scope.
    def exitScope(self, ctx:CParser.ScopeContext):
        pass


    # Enter a parse tree produced by CParser#for_stat.
    def enterFor_stat(self, ctx:CParser.For_statContext):
        pass

    # Exit a parse tree produced by CParser#for_stat.
    def exitFor_stat(self, ctx:CParser.For_statContext):
        pass


    # Enter a parse tree produced by CParser#while_stat.
    def enterWhile_stat(self, ctx:CParser.While_statContext):
        pass

    # Exit a parse tree produced by CParser#while_stat.
    def exitWhile_stat(self, ctx:CParser.While_statContext):
        pass


    # Enter a parse tree produced by CParser#if_stat.
    def enterIf_stat(self, ctx:CParser.If_statContext):
        pass

    # Exit a parse tree produced by CParser#if_stat.
    def exitIf_stat(self, ctx:CParser.If_statContext):
        pass


    # Enter a parse tree produced by CParser#elif_stat.
    def enterElif_stat(self, ctx:CParser.Elif_statContext):
        pass

    # Exit a parse tree produced by CParser#elif_stat.
    def exitElif_stat(self, ctx:CParser.Elif_statContext):
        pass


    # Enter a parse tree produced by CParser#else_stat.
    def enterElse_stat(self, ctx:CParser.Else_statContext):
        pass

    # Exit a parse tree produced by CParser#else_stat.
    def exitElse_stat(self, ctx:CParser.Else_statContext):
        pass


    # Enter a parse tree produced by CParser#switch_stat.
    def enterSwitch_stat(self, ctx:CParser.Switch_statContext):
        pass

    # Exit a parse tree produced by CParser#switch_stat.
    def exitSwitch_stat(self, ctx:CParser.Switch_statContext):
        pass


    # Enter a parse tree produced by CParser#type_specifier.
    def enterType_specifier(self, ctx:CParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by CParser#type_specifier.
    def exitType_specifier(self, ctx:CParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by CParser#Float.
    def enterFloat(self, ctx:CParser.FloatContext):
        pass

    # Exit a parse tree produced by CParser#Float.
    def exitFloat(self, ctx:CParser.FloatContext):
        pass


    # Enter a parse tree produced by CParser#Integer.
    def enterInteger(self, ctx:CParser.IntegerContext):
        pass

    # Exit a parse tree produced by CParser#Integer.
    def exitInteger(self, ctx:CParser.IntegerContext):
        pass


    # Enter a parse tree produced by CParser#String.
    def enterString(self, ctx:CParser.StringContext):
        pass

    # Exit a parse tree produced by CParser#String.
    def exitString(self, ctx:CParser.StringContext):
        pass


    # Enter a parse tree produced by CParser#Character.
    def enterCharacter(self, ctx:CParser.CharacterContext):
        pass

    # Exit a parse tree produced by CParser#Character.
    def exitCharacter(self, ctx:CParser.CharacterContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#FunctionDeclaration.
    def enterFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#FunctionDeclaration.
    def exitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CParser#definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        pass

    # Exit a parse tree produced by CParser#definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
        pass


    # Enter a parse tree produced by CParser#function_definition.
    def enterFunction_definition(self, ctx:CParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by CParser#function_definition.
    def exitFunction_definition(self, ctx:CParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CParser#function_call.
    def enterFunction_call(self, ctx:CParser.Function_callContext):
        pass

    # Exit a parse tree produced by CParser#function_call.
    def exitFunction_call(self, ctx:CParser.Function_callContext):
        pass


    # Enter a parse tree produced by CParser#arg_list.
    def enterArg_list(self, ctx:CParser.Arg_listContext):
        pass

    # Exit a parse tree produced by CParser#arg_list.
    def exitArg_list(self, ctx:CParser.Arg_listContext):
        pass


    # Enter a parse tree produced by CParser#call_list.
    def enterCall_list(self, ctx:CParser.Call_listContext):
        pass

    # Exit a parse tree produced by CParser#call_list.
    def exitCall_list(self, ctx:CParser.Call_listContext):
        pass



del CParser