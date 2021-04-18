from SymbolTable import SymbolTable
from ASTNode import *
from utils import *

#TODO: replace error messages with actual exceptions
#TODO: Check if void only in functions

PRINTF_TO_TYPE = {'d': "i32", 'i': "i32", 's': "i8*", 'c': "i8", 'f': "double"}

class SemanticalErrorVisitor(ASTVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.defined_functions = []
        self.stdio_included = False
        self.warnings = []
        self.errors = []

    def printWarnings(self):
        print("\n".join(self.warnings))

    def printErrors(self):
        print("\n".join(self.errors))
        if self.errors:
            raise Exception(self.errors[0])

    def handleWarning(self, node, msg):
        if node.lineNr and node.column:
            self.warnings.append(f"Warning at line {node.lineNr}:{node.column}: {msg}")
        else:
            self.warnings.append(f"Warning: {msg}")

    def handleError(self, node, msg):
        if node.lineNr and node.column:
            self.errors.append(f"Error at line {node.lineNr}:{node.column}: {msg}")
        else:
            self.errors.append(f"Error: {msg}")


    def get_arg_amount(self, string):
        arg_list = []
        for i in range(len(string)):
            if string[i] == '%' and i != range(len(string)):
                if string[i+1] in ['d', 'i', 's', 'c', 'f']:
                    arg_list.append(PRINTF_TO_TYPE[string[i+1]])
        return arg_list

    def enterProg(self, node):
        if node.include:
            self.stdio_included = True
        main_found = False
        for child in node.children:
            if isinstance(child, FunctionDefinitionNode):
                if child.children[0].children[0].name == "main":
                    main_found = True
        if not main_found:
            self.handleError(node, "No main function found")

    def exitProg(self, node):
        self.printWarnings()
        self.printErrors()

    def enterScope(self, node):
        self.table.enter_scope()

    def exitScope(self, node):
        self.table.exit_scope()

    def exitIdentifier(self, node):
        # If the identifier is on the left side of a definition or declaration
        if node.type == "void":
            self.handleError(node, "Variable has incomplete type 'void'")
        if node.isBeingDeclared():
            def_node = None
            if not getParent(node, ScopeNode) and not getParent(node, FunctionDeclarationNode):
                node.type_semantics.append("global")
            if not (getParent(node, FunctionDeclarationNode) and not getParent(node, FunctionDefinitionNode)):
                def_node = self.table.get_symbol_curr_scope(node.name)
            # If the identifier was already declared before
            if def_node is not None and not isinstance(def_node.parent.parent, ArgListNode):
                err_msg = f"Redefinition of '{node.name}'"
                if def_node.type != node.type:
                    err_msg += f" with a different type: '{node.type}' vs '{def_node.type}'" 
                self.handleError(node, err_msg)
            else:
                self.table.add_symbol(node)
        # If the identifier is on the left side of an assignment
        elif node.isBeingAssigned():
            def_node = self.table.get_symbol(node.name)
            if def_node is None:
                self.handleError(node, f"Use of undeclared variable '{node.name}'")
            if "const" in def_node.type_semantics:
                self.handleError(node, f"Cannot assign to variable '{node.name}' with const-qualified type '{node.type}'")
        else:
            def_node = self.table.get_symbol(node.name)
            if def_node is None:
                self.handleError(node, f"Use of undeclared variable '{node.name}'")
            else:
                node.type = def_node.type

    def exitUnaryOperation(self, node):
        if isinstance(node.parent, ScopeNode) or isinstance(node.parent, ProgNode):
            self.handleWarning(node, "Expression result unused")
        if isinstance(node.children[0], LiteralNode) and node.operation in ["++x", "x++", "--x", "x--"]:
            self.handleError(node, "Expression is not assignable")
        if node.operation in BOOLEAN_OPS:
            node.type = "i1"
        elif node.operation == "*":
            if not node.children[0].type.endswith("*"):
                self.handleError(node, f"Indirection requires pointer operand ('{node.children[0].type}' invalid)")
            else:
                node.type = node.children[0].type[:-1]
        elif node.operation == "&":
            if isinstance(node.children[0], LiteralNode):
                self.handleError(node, f"Cannot take the address of an rvalue of type '{node.children[0].type}'")
            node.type = "i64"
        elif node.operation == '[]':
            if not node.children[0].type.startswith("["):
                self.handleError(node, "Subscripted value is not an array, pointer or vector")
            if node.children[1].type not in INTEGER_TYPES:
                self.handleError(node, "Array subscript is not an integer")
        else:
            node.type = node.children[0].type

    def exitBinaryOperation(self, node):
        if isinstance(node.parent, ScopeNode) or isinstance(node.parent, ProgNode):
            self.handleWarning(node, "Expression result unused")
        if node.operation in BOOLEAN_OPS:
            node.type = "i1"
        else:
            node.type = getBinaryType(node.children[0].type, node.children[1].type)
            if node.operation == "%" and node.type in ["float", "double"]:
                self.handleError(node, f"Invalid operands to binary expression ('{node.children[0].type}' and '{node.children[1].type}'")

    def exitDefinition(self, node):
        child1 = node.children[0].children[0]
        child2 = node.children[1]
        if child1.type.endswith("*"):
            if child1.type == child2.type:
                pass
            elif child2.type in INTEGER_TYPES:
                self.handleWarning(node, f"Incompatible integer to pointer conversion initializing '{child1.type}' with an expression of type '{child2.type}'")
            elif child2.type.endswith("*"):
                self.handleWarning(node, f"Incompatible pointer types initializing '{child1.type}' with an expression of type '{child2.type}'")
            elif not child1.type == child2.type:
                self.handleError(node, f"Initializing '{child1.type}' with an expression of incompatible type '{child2.type}'")
        if child1.type.startswith("["):
            if not child2.type.startswith("["):
                self.handleError(node, f"Array Initializer must be an initializer list or wide string literal")
            # TODO: wont work for multidimensional arrays
            for child in child2.children:
                if self.checkInfoLoss(child, child1):
                    self.handleWarning(node, f"implicit conversion from '{child.type}' to '{child1.type}' can cause a loss of information.")
        elif self.checkInfoLoss(child2, child1):
            self.handleWarning(node, f"implicit conversion from '{child2.type}' to '{child1.type}' can cause a loss of information.")

    def exitAssignment(self, node):
        child1, child2 = node.children
        # Get the identifier node on the left side by going down potential unary operations
        while not isinstance(child1, IdentifierNode):
            # If the unary operation node on the left is not a [] or * operation, throw an exception
            if isinstance(child1, UnaryOperationNode) and (child1.operation == "[]" or child1.operation == "*"):
                child1 = child1.children[0]
            else:
                self.handleError(node, "Expression is not assignable")
        # Make a temporary copy of the identifier on the left, take the child1 node from the symbol table
        tmp = child1
        child1 = self.table.get_symbol(child1.name)
        tmp.type = child1.type
        # For each * operation, remove a * from the type, throw an exception if it becomes an expression by doing this
        while not isinstance(tmp.parent, AssignmentNode):
            if tmp.parent.operation == "*" and tmp.type.endswith("*"):
                tmp.parent.type = tmp.type[:-1]
            elif tmp.parent.operation == "*":
                self.handleError(node, "Expression is not assignable")
            #TODO: maybe do something for [] operations?
            tmp = tmp.parent
        # If the right side of the expression is an identifier, grab it from the symbol table
        if isinstance(child2, IdentifierNode):
            child2 = self.table.get_symbol(child2.name)
        if child2.type == 'void':
            self.handleError(node, f"Assigning to '{child1.type} from incompatible type '{child2.type}'")
        # If the identifier on the left of the assignment is a pointer, throw the appropriate exceptions/warnings
        if child1.type.endswith("*"):
            if child2.type in INTEGER_TYPES:
                self.handleWarning(node, f"Incompatible integer to pointer conversion assigning to '{child1.type}' from '{child2.type}'")
            else:
                self.handleError(node, f"Assigning to '{child1.type}' from incompatible type '{child2.type}'")
        # Otherwise check if an information loss occurs
        elif self.checkInfoLoss(child2, child1):
            self.handleWarning(node, f"implicit conversion from '{child2.type}' to '{child1.type}' can cause a loss of information.")

    def exitDeclaration(self, node):
        pass

    def exitBreak(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, WhileNode)):
            self.handleError(node, "'break' statement not in loop or switch statement")

    def exitContinue(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, WhileNode)):
            self.handleError(node, "'continue' statement not in loop statement")

    def exitReturn(self, node):
        if not (isinstance(node.parent, ScopeNode) and getParent(node, FunctionDefinitionNode)):
            self.handleError(node, "'return' statement not in function body")
        if not node.children:
            node.type = 'void'
        else:
            node.type = node.children[0].type
        func_name = getParent(node, FunctionDefinitionNode).children[0].children[0].name
        func_type = self.table.get_symbol(func_name).type
        if func_type == 'void' and node.type != 'void':
            self.handleError(node, f"Void function '{func_name}' should not return a value")
        elif func_type != 'void' and node.type == 'void':
            self.handleError(node, f"Non-void function '{func_name}' should return a value")

    def exitFunctionDefinition(self, node):
        if not isinstance(node.parent, ProgNode):
            self.handleError(node, "Function definition is not allowed here")

    def enterFunctionDeclaration(self, node):
        function = node.children[0]
        def_node = self.table.get_symbol_curr_scope(function.name)

        # Check if there are multiple paramaters with the same name
        arg_names = []
        for arg in function.children[0].children:
            if arg.children[0].name not in arg_names:
                arg_names.append(arg.children[0].name)
            else:
                raise Exception(f"Error: Redefinition of parameter {arg.children[0].name}")
        # If the symbol was already declared before
        if def_node is not None and function.name in self.defined_functions:
            self.handleError(node, f"Redefinition of '{function.name}' as different kind of symbol")
        # Elif the return type is different of the same function
        elif def_node is not None and def_node.type != function.type:
            self.handleError(node, f"Conflicting types for '{function.name}'")
        # Elif the number of arguments is not the same
        elif def_node is not None:
            for child1, child2 in zip(function.children[0].children, def_node.children[0].children):
                if child1.type != child2.type:
                    self.handleError(node, f"Conflicting types for '{function.name}'")
        else:
            self.table.add_symbol(function)
            if isinstance(node.parent, FunctionDefinitionNode):
                self.defined_functions.append(function.name)

    def exitFunctionCall(self, node):
        function = self.getSymbol(node.children[0])
        if function is None:
            self.handleError(node, f"Implicit declaration of function \'{node.children[0].name}\' is invalid in C99")
        if function.name in ["printf", "scanf"]:
            if not self.stdio_included:
                self.handleError(node, f"Implicitly declaring library function '{function.name}' with type '{function.type}'")
            arg_list = node.children[1].children
            arg_char_list = self.get_arg_amount(node.children[1].children[0].value)
            if len(arg_list)-1 > len(arg_char_list):
                self.handleWarning(node, f"Data argument(s) not used by format string")
            elif len(arg_list)-1 < len(arg_char_list):
                self.handleWarning(node, f"More '%' conversions than data arguments")
            else:
                for i in range(len(arg_char_list)):
                    if arg_list[i+1].type != arg_char_list[i]:
                        self.handleWarning(node, f"Format specifies type '{arg_char_list[i]}' but the argument has type '{arg_list[i+1].type}'")

            return
        node.type = function.type
        node.type_semantics = function.type_semantics
        call_args = node.children[1].children
        function_args = function.children[0].children

        if len(function_args) > len(call_args):
            self.handleError(node, f"Too few arguments to function call, expected {len(function_args)}, have {len(call_args)}")
        elif len(function_args) < len(call_args):
            self.handleError(node, f"Too many arguments to function call, expected {len(function_args)}, have {len(call_args)}")
        for child1, child2 in zip(call_args, function_args):
            child2 = child2.children[0]
            if child1.type == child2.type:
                continue
            elif child1.type.endswith("*"):
                if child2.type in INTEGER_TYPES:
                    self.handleWarning(node, f"Incompatible pointer to integer conversion passing '{child1.type}' to parameter of type '{child2.type}'; dereference with *")
                else:
                    self.handleError(node, f"Passing '{child1.type}' to parameter of incompatible type '{child2.type}'")
            elif child2.type.endswith("*"):
                if child1.type in INTEGER_TYPES:
                    self.handleWarning(node, f"Incompatible integer to pointer conversion passing '{child1.type}' to parameter of type '{child2.type}'; dereference with *")
                else:
                    self.handleError(node, f"Passing '{child1.type}' to parameter of incompatible type '{child2.type}'")
            elif self.checkInfoLoss(child1, child2):
                self.handleWarning(node, f"implicit conversion from '{child1.type}' to '{child2.type}' can cause a loss of information.")
        

    def getSymbol(self, node):
        if (isinstance(node, IdentifierNode) or isinstance(node, FunctionNode)) and not node.name in [None, "printf", "scanf"]:
            return self.table.get_symbol(node.name)
        else:
            return node

    def checkInfoLoss(self, node1, node2):
        if isinstance(node1, LiteralNode) and node1.type in DECIMAL_TYPES and node2.type in DECIMAL_TYPES:
            return False
        else:
            return checkInfoLoss(node1.type, node2.type)