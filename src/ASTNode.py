from utils import Counter, getAlignment
from ASTVisitor import ASTVisitor


class ASTNode:
    def __init__(self, node_id=1):
        self.id = node_id
        self.parent = None
        self.children = None
        self.lineNr = None
        self.column = None
        self.symbol = None

    def setLineInfo(self, ctx):
        self.lineNr = str(ctx.start.line)
        self.column = str(ctx.start.column)
        self.symbol = ctx.getText()

    def __str__(self):
        return "error"

    def accept(self, visitor:ASTVisitor):
        pass

    def set_parent(self, node):
        assert self.parent is None
        self.parent = node

    def add_child(self, node, ctx=None):
        if not self.children:
            self.children = [node]
        else:
            self.children.append(node)
        self.last_child().parent = self
        if ctx:
            self.setLineInfo(ctx)

    def last_child(self):
        if not self.children:
            return None
        return self.children[-1]

    def to_dot_recursive(self, file):
        if self.children is not None:
            for child in self.children:
                file.write(f"\tnode{str(child.id)}[label=\"{str(child)}\"]\n")
                file.write(f"\tnode{str(self.id)}->node{str(child.id)}\n")
                child.to_dot_recursive(file)

    def to_dot(self, filename):
        file = open(filename + ".dot", "w")
        file.write("digraph AST {\n")
        file.write(f"\tnode0[label=\"{str(self)}\"]\n")
        self.to_dot_recursive(file)
        file.write("}")

    def visitChildren(self, visitor):
        if not self.children:
            return
        for child in self.children:
            child.accept(visitor)


class ProgNode(ASTNode):
    def __init__(self, include, node_id=0):
        super().__init__(node_id)
        self.include = include

    def __str__(self):
        return 'prog'

    def accept(self, visitor:ASTVisitor):
        visitor.enterProg(self)
        self.visitChildren(visitor)
        visitor.exitProg(self)

class ScopeNode(ASTNode):
    def __init__(self, node_id=0):
        super().__init__(node_id)

    def __str__(self):
        return 'scope'

    def accept(self, visitor:ASTVisitor):
        visitor.enterScope(self)
        self.visitChildren(visitor)
        visitor.exitScope(self)


class LiteralNode(ASTNode):
    def __init__(self, value, _type, node_id, type_semantics = []):
        super().__init__(node_id)
        self.value = value
        self.type_semantics = type_semantics
        self.type = _type
        self.str_length = None
        self.temp_address = None

    def __str__(self):
        return f"{str(self.value)} ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterLiteral(self)
        self.visitChildren(visitor)
        visitor.exitLiteral(self)

    def getValue(self):
        if self.type == "i8*" and "string" in self.type_semantics:
            return f"getelementptr inbounds ([{str(self.str_length)} x i8], [{str(self.str_length)} x i8]* {str(self.temp_address)}, i64 0, i64 0)"
        else:   
            return str(self.value)

    def alignment(self):
        return str(int(getAlignment(self)))


class IdentifierNode(ASTNode):
    def __init__(self, name, node_id, _type=None):
        super().__init__(node_id)
        self.name = name
        self.type = _type
        self.type_semantics = []
        self.original_address = None
        self.temp_address = None
        self.dimensions = []

    def __str__(self):
        return f"{str(self.name)} ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterIdentifier(self)
        self.visitChildren(visitor)
        visitor.exitIdentifier(self)

    def isBeingDeclared(self):
        if isinstance(self.parent, DeclarationNode):
            return self == self.parent.children[0]
        return False

    def isBeingAssigned(self):
        if isinstance(self.parent, AssignmentNode):
            return self == self.parent.children[0]
        return False

    def alignment(self):
        return str(int(getAlignment(self)))

    def getValue(self, original=False):
        if "global" in self.type_semantics and original:
            return f"@{self.name}"
        elif original:
            return f"%{str(self.original_address)}"
        else:
            return f"%{str(self.temp_address)}"

class FunctionNode(ASTNode):
    def __init__(self, name, node_id):
        super().__init__(node_id)
        self.name = name
        self.type = None
        self.type_semantics = []
        self.original_address = None
        self.temp_address = None

    def __str__(self):
        return f"{self.name} ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterFunction(self)
        self.visitChildren(visitor)
        visitor.exitFunction(self)

    def getValue(self, original=False):
        if original:
            return "%" + self.original_address
        else:
            return "@" + self.name

    def alignment(self):
        return str(int(getAlignment(self)))


class DefinitionNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.type = None

    def __str__(self):
        return f"define ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterDefinition(self)
        self.visitChildren(visitor)
        visitor.exitDefinition(self)


class FunctionDefinitionNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.type = None

    def __str__(self):
        return f"define_func ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterFunctionDefinition(self)
        self.visitChildren(visitor)
        visitor.exitFunctionDefinition(self)


class UnaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation
        self.type = None
        self.type_semantics = []
        self.temp_address = None
        self.original_address = None

    def __str__(self):
        return f"{self.operation} ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterUnaryOperation(self)
        self.visitChildren(visitor)
        visitor.exitUnaryOperation(self)

    def fold(self, _type):
        # Calculate the result of the unary operation in order to fold, handle ! separately as this has different syntax in python
        if self.operation == '!':
            result = int(self.children[0].value == 0)
        else:
            result = eval(self.operation + str(self.children[0].value))
        # Replace this node by the calculated result
        new_node = LiteralNode(result, _type, self.id)
        new_node.parent = self.parent
        self.parent.children[self.parent.children.index(self)] = new_node

    def getValue(self, original=False):
        if original:
            return f"%{str(self.original_address)}"
        else:
            return f"%{str(self.temp_address)}"

    def alignment(self):
        return str(int(getAlignment(self)))


class BinaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation
        self.type = None
        self.type_semantics = []
        self.temp_address = None

    def __str__(self):
        return f"{self.operation} ({self.type})"

    def alignment(self):
        return str(int(getAlignment(self)))

    def accept(self, visitor:ASTVisitor):
        visitor.enterBinaryOperation(self)
        self.visitChildren(visitor)
        visitor.exitBinaryOperation(self)

    def fold(self, _type):
        # Calculate the result of the binary operation in order to fold
        child1 = self.children[0].value
        operation = self.operation.replace("&&", " and ").replace("||", " or ")
        child2 = self.children[1].value
        if self.operation in ["&&", "||"]:
            child1 = bool(child1)
            child2 = bool(child2)
        formula = str(child1) + operation + str(child2)
        result = float(eval(formula))
        # Replace this node by the calculated result
        new_node = LiteralNode(result, _type, self.id)
        new_node.parent = self.parent
        self.parent.children[self.parent.children.index(self)] = new_node

    def getValue(self):
        return f"%{str(self.temp_address)}"



class AssignmentNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'assign'

    def accept(self, visitor:ASTVisitor):
        visitor.enterAssignment(self)
        self.visitChildren(visitor)
        visitor.exitAssignment(self)


class DeclarationNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.type = None

    def __str__(self):
        return f"declare ({self.type})"

    def accept(self, visitor:ASTVisitor):
        visitor.enterDeclaration(self)
        self.visitChildren(visitor)
        visitor.exitDeclaration(self)

class FunctionDeclarationNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'declare_func'

    def accept(self, visitor:ASTVisitor):
        visitor.enterFunctionDeclaration(self)
        self.visitChildren(visitor)
        visitor.exitFunctionDeclaration(self)


class WhileNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.start_address = None

    def __str__(self):
        return 'while'

    def accept(self, visitor:ASTVisitor):
        visitor.enterWhile(self)
        self.visitChildren(visitor)
        visitor.exitWhile(self)


class BranchNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'branch'

    def accept(self, visitor:ASTVisitor):
        visitor.enterBranch(self)
        self.visitChildren(visitor)
        visitor.exitBranch(self)

class IfNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.start_address = None

    def __str__(self):
        return 'if'

    def accept(self, visitor:ASTVisitor):
        visitor.enterIf(self)
        self.visitChildren(visitor)
        visitor.exitIf(self)

class ElifNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'elif'

    def accept(self, visitor:ASTVisitor):
        visitor.enterElif(self)
        self.visitChildren(visitor)
        visitor.exitElif(self)

class ElseNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'else'

    def accept(self, visitor:ASTVisitor):
        visitor.enterElse(self)
        self.visitChildren(visitor)
        visitor.exitElse(self)

class BreakNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'break'

    def accept(self, visitor:ASTVisitor):
        visitor.enterBreak(self)
        self.visitChildren(visitor)
        visitor.exitBreak(self)

class ContinueNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'continue'

    def accept(self, visitor:ASTVisitor):
        visitor.enterContinue(self)
        self.visitChildren(visitor)
        visitor.exitContinue(self)

class ReturnNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'return'

    def accept(self, visitor:ASTVisitor):
        visitor.enterReturn(self)
        self.visitChildren(visitor)
        visitor.exitReturn(self)

class FunctionCallNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.temp_address = None

    def __str__(self):
        return 'func_call'

    def accept(self, visitor:ASTVisitor):
        visitor.enterFunctionCall(self)
        self.visitChildren(visitor)
        visitor.exitFunctionCall(self)

    def getValue(self):
        return f"%{str(self.temp_address)}"

class ArgListNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.children = []

    def __str__(self):
        return 'arguments'

    def accept(self, visitor:ASTVisitor):
        visitor.enterArgList(self)
        self.visitChildren(visitor)
        visitor.exitArgList(self)

class InitializerListNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)
        self.children = []
        self.dimensions = []

    def __str__(self):
        return 'initializer_list'

    def accept(self, visitor:ASTVisitor):
        visitor.enterInitializerList(self)
        self.visitChildren(visitor)
        visitor.exitInitializerList(self)