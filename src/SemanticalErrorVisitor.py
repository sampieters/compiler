from grammars.variables.variablesParser import variablesParser
from grammars.variables.variablesVisitor import variablesVisitor
from SymbolTable import SymbolTable
from ASTNode import *
from utils import *

class SemanticalErrorVisitor(ASTVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # Visit a parse tree produced by variablesParser#Program.
    def visitProgram(self, ctx:variablesParser.ProgramContext):
        print(self.visitChildren(ctx))

    def visitIdentifier(self, node):
        # If the identifier is on the left side of a definition or declaration
        if node.isBeingDeclared():
            def_node = self.table.get_symbol_curr_scope(str(node))
            # If the identifier was already declared before
            if def_node is not None:
                print(f"Error: Redefinition of '{str(node)}'{"" if def_node.type == node.type else f" with a different type: '{node.type}' vs '{def_node.type}'"}")
            else:
                self.table.add_symbol(node)
        elif node.isBeingAssigned():
            def_node = self.table.get_symbol(str(node))
            if def_node.type.startswith("const"):
                print(f"Error: Cannot assign to variable '{str(node)}' with const-qualified type '{node.type}'")
        else:
            if self.table.get_symbol(node.name) is None:
                print(f"Error: Use of undeclared variable '{node.name}'")

    def visitUnaryOp(self, node):
        node.type = node.children[0].type

    def visitUnaryOpBoolean(self, node):
        node.type = "int"

    def visitBinaryOp(self, node):
        node.type = getBinaryType(node.children[0], node.children[1])

    def visitBinaryOpBoolean(self, node):
        node.type = "int"

    def visitDefinitionNode(self, node):
        pass

    def visitDeclaration(self, node):
        pass