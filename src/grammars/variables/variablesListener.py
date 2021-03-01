# Generated from src/grammars/variables/variables.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .variablesParser import variablesParser
else:
    from variablesParser import variablesParser

# This class defines a complete listener for a parse tree produced by variablesParser.
class variablesListener(ParseTreeListener):

    # Enter a parse tree produced by variablesParser#Program.
    def enterProgram(self, ctx:variablesParser.ProgramContext):
        pass

    # Exit a parse tree produced by variablesParser#Program.
    def exitProgram(self, ctx:variablesParser.ProgramContext):
        pass


    # Enter a parse tree produced by variablesParser#DefinitionStatement.
    def enterDefinitionStatement(self, ctx:variablesParser.DefinitionStatementContext):
        pass

    # Exit a parse tree produced by variablesParser#DefinitionStatement.
    def exitDefinitionStatement(self, ctx:variablesParser.DefinitionStatementContext):
        pass


    # Enter a parse tree produced by variablesParser#DeclarationStatement.
    def enterDeclarationStatement(self, ctx:variablesParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by variablesParser#DeclarationStatement.
    def exitDeclarationStatement(self, ctx:variablesParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by variablesParser#AssignmentStatement.
    def enterAssignmentStatement(self, ctx:variablesParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by variablesParser#AssignmentStatement.
    def exitAssignmentStatement(self, ctx:variablesParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by variablesParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:variablesParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by variablesParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:variablesParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by variablesParser#Identifier.
    def enterIdentifier(self, ctx:variablesParser.IdentifierContext):
        pass

    # Exit a parse tree produced by variablesParser#Identifier.
    def exitIdentifier(self, ctx:variablesParser.IdentifierContext):
        pass


    # Enter a parse tree produced by variablesParser#Brackets.
    def enterBrackets(self, ctx:variablesParser.BracketsContext):
        pass

    # Exit a parse tree produced by variablesParser#Brackets.
    def exitBrackets(self, ctx:variablesParser.BracketsContext):
        pass


    # Enter a parse tree produced by variablesParser#UnaryOpPointer.
    def enterUnaryOpPointer(self, ctx:variablesParser.UnaryOpPointerContext):
        pass

    # Exit a parse tree produced by variablesParser#UnaryOpPointer.
    def exitUnaryOpPointer(self, ctx:variablesParser.UnaryOpPointerContext):
        pass


    # Enter a parse tree produced by variablesParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:variablesParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by variablesParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:variablesParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by variablesParser#UnaryOpIdentifier.
    def enterUnaryOpIdentifier(self, ctx:variablesParser.UnaryOpIdentifierContext):
        pass

    # Exit a parse tree produced by variablesParser#UnaryOpIdentifier.
    def exitUnaryOpIdentifier(self, ctx:variablesParser.UnaryOpIdentifierContext):
        pass


    # Enter a parse tree produced by variablesParser#UnaryOpBoolean.
    def enterUnaryOpBoolean(self, ctx:variablesParser.UnaryOpBooleanContext):
        pass

    # Exit a parse tree produced by variablesParser#UnaryOpBoolean.
    def exitUnaryOpBoolean(self, ctx:variablesParser.UnaryOpBooleanContext):
        pass


    # Enter a parse tree produced by variablesParser#BinaryOp.
    def enterBinaryOp(self, ctx:variablesParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by variablesParser#BinaryOp.
    def exitBinaryOp(self, ctx:variablesParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by variablesParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:variablesParser.BinaryOpBooleanContext):
        pass

    # Exit a parse tree produced by variablesParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:variablesParser.BinaryOpBooleanContext):
        pass


    # Enter a parse tree produced by variablesParser#type_specifier.
    def enterType_specifier(self, ctx:variablesParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by variablesParser#type_specifier.
    def exitType_specifier(self, ctx:variablesParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by variablesParser#Float.
    def enterFloat(self, ctx:variablesParser.FloatContext):
        pass

    # Exit a parse tree produced by variablesParser#Float.
    def exitFloat(self, ctx:variablesParser.FloatContext):
        pass


    # Enter a parse tree produced by variablesParser#Integer.
    def enterInteger(self, ctx:variablesParser.IntegerContext):
        pass

    # Exit a parse tree produced by variablesParser#Integer.
    def exitInteger(self, ctx:variablesParser.IntegerContext):
        pass


    # Enter a parse tree produced by variablesParser#String.
    def enterString(self, ctx:variablesParser.StringContext):
        pass

    # Exit a parse tree produced by variablesParser#String.
    def exitString(self, ctx:variablesParser.StringContext):
        pass


    # Enter a parse tree produced by variablesParser#Character.
    def enterCharacter(self, ctx:variablesParser.CharacterContext):
        pass

    # Exit a parse tree produced by variablesParser#Character.
    def exitCharacter(self, ctx:variablesParser.CharacterContext):
        pass


    # Enter a parse tree produced by variablesParser#declaration.
    def enterDeclaration(self, ctx:variablesParser.DeclarationContext):
        pass

    # Exit a parse tree produced by variablesParser#declaration.
    def exitDeclaration(self, ctx:variablesParser.DeclarationContext):
        pass


    # Enter a parse tree produced by variablesParser#definition.
    def enterDefinition(self, ctx:variablesParser.DefinitionContext):
        pass

    # Exit a parse tree produced by variablesParser#definition.
    def exitDefinition(self, ctx:variablesParser.DefinitionContext):
        pass


    # Enter a parse tree produced by variablesParser#assignment.
    def enterAssignment(self, ctx:variablesParser.AssignmentContext):
        pass

    # Exit a parse tree produced by variablesParser#assignment.
    def exitAssignment(self, ctx:variablesParser.AssignmentContext):
        pass



del variablesParser