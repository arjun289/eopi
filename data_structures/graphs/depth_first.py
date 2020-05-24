
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.prdecessor = None


class DFS:
    def dfs(self, node):
        node.visited = True
        print("%s" % node.name)

        for n in node.adjacency_list:
            if not n.visited:
                self.dfs(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node6)
node1.adjacency_list.append(node7)

node2.adjacency_list.append(node1)
node2.adjacency_list.append(node3)
node2.adjacency_list.append(node4)

node3.adjacency_list.append(node2)

node4.adjacency_list.append(node2)
node4.adjacency_list.append(node5)

node5.adjacency_list.append(node4)

node6.adjacency_list.append(node1)

dfs = DFS()

dfs.dfs(node1)