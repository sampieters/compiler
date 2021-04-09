from SymbolTable import SymbolTable
from ASTNode import *
from utils import *

#TODO: replace error messages with actual exceptions
#TODO: Check if void only in functions

class SemanticalErrorVisitor(ASTVisitor):
    def __init__(self):
        self.table = SymbolTable()

    def exitIdentifier(self, node):
        # If the identifier is on the left side of a definition or declaration
        if node.isBeingDeclared():
            def_node = self.table.get_symbol_curr_scope(node.name)
            # If the identifier was already declared before
            if def_node is not None:
                err_msg = f"Error: Redefinition of '{node.name}'"
                if def_node.type != node.type:
                    err_msg += f" with a different type: '{node.type}' vs '{def_node.type}'" 
                raise Exception(err_msg)
            else:
                self.table.add_symbol(node)
        elif node.isBeingAssigned():
            def_node = self.table.get_symbol(node.name)
            if def_node.type.startswith("const"):
                raise Exception(f"Error: Cannot assign to variable '{node.name}' with const-qualified type '{node.type}'")
        else:
            def_node = self.table.get_symbol(node.name)
            if def_node is None:
                raise Exception(f"Error: Use of undeclared variable '{node.name}'")
            else:
                node.type = def_node.type

    def exitUnaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.exitUnaryOpBoolean(node)
        elif node.operation in POINTER_OPS:
            self.exitUnaryOpPointer(node)
        else:
            self.exitUnaryOp(node)

    def exitUnaryOp(self, node):
        node.type = node.children[0].type

    def exitUnaryOpBoolean(self, node):
        node.type = "i32"

    def exitUnaryOpPointer(self, node):
        if node.operation == "*":
            if not node.children[0].type.endswith("*"):
                raise Exception(f"Error: Indirection requires pointer operand ('{node.children[0].type}' invalid)")
            else:
                node.type = node.children[0].type[:-1]
        elif node.operation == "&":
            node.type = "i64"

    def exitBinaryOperation(self, node):
        if node.operation in BOOLEAN_OPS:
            self.exitBinaryOpBoolean(node)
        else:
            self.exitBinaryOp(node)

    def exitBinaryOp(self, node):
        node.type = getBinaryType(node.children[0].type, node.children[1].type)

    def exitBinaryOpBoolean(self, node):
        node.type = "i32"

    def exitDefinitionNode(self, node):
        pass

    def exitDeclaration(self, node):
        pass

    # TODO: make sure break continue are only used in loops, function declarations/definitions are only used in global scope