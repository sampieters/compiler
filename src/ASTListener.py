from grammars.variables.variablesListener import variablesListener
from grammars.variables.variablesParser import variablesParser
from ASTNode import *
from SymbolTable import SymbolTable
from utils import Counter

class ASTListener(variablesListener):
    def __init__(self):
        self.curr_node = None
        self.counter = Counter()
        
    def enterProgram(self, ctx:variablesParser.ProgramContext):
        assert self.curr_node is None
        self.curr_node = ProgNode(self.counter.incr())

    # Exit a parse tree produced by variablesParser#Program.
    def exitProgram(self, ctx:variablesParser.ProgramContext):
        pass

    # Enter a parse tree produced by variablesParser#Integer.
    def enterInteger(self, ctx:variablesParser.IntegerContext):
        self.curr_node.add_child(LiteralNode(int(ctx.getText()), "int", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        
    # Exit a parse tree produced by variablesParser#Integer.
    def exitInteger(self, ctx:variablesParser.IntegerContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Float.
    def enterFloat(self, ctx:variablesParser.FloatContext):
        self.curr_node.add_child(LiteralNode(float(ctx.getText()), "float", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Float.
    def exitFloat(self, ctx:variablesParser.FloatContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#String.
    def enterString(self, ctx:variablesParser.StringContext):
        self.curr_node.add_child(LiteralNode(ctx.getText(), "string", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#String.
    def exitString(self, ctx:variablesParser.StringContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Character.
    def enterCharacter(self, ctx:variablesParser.CharacterContext):
        self.curr_node.add_child(LiteralNode(ctx.getText()[0], "char", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Character.
    def exitCharacter(self, ctx:variablesParser.CharacterContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierPrefix(self, ctx:variablesParser.UnaryOpIdentifierPrefixContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText() + 'x', self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierPrefix(self, ctx:variablesParser.UnaryOpIdentifierPrefixContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierSuffix(self, ctx:variablesParser.UnaryOpIdentifierSuffixContext):
        self.curr_node.add_child(UnaryOperationNode('x' + ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(0).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierSuffix(self, ctx:variablesParser.UnaryOpIdentifierSuffixContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOp.
    def enterBinaryOp(self, ctx:variablesParser.BinaryOpContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOp.
    def exitBinaryOp(self, ctx:variablesParser.BinaryOpContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:variablesParser.BinaryOpBooleanContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:variablesParser.BinaryOpBooleanContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#definition.
    def enterDefinition(self, ctx:variablesParser.DefinitionContext):
        self.curr_node.add_child(DefinitionNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#definition.
    def exitDefinition(self, ctx:variablesParser.DefinitionContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by variablesParser#assignment.
    def enterAssignment(self, ctx:variablesParser.AssignmentContext):
        self.curr_node.add_child(AssignmentNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(0).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#assignment.
    def exitAssignment(self, ctx:variablesParser.AssignmentContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#declaration.
    def enterDeclaration(self, ctx:variablesParser.DeclarationContext):
        self.curr_node.add_child(DeclarationNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#declaration.
    def exitDeclaration(self, ctx:variablesParser.DeclarationContext):
        self.curr_node.children[0].type = ctx.getChild(0).getText()
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Identifier.
    def enterIdentifier(self, ctx:variablesParser.IdentifierContext):
        self.curr_node.add_child(IdentifierNode(ctx.getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Identifier.
    def exitIdentifier(self, ctx:variablesParser.IdentifierContext):
        self.curr_node = self.curr_node.parent