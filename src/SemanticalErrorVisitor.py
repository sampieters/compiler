from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor
from .SymbolTable import SymbolTable
from .ASTNode import *

class SemanticalErrorVisitor(variablesVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx:variablesParser.ProgramContext):
        print(self.visitChildren(ctx))

    def visitIdentifier(self, node):
        if isinstance(node.parent, DefinitionNode) or isinstance(node.parent, DeclarationNode):
            if self.table.get_symbol(str(node.name)):
                print("error, already definition of this ID")
            else:
                self.table.add_symbol(str(node.name))

    def visitBinaryOp(self, node):
        print("bezig")




    def visitDeclaration(self, node):
        SymbolTable.add_symbol(str(node.children[0]))

        # print("Visiting Declaration Node")
        pass