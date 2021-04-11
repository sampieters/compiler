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
        if node.type == "void":
            raise Exception("Variable has incomplete type 'void'")
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
        # If the identifier is on the left side of an assignment
        elif node.isBeingAssigned():
            def_node = self.table.get_symbol(node.name)
            if "const" in def_node.type_semantics:
                raise Exception(f"Error: Cannot assign to variable '{node.name}' with const-qualified type '{node.type}'")
        else:
            def_node = self.table.get_symbol(node.name)
            if def_node is None:
                raise Exception(f"Error: Use of undeclared variable '{node.name}'")
            else:
                node.type = def_node.type

    def exitUnaryOperation(self, node):
        if isinstance(node.parent, ScopeNode) or isinstance(node.parent, ProgNode):
            print("Warning: Expression result unused")
        if node.operation in BOOLEAN_OPS:
            node.type = "i32"
        elif node.operation == "*":
            if not node.children[0].type.endswith("*"):
                raise Exception(f"Error: Indirection requires pointer operand ('{node.children[0].type}' invalid)")
            else:
                node.type = node.children[0].type[:-1]
        elif node.operation == "&":
            node.type = "i64"
        else:
            node.type = node.children[0].type

    def exitBinaryOperation(self, node):
        if isinstance(node.parent, ScopeNode) or isinstance(node.parent, ProgNode):
            print("Warning: Expression result unused")
        if node.operation in BOOLEAN_OPS:
            node.type = "i32"
        else:
            node.type = getBinaryType(node.children[0].type, node.children[1].type)
            if node.operation == "%" and node.type in ["float", "double"]:
                raise Exception(f"Error: Invalid operands to binary expression ('{node.children[0].type}' and '{node.children[1].type}'")

    def exitDefinition(self, node):
        if checkInfoLoss(node.children[1].type, node.children[0].children[0].type):
            print(f"Warning: implicit conversion from '{node.children[1].type}' to '{node.children[0].children[0].type}' can cause a loss of information.")

    def exitAssignment(self, node):
        child1, child2 = node.children
        for child in [child1, child2]:
            if isinstance(IdentifierNode, child):
                child = self.table.get_symbol(child.name)
        if checkInfoLoss(child2.type, child1.type):
            print(f"Warning: implicit conversion from '{child2.type}' to '{child1.type}' can cause a loss of information.")

    def exitDeclaration(self, node):
        pass

    def exitBreak(self, node):
        if not (isinstance(node.parent, ScopeNode) and isinstance(node.parent.parent, WhileNode)):
            raise Exception("Error: 'break' statement not in loop or switch statement")

    def exitContinue(self, node):
        if not (isinstance(node.parent, ScopeNode) and isinstance(node.parent.parent, WhileNode)):
            raise Exception("Error: 'continue' statement not in loop statement")

    def exitReturn(self, node):
        if not (isinstance(node.parent, ScopeNode) and isinstance(node.parent.parent, FunctionDefinitionNode)):
            raise Exception("Error: 'return' statement not in function body")
        if not node.children:
            node.type = 'void'
        else:
            node.type = node.children[0].type
        func_name = node.parent.parent.children[0].children[0].name
        func_type = self.table.get_symbol(func_name).type
        if func_type == 'void' and node.type != 'void':
            raise Exception(f"Error: Void function '{func_name}' should not return a value")
        elif func_type != 'void' and node.type == 'void':
            raise Exception(f"Error: Non-void function '{func_name}' should return a value")

    def exitFunctionDefinition(self, node):
        if not isinstance(node.parent, ProgNode):
            raise Exception("Error: Function definition is not allowed here")
