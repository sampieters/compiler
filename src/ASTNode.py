class ASTNode:
    def __init__(self):
        self.parent = None
        self.children = None

    def set_parent(self, node):
        assert self.parent is None
        self.parent = node

    def add_child(self, node):
        if not self.children:
            self.children = [node]
        else:
            self.children.append(node)

    def to_dot(self, filename):
        pass


class LiteralNode(ASTNode):
    def __init__(self, value):
        self.parent = None
        self.children = None
        self.value = value




class UnaryOperationNode(ASTNode):
    def __init__(self, operation):
        self.parent = None
        self.children = None
        self.operation = operation




class BinaryOperationNode(ASTNode):
    def __init__(self, operation):
        self.parent = None
        self.children = None
        self.operation = operation