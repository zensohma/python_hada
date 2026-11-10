class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root = Node("A")
b = Node("B")
c = Node("C")

root.children.append(b)
root.children.append(c)


