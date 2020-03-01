
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    if root:
        print('Preorder: %d', root.data)
        tree_traversal(root.left)

        print('Inorder: %d', root.data)
        tree_traversal(root.right)

        print('Postorder: %d', root.data)


def inorder(root):
    if root.left:
        inorder(root.left)

    print(root.data)
 
    if root.right:
        inorder(root.right)
 
def is_balanced_binary_tree(root):


if __name__ == "__main__":
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    inorder(node1)