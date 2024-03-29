from grammars.C.CListener import CListener
from grammars.C.CParser import CParser
from ASTNode import *
from SymbolTable import SymbolTable
from utils import Counter, getTypeLLVM
import re

class ASTListener(CListener):
    def __init__(self):
        self.curr_node = None
        self.counter = Counter()
        
    def enterProgram(self, ctx:CParser.ProgramContext):
        assert self.curr_node is None
        self.curr_node = ProgNode(ctx.getChild(0).getText() == "#include <stdio.h>", self.counter.incr())
        self.curr_node.setLineInfo(ctx)


    # Exit a parse tree produced by variablesParser#Program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass

    # Enter a parse tree produced by variablesParser#Integer.
    def enterInteger(self, ctx:CParser.IntegerContext):
        self.curr_node.add_child(LiteralNode(int(ctx.getText()), "i32", self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        
    # Exit a parse tree produced by variablesParser#Integer.
    def exitInteger(self, ctx:CParser.IntegerContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Float.
    def enterFloat(self, ctx:CParser.FloatContext):
        self.curr_node.add_child(LiteralNode(float(ctx.getText()), "double", self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Float.
    def exitFloat(self, ctx:CParser.FloatContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#String.
    def enterString(self, ctx:CParser.StringContext):
        value = ctx.getText()[1:-1].replace("\\n", "\\0A").replace("\\t", "\\09") + '\\00' 
        self.curr_node.add_child(LiteralNode(value, "i8*", self.counter.incr(), ["const", "string"]), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.str_length = len(self.curr_node.value) - (2 * value.count("\\0"))

    # Exit a parse tree produced by variablesParser#String.
    def exitString(self, ctx:CParser.StringContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Character.
    def enterCharacter(self, ctx:CParser.CharacterContext):
        self.curr_node.add_child(LiteralNode(ord(ctx.getText()[1]), "i8", self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Character.
    def exitCharacter(self, ctx:CParser.CharacterContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOp(self, ctx:CParser.UnaryOpContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOp(self, ctx:CParser.UnaryOpContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpBoolean(self, ctx:CParser.UnaryOpBooleanContext):
        self.curr_node = self.curr_node.parent

        # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        if self.curr_node.operation == "&":
            self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpPointer(self, ctx:CParser.UnaryOpPointerContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        self.curr_node.add_child(UnaryOperationNode(ctx.getChild(0).getText() + 'x', self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierPrefix(self, ctx:CParser.UnaryOpIdentifierPrefixContext):
        if not self.curr_node.children:
            self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#UnaryOp.
    def enterUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        self.curr_node.add_child(UnaryOperationNode('x' + ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#UnaryOp.
    def exitUnaryOpIdentifierSuffix(self, ctx:CParser.UnaryOpIdentifierSuffixContext):
        if not self.curr_node.children:
            self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.parent

    def enterUnaryOpArray(self, ctx:CParser.UnaryOpArrayContext):
        self.curr_node.add_child(UnaryOperationNode("[]", self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(0).getText(), self.counter.incr()), ctx)

    def exitUnaryOpArray(self, ctx:CParser.UnaryOpArrayContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOp.
    def enterBinaryOp(self, ctx:CParser.BinaryOpContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOp.
    def exitBinaryOp(self, ctx:CParser.BinaryOpContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#BinaryOpBoolean.
    def enterBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        self.curr_node.add_child(BinaryOperationNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#BinaryOpBoolean.
    def exitBinaryOpBoolean(self, ctx:CParser.BinaryOpBooleanContext):
        self.curr_node = self.curr_node.parent

    def enterInitializerList(self, ctx:CParser.InitializerListContext):
        self.curr_node.add_child(InitializerListNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    def exitInitializerList(self, ctx:CParser.InitializerListContext):
        self.curr_node.type = f"[{len(self.curr_node.children)} x {self.curr_node.children[0].type}]"
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        self.curr_node.add_child(DefinitionNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
        self.curr_node = self.curr_node.parent


    # Enter a parse tree produced by variablesParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        self.curr_node.add_child(AssignmentNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()


    # Exit a parse tree produced by variablesParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        self.curr_node.add_child(DeclarationNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IdentifierNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)

    # Exit a parse tree produced by variablesParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        _type, type_semantics = getTypeLLVM(ctx.getChild(0).getText())
        identifier = self.curr_node.children[0]
        identifier.type = _type
        identifier.type_semantics = type_semantics
        if ctx.getChildCount() > 3:
            dimensions = re.findall('\[.*?\]', ctx.getText())
            for dim in dimensions:
                dim = dim[1:-1]
                identifier.type = f"[{str(eval(dim))} x {identifier.type}]"
        self.curr_node.children = [self.curr_node.children[0]]
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by variablesParser#Identifier.
    def enterIdentifierExpr(self, ctx:CParser.IdentifierExprContext):
        self.curr_node.add_child(IdentifierNode(ctx.getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by variablesParser#Identifier.
    def exitIdentifierExpr(self, ctx:CParser.IdentifierExprContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by CParser#scope.
    def enterScope(self, ctx:CParser.ScopeContext):
        self.curr_node.add_child(ScopeNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by CParser#scope.
    def exitScope(self, ctx:CParser.ScopeContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by CParser#IfStatement.
    def enterIfStatement(self, ctx:CParser.IfStatementContext):
        self.curr_node.add_child(BranchNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(IfNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by CParser#IfStatement.
    def exitIfStatement(self, ctx:CParser.IfStatementContext):
        self.curr_node = self.curr_node.parent.parent    

    def enterElif_stat(self, ctx:CParser.Elif_statContext):
        self.curr_node.parent.add_child(ElifNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.parent.last_child()

    # Exit a parse tree produced by CParser#elif_stat.
    def exitElif_stat(self, ctx:CParser.Elif_statContext):
        pass

    # Enter a parse tree produced by CParser#else_stat.
    def enterElse_stat(self, ctx:CParser.Else_statContext):
        self.curr_node.parent.add_child(ElseNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.parent.last_child()

    # Exit a parse tree produced by CParser#else_stat.
    def exitElse_stat(self, ctx:CParser.Else_statContext):
        pass

    # Enter a parse tree produced by CParser#WhileStatement.
    def enterWhileStatement(self, ctx:CParser.WhileStatementContext):
        self.curr_node.add_child(WhileNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by CParser#WhileStatement.
    def exitWhileStatement(self, ctx:CParser.WhileStatementContext):
        self.curr_node = self.curr_node.parent

    # Enter a parse tree produced by CParser#ForStatement.
    def enterForStatement(self, ctx:CParser.ForStatementContext):
        self.curr_node.add_child(WhileNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by CParser#ForStatement.
    def exitForStatement(self, ctx:CParser.ForStatementContext):
        node = self.curr_node
        self.curr_node.parent.children.pop()
        self.curr_node.parent.add_child(node.children.pop(0), ctx)
        self.curr_node.parent.add_child(node)
        node.last_child().add_child(node.children.pop(1), ctx)
        self.curr_node = self.curr_node.parent       

    # Enter a parse tree produced by CParser#SwitchStatement.
    def enterSwitchStatement(self, ctx:CParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by CParser#SwitchStatement.
    def exitSwitchStatement(self, ctx:CParser.SwitchStatementContext):
        pass

    def enterFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        self.curr_node.add_child(FunctionDeclarationNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(FunctionNode(ctx.getChild(1).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(ArgListNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    # Exit a parse tree produced by CParser#function_declaration.
    def exitFunctionDeclaration(self, ctx:CParser.FunctionDeclarationContext):
        # _type, type_semantics = getTypeLLVM(ctx.getChild(0).getText())
        # self.curr_node.children[0].type = _type
        # self.curr_node.children[0].type_semantics = type_semantics
        # childCount = ctx.getChild(2).getChildCount()
        # if childCount > 2:
        #     for i in range(1, childCount, 3):
        #         arg_type, arg_type_semantics = getTypeLLVM(ctx.getChild(2).getChild(i).getText())
        #         self.curr_node.children[0].arg_types.append(arg_type)
        #         self.curr_node.children[0].arg_types_semantics.append(arg_type_semantics)
        self.curr_node = self.curr_node.parent
        _type, type_semantics = getTypeLLVM(ctx.getChild(0).getText())
        self.curr_node.type = _type
        self.curr_node.type_semantics = type_semantics
        self.curr_node = self.curr_node.parent.parent

    def enterFunctionDefinitionStatement(self, ctx:CParser.FunctionDefinitionStatementContext):
        self.curr_node.add_child(FunctionDefinitionNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    def exitFunctionDefinitionStatement(self, ctx:CParser.FunctionDefinitionStatementContext):
        if not self.curr_node.children[1].last_child() or not isinstance(self.curr_node.children[1].last_child(), ReturnNode):
            return_node = ReturnNode(self.counter.incr())
            return_type = self.curr_node.children[0].children[0].type
            if return_type != 'void':
                return_node.add_child(LiteralNode(0, return_type, self.counter.incr()), ctx)
            self.curr_node.children[1].add_child(return_node, ctx)
        self.curr_node = self.curr_node.parent

    def enterFunctionCall(self, ctx:CParser.FunctionCallContext):
        self.curr_node.add_child(FunctionCallNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        self.curr_node.add_child(FunctionNode(ctx.getChild(0).getChild(0).getText(), self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()
        if self.curr_node.name == "printf" or self.curr_node.name == "scanf":
            self.curr_node.type = "i32 (i8*, ...)"
        self.curr_node = self.curr_node.parent
        self.curr_node.add_child(ArgListNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    def exitFunctionCall(self, ctx:CParser.FunctionCallContext):
        self.curr_node = self.curr_node.parent.parent

    def enterBreakStatement(self, ctx:CParser.BreakStatementContext):
        self.curr_node.add_child(BreakNode(self.counter.incr()), ctx)
        
    def enterContinueStatement(self, ctx:CParser.ContinueStatementContext):
        self.curr_node.add_child(ContinueNode(self.counter.incr()), ctx)

    def enterReturnStatement(self, ctx:CParser.ReturnStatementContext):
        self.curr_node.add_child(ReturnNode(self.counter.incr()), ctx)
        self.curr_node = self.curr_node.last_child()

    def exitReturnStatement(self, ctx:CParser.ReturnStatementContext):
        self.curr_node = self.curr_node.parent
