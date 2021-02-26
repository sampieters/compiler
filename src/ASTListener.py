from grammars.expressions.expressionsListener import expressionsListener
from grammars.expressions.expressionsParser import expressionsParser
from ASTNode import *
from utils import Counter

class ASTListener(expressionsListener):
    def __init__(self):
        self.curr_node = None
        self.counter = Counter()
        
    def enterProgram(self, ctx:expressionsParser.ProgramContext):
        assert self.curr_node is None
        self.curr_node = ASTNode(self.counter.incr())

    # Exit a parse tree produced by expressionsParser#Program.
    def exitProgram(self, ctx:expressionsParser.ProgramContext):
        pass


    # Enter a parse tree produced by expressionsParser#Expression.
    def enterExpression(self, ctx:expressionsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by expressionsParser#Expression.
    def exitExpression(self, ctx:expressionsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by expressionsParser#Integer.
    def enterInteger(self, ctx:expressionsParser.IntegerContext):
        self.curr_node.add_child(LiteralNode(int(ctx.getText()), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()
        

    # Exit a parse tree produced by expressionsParser#Integer.
    def exitInteger(self, ctx:expressionsParser.IntegerContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by expressionsParser#UnaryOp.
    def enterUnaryOp(self, ctx:expressionsParser.UnaryOpContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()


    # Exit a parse tree produced by expressionsParser#UnaryOp.
    def exitUnaryOp(self, ctx:expressionsParser.UnaryOpContext):
        self.curr_node = self.parent

    # Enter a parse tree produced by expressionsParser#Brackets.
    def enterBrackets(self, ctx:expressionsParser.BracketsContext):
        pass

    # Exit a parse tree produced by expressionsParser#Brackets.
    def exitBrackets(self, ctx:expressionsParser.BracketsContext):
        pass


    # Enter a parse tree produced by expressionsParser#BinaryOp.
    def enterBinaryOp(self, ctx:expressionsParser.BinaryOpContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by expressionsParser#BinaryOp.
    def exitBinaryOp(self, ctx:expressionsParser.BinaryOpContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by expressionsParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:expressionsParser.BinaryOpBooleanContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()))
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by expressionsParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:expressionsParser.BinaryOpBooleanContext):
        self.curr_node = self.parent
