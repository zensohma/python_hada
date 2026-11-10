class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    if data < root.data:
        root.left = insert(root.right, data)

    return root

def search(root, target):

    if root is None:
        return False

    if target == root.data:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


root = None

data = [10, 5, 20, 3, 7, 15, 30]

for x in data:
    root = insert(root, x)

print(search(root, 5))
print(search(root, 100))