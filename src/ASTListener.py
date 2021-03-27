from grammars.C.CListener import CListener
from grammars.C.CParser import CParser
from ASTNode import *
from SymbolTable import SymbolTable
from utils import Counter

class ASTListener(CListener):
    def __init__(self):
        self.curr_node = None
        self.counter = Counter()
        
    def enterProgram(self, ctx:CParser.ProgramContext):
        assert self.curr_node is None
        self.curr_node = ProgNode(self.counter.incr())

    # Exit a parse tree produced by variablesParser#Program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass

    # Enter a parse tree produced by variablesParser#Integer.
    def enterInteger(self, ctx:CParser.IntegerContext):
        self.curr_node.add_child(LiteralNode(int(ctx.getText()), "int", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        
    # Exit a parse tree produced by variablesParser#Integer.
    def exitInteger(self, ctx:CParser.IntegerContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Float.
    def enterFloat(self, ctx:CParser.FloatContext):
        self.curr_node.add_child(LiteralNode(float(ctx.getText()), "float", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Float.
    def exitFloat(self, ctx:CParser.FloatContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#String.
    def enterString(self, ctx:CParser.StringContext):
        self.curr_node.add_child(LiteralNode(ctx.getText(), "string", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#String.
    def exitString(self, ctx:CParser.StringContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Character.
    def enterCharacter(self, ctx:CParser.CharacterContext):
        self.curr_node.add_child(LiteralNode(ctx.getText()[0], "char", self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Character.
    def exitCharacter(self, ctx:CParser.CharacterContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOp(self, ctx:CParser.UnaryOpContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOp(self, ctx:CParser.UnaryOpContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText() + 'x', self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        self.curr_node.add_child(UnaryOperationNode('x' + ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(0).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOp.
    def enterBinaryOp(self, ctx:CParser.BinaryOpContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOp.
    def exitBinaryOp(self, ctx:CParser.BinaryOpContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        self.curr_node.add_child(DefinitionNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by variablesParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        self.curr_node.add_child(AssignmentNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(0).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        self.curr_node.add_child(DeclarationNode(self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()))

    # Exit a parse tree produced by variablesParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        self.curr_node.children[0].type = ctx.getChild(0).getText()
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Identifier.
    def enterIdentifier(self, ctx:CParser.IdentifierContext):
        self.curr_node.add_child(IdentifierNode(ctx.getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Identifier.
    def exitIdentifier(self, ctx:CParser.IdentifierContext):
        self.curr_node = self.curr_node.parent