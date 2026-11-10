class Node:
    def __init__ (self, data):
        self.data = data
        self.children = []

# Membuat Node 
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# Menghubungkan node
A.children = [B, C]
B.children = [D, E]
C.children = [F]