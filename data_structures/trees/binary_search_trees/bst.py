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

    def traverse(self, type):
        if self.root and type == "inorder":
            self.traverseInorder(self.root)
        elif self.root and type == "postorder":
            self.traversePostorder(self.root)
        else:
            self.traversePreorder(self.root)

    def traverseInorder(self, node):
        if node.left:
            self.traverseInorder(node.left)

        print("%s " % node.data)

        if node.right:
            self.traverseInorder(node.right)

    def traversePostorder(self, node):
        if node.left:
            self.traverseInorder(node.left)

        if node.right:
            self.traverseInorder(node.right)
        print("%s " % node.data)

    def traversePreorder(self, node):
        print("%s " % node.data)
        if node.left:
            self.traverseInorder(node.left)

        if node.right:
            self.traverseInorder(node.right)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(self.root, data)

    def removeNode(self, node, data):
        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(node.left, data)
        elif data > node.data:
            node.right = self.removeNode(node.right, data)
        else:
            if not node.left and not node.right:
                print("Removing a leaf node...")
                del node
                return None
            elif not node.left:
                print("Removing node with single right child...")
                temp = node.right
                del node
                return temp
            elif not node.right:
                print("Removing node with single left child...")
                temp = node.left
                del node
                return temp
            else:
                print("Removing node with two children...")
                temp = self.get_predecessor(node.left)
                node.data = temp.data
                node.left = self.removeNode(node.left, temp.data)
                return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node


bst = BinarySearchTree()
bst.insert("C")
bst.insert("A")
bst.insert("Z")
bst.insert("G")

bst.traverse("inorder")

bst.remove("C")
bst.traverse("inorder")
