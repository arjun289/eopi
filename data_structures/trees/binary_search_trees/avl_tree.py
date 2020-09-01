class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def traverse(self):
        self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print("%s" % node.data)
        if node.right_child:
            self.traverse_in_order(node.right_child)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        return self.settle_violations(data, node)

    def delete(self, data):
        if self.root:
            self.root = self.delete_node(data, self.root)
    
    def delete_node(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.left_child = self.delete_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.delete_node(data, node.right_child)
        else:
            # node is leaf node
            if node.left_child is None and node.right_child is None:
                print("Removing leaf node")
                del(node)
                return None
            # node has right child
            if not node.right_child:
                print("Removing node with left child")
                temp_node = node.left_child
                del(node)
                return temp_node
            # node has left child
            if not node.left_child:
                print("Removing node with right child")
                temp_node = node.right_child
                del(node)
                return temp_node
            # node has two children
            else:
                print("Removing node with two children")
                temp_node = self.get_predecessor(self, node.left_child)
                node.data = temp_node.data
                node.left_child = self.delete_node(temp_node.data,
                                                   node.left_child)
        
        if not node:
            return node
        
        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        balance = self.check_balance(node)

        # left-left heavy situation
        if balance < 1 and self.check_balance(node.left_child) >= 0:
            return self.rotate_right(node)
        if balance < 1 and self.check_balance(node.left_child) < 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance > 1 and self.check_balance(node.right_child) <= 0:
            return self.rotate_left(node)
        if balance > 1 and self.check_balance(node.right_child) > 0:
            node.left_child = self.rotate_right(node.left_child)
            return self.rotate_left(node)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right)
        else:
            return node
        
    def settle_violations(self, data, node):
        balance = self.check_balance(node)

        # case 1 -> left-left heavy situation
        if balance > 1 and data < node.left_child.data:
            print("left-left heavy situtation...")
            return self.rotate_right(node)
        # case2 -> right-right heavy situation
        if balance < -1 and data > node.right_child.data:
            print("right-right heavy situtation...")
            return self.rotate_left(node)
        # case 3 -> left right heavy situation
        if balance > 1 and data > node.left_child.data:
            print("left right heavy situation...")
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        # case 4 -> right left heavy situation
        if balance < -1 and data < node.right_child.data:
            print("right left heavy situation")
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def calculate_height(self, node):
        if not node:
            return -1
        return node.height

    # if difference value > 1 it means it is left heavy situation
    # if difference value < -1 it means it is a right heavy situation
    def check_balance(self, node):
        if not node:
            return 0

        return self.calculate_height(node.left_child) - \
            self.calculate_height(node.right_child)

    def rotate_right(self, node):
        print("rotating to the right with the node ", node.data)
        temp_left = node.left_child
        in_pred = temp_left.right_child

        temp_left.right_child = node
        node.left_child = in_pred

        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        temp_left.height = max(self.calculate_height(temp_left.left_child),
                               self.calculate_height(temp_left.right_child)
                               ) + 1

        return temp_left

    def rotate_left(self, node):
        print("rotating to the right with the node ", node.data)
        temp_right = node.right_child
        in_suc = temp_right.left_child

        temp_right.left_child = node
        node.right_child = in_suc

        node.height = max(self.calculate_height(node.left_child),
                          self.calculate_height(node.right_child)) + 1
        temp_right.height = max(self.calculate_height(temp_right.left_child),
                                self.calculate_height(temp_right.right_child)
                                ) + 1
        
        return temp_right
    

avl = AVL()
avl.insert(1)
avl.insert(2)
avl.insert(3)

avl.traverse()
