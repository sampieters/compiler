class Counter:
    def __init__(self):
        self.counter = 0

    def incr(self):
        self.counter += 1

    def __str__(self):
        return str(self.counter)


class ASTNode:
    def __init__(self):
        self.parent = None
        self.children = None

    def __str__(self):
        return "Something went wrong"

    def set_parent(self, node):
        assert self.parent is None
        self.parent = node

    def add_child(self, node):
        if not self.children:
            self.children = [node]
        else:
            self.children.append(node)

    def to_dot_recursive(self, file, counter):
        if self.children is not None:
            for child in self.children:
                file.write("\tnode" + str(counter) + "[label=\"" + str(child) + "\"]\n")
                file.write("\tnode" + str(counter) + "->node")
                counter.incr()
                file.write(str(counter) + "\n")

            for child in self.children:
                child.to_dot_recursive(file, counter)

    def to_dot(self, filename):
        file = open(filename + ".dot", "w")
        file.write("digraph AST {\n")
        self.to_dot_recursive(file, Counter())
        file.write("}")


class LiteralNode(ASTNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)


class UnaryOperationNode(ASTNode):
    def __init__(self, operation):
        super().__init__()
        self.operation = operation

    def __str__(self):
        return self.operation


class BinaryOperationNode(ASTNode):
    def __init__(self, operation):
        super().__init__()
        self.operation = operation

    def __str__(self):
        return self.operation


test = ASTNode()
mult = BinaryOperationNode("*")
lit_1 = LiteralNode("3")
lit_1.set_parent(mult)
lit_2 = LiteralNode("4")
lit_2.set_parent(mult)
mult.set_parent(ASTNode)
mult.add_child(lit_1)
mult.add_child(lit_2)
test.add_child(mult)
test.to_dot("wow")
