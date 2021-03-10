from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor
from .SymbolTable import SymbolTable
from .ASTNode import *
from .utils import *

class SemanticalErrorVisitor(variablesVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx:variablesParser.ProgramContext):
        print(self.visitChildren(ctx))

    def visitIdentifier(self, node):
        if isinstance(node.parent, DefinitionNode) or isinstance(node.parent, DeclarationNode):
            if self.table.get_symbol_curr_scope(str(node.name)) is None:
                print("Warning: already definition of this ID")
            else:
                self.table.add_symbol(node)
        else:
            if self.table.get_symbol_curr_scope(node.name) is None:
                print("Warning: identifier with name " + node.name + " not declared")


    def visitUnaryOp(self, node):
        print("bezig")

    def visitBinaryOp(self, node):
        node.type = getAccType(node.children[0], node.children[1])

    def visitDefinitionNode(self, node):
        print("lolo")




    def visitDeclaration(self, node):
        SymbolTable.add_symbol(str(node.children[0]))

        # print("Visiting Declaration Node")
        pass