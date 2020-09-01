class Node:
    def __init__(self, char):
        self.char = char
        self.end_char = False
        self.left_node = None
        self.middle_node = None
        self.right_node = None
        self.value = 0


class TST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value, 0)

    def put_item(self, node, key, value, index):
        c = key[index]

        if node is None:
            node = Node(c)

        if c < node.char:
            node.left_node = self.put_item(node.left_node, key, value, index)
        elif c > node.char:
            node.right_node = self.put_item(node.right_node, key, value, index)
        elif index < len(key) - 1:
            node.middle_node = self.put_item(node.middle_node, key, value,
                                             index+1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.get_item(self.root, key, 0)
        
        if node is None:
            return -1
        
        return node.value

    def get_item(self, node, key, index):
        if node is None:
            return None

        c = key[index]
        if c < node.char:
            node = self.get_item(node.left_node, key, index)
        elif c > node.char:
            node = self.get_item(node.right_node, key, index)
        elif index < len(key) - 1:
            node = self.get_item(node.middle_node, key, index + 1)
        else:
            return node

        return node


if __name__ == "__main__":
    tree = TST()
    tree.put("apple", 200)
    tree.put("orange", 100)

    print(tree.get("apple"))
