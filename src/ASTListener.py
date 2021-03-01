from grammars.variables.variablesListener import variablesListener
from grammars.variables.variablesParser import variablesParser
from ASTNode import *
from utils import Counter

class ASTListener(variablesListener):
    def __init__(self):
        self.curr_node = None
        self.counter = Counter()
        
    def enterProgram(self, ctx:variablesParser.ProgramContext):
        assert self.curr_node is None
        self.curr_node = ASTNode(self.counter.incr())

    # Exit a parse tree produced by variablesParser#Program.
    def exitProgram(self, ctx:variablesParser.ProgramContext):
        pass

    # Enter a parse tree produced by variablesParser#Integer.
    def enterInteger(self, ctx:variablesParser.IntegerContext):
        self.curr_node.add_child(LiteralNode(int(ctx.getText()), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        

    # Exit a parse tree produced by variablesParser#Integer.
    def exitInteger(self, ctx:variablesParser.IntegerContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOp(self, ctx:variablesParser.UnaryOpContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOp(self, ctx:variablesParser.UnaryOpContext):
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
