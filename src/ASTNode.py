from utils import Counter
from ASTVisitor import ASTVisitor


class ASTNode:
    def __init__(self, node_id=0):
        self.id = node_id
        self.parent = None
        self.children = None

    def __str__(self):
        return "error"

    def accept(self, visitor:ASTVisitor) -> None:
        pass

    def set_parent(self, node):
        assert self.parent is None
        self.parent = node

    def add_child(self, node):
        if not self.children:
            self.children = [node]
        else:
            self.children.append(node)
        self.last_child().parent = self

    def last_child(self):
        return self.children[-1]

    def to_dot_recursive(self, file):
        if self.children is not None:
            for child in self.children:
                file.write("\tnode" + str(child.id) + "[label=\"" + str(child) + "\"]\n")
                file.write("\tnode" + str(self.id) + "->node" + str(child.id) + "\n")
                child.to_dot_recursive(file)

    def to_dot(self, filename):
        file = open(filename + ".dot", "w")
        file.write("digraph AST {\n")
        file.write("\tnode0[label=\"" + str(self) + "\"]\n")
        self.to_dot_recursive(file)
        file.write("}")


class ProgNode(ASTNode):
    def __init__(self, node_id=0):
        super().__init__(node_id)

    def __str__(self):
        return 'prog'

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitProg(self)


class LiteralNode(ASTNode):
    def __init__(self, value, node_id):
        super().__init__(node_id)
        self.value = value
        self.type = None

    def __str__(self):
        return str(self.value)

    def accept(self, visitor:ASTVisitor):
        visitor.visitLiteral(self)


class IdentifierNode(ASTNode):
    def __init__(self, name, node_id):
        super().__init__(node_id)
        self.name = name
        self.type = None

    def __str__(self):
        return self.name

    def accept(self, visitor:ASTVisitor):
        visitor.visitIdentifier(self)


class DefinitionNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'define'

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitDefinition(self)


class UnaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation

    def __str__(self):
        return self.operation

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitUnaryOperation(self)


class BinaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation

    def __str__(self):
        return self.operation

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitBinaryOperation(self)


class AssignmentNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'assign'

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitAssignment(self)

class DeclarationNode(ASTNode):
    def __init__(self, node_id):
        super().__init__(node_id)

    def __str__(self):
        return 'declare'

    def accept(self, visitor:ASTVisitor):
        for child in self.children:
            child.accept(visitor)
        visitor.visitDeclaration(self)
