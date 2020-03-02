class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            node = Node(data)
            self.root = node
        else:
            self.insertNode(data, self.root)

    # O(logN) if the tree is balanced.
    # worst case scenario can be O(N)
    def insertNode(self, data, parent):
        if data < parent.data:
            if parent.left is None:
                parent.left = Node(data)
            else:
                self.insertNode(data, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(data)
            else:
                self.insertNode(data, parent.right)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.left:
            return self.getMin(node.left)

        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.right:
            return self.getMax(node.right)

        return node.data
