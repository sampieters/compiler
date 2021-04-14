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
            node.type = "i1"
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
            node.type = "i1"
        else:
            node.type = getBinaryType(node.children[0].type, node.children[1].type)
            if node.operation == "%" and node.type in ["float", "double"]:
                raise Exception(f"Error: Invalid operands to binary expression ('{node.children[0].type}' and '{node.children[1].type}'")

    def exitDefinition(self, node):
        child1 = node.children[0].children[0]
        child2 = node.children[1]
        if child1.type.endswith("*"):
            if child1.type == child2.type:
                pass
            elif child2.type in INTEGER_TYPES:
                print(f"Warning: Incompatible integer to pointer conversion initializing '{child1.type}' with an expression of type '{child2.type}'")
            elif child2.type.endswith("*"):
                print(f"Warning: Incompatible pointer types initializing '{child1.type}' with an expression of type '{child2.type}'")
            elif not child1.type == child2.type:
                raise Exception(f"Error: Initializing '{child1.type}' with an expression of incompatible type '{child2.type}'")
        if child1.dimensions:
            if not child2.dimensions:
                raise Exception(f"Error: Array Initializer must be an initializer list or wide string literal")
            # TODO: wont work for multidimensional arrays
            for child in child2.children:
                if checkInfoLoss(child.type, child1.type):
                    print(f"Warning: implicit conversion from '{child.type}' to '{child1.type}' can cause a loss of information.")
        elif checkInfoLoss(child2.type, child1.type):
            print(f"Warning: implicit conversion from '{child2.type}' to '{child1.type}' can cause a loss of information.")

    def exitAssignment(self, node):
        child1, child2 = node.children
        for child in [child1, child2]:
            if isinstance(IdentifierNode, child):
                child = self.table.get_symbol(child.name)
        if child1.type.endswith("*"):
            if child2.type in INTEGER_TYPES:
                print(f"Warning: Incompatible integer to pointer conversion assigning to '{child1.type}' from '{child2.type}'")
            else:
                raise Exception(f"Error: Assigning to '{child1.type}' from incompatible type '{child2.type}'")
        elif checkInfoLoss(child2.type, child1.type):
            print(f"Warning: implicit conversion from '{child2.type}' to '{child1.type}' can cause a loss of information.")

    def exitDeclaration(self, node):
        pass

    def exitBreak(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, WhileNode)):
            raise Exception("Error: 'break' statement not in loop or switch statement")

    def exitContinue(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, WhileNode)):
            raise Exception("Error: 'continue' statement not in loop statement")

    def exitReturn(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, FunctionDefinitionNode)):
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

    def exitFunctionDeclaration(self, node):
        function = node.children[0]
        def_node = self.table.get_symbol_curr_scope(function.name)
        # If the symbol was already declared before
        if def_node is not None:
            raise Exception(f"Error: Redefinition of '{function.name}' as different kind of symbol")
        else:
            self.table.add_symbol(function)

    def exitFunctionCall(self, node):
        function = self.getSymbol(node.children[0])
        node.type = function.type
        node.type_semantics = function.type_semantics
        call_args = node.children[1].children
        function_args = function.children[0].children

        if len(function_args) > len(call_args):
            raise Exception(f"Too few arguments to function call, expected {len(function_args)}, have {len(call_args)}")
        elif len(function_args) < len(call_args):
            raise Exception(f"Too many arguments to function call, expected {len(function_args)}, have {len(call_args)}")
        for child1, child2 in zip(call_args, function_args):
            child2 = child2.children[0]
            if child1.type.endswith("*"):
                if child2.type in INTEGER_TYPES:
                    print(f"Warning: Incompatible pointer to integer conversion passing '{child1.type}' to parameter of type '{child2.type}'; dereference with *")
                else:
                    raise Exception(f"Error: Passing '{child1.type}' to parameter of incompatible type '{child2.type}'")
            elif child2.type.endswith("*"):
                if child1.type in INTEGER_TYPES:
                    print(f"Warning: Incompatible integer to pointer conversion passing '{child1.type}' to parameter of type '{child2.type}'; dereference with *")
                else:
                    raise Exception(f"Error: Passing '{child1.type}' to parameter of incompatible type '{child2.type}'")
            elif checkInfoLoss(child1.type, child2.type):
                print(f"Warning: implicit conversion from '{child1.type}' to '{child2.type}' can cause a loss of information.")
        

    def getSymbol(self, node):
        if (isinstance(node, IdentifierNode) or isinstance(node, FunctionNode)) and node.name is not None:
            return self.table.get_symbol(node.name)
        else:
            return node