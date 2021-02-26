from utils import Counter

class ASTNode:
    def __init__(self, node_id=0):
        self.id = node_id
        self.parent = None
        self.children = None

    def __str__(self):
        return "prog"

    def set_parent(self, node):
        assert self.parent is None
        self.parent = node

    def add_child(self, node):
        if not self.children:
            self.children = [node]
        else:
            self.children.append(node)

    def to_dot_recursive(self, file):
        if self.children is not None:
            for child in self.children:
                file.write("\tnode" + str(child.id) + "[label=\"" + str(child) + "\"]\n")
                file.write("\tnode" + str(self.id) + "->node" + str(child.id) + "\n")
            #for child in self.children:
                child.to_dot_recursive(file)

    def to_dot(self, filename):
        file = open(filename + ".dot", "w")
        file.write("digraph AST {\n")
        file.write("node0[label=\"" + str(self) + "\"]\n")
        self.to_dot_recursive(file)
        file.write("}")


class LiteralNode(ASTNode):
    def __init__(self, value, node_id):
        super().__init__(node_id)
        self.value = value

    def __str__(self):
        return str(self.value)


class UnaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation

    def __str__(self):
        return self.operation


class BinaryOperationNode(ASTNode):
    def __init__(self, operation, node_id):
        super().__init__(node_id)
        self.operation = operation

    def __str__(self):
        return self.operation

counter = Counter()
test = ASTNode(counter.curr())
counter.incr()
mult = BinaryOperationNode("*", counter.curr())
counter.incr()
lit_1 = LiteralNode("3", counter.curr())
lit_1.set_parent(mult)
counter.incr()
lit_2 = LiteralNode("4", counter.curr())
lit_2.set_parent(mult)
mult.set_parent(ASTNode)
mult.add_child(lit_1)
mult.add_child(lit_2)
test.add_child(mult)
test.to_dot("wow")
