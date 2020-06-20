class Vertex:
    def __init__(self, name):
        self.name = name
        self.node = None


class Node:
    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        self.weight = weight

    def __cmp__(self, other_edge):
        return self.cmp(self.weight, other_edge.weight)

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class DisjoinSet:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = []
        self.node_count = 0
        self.set_count = 0
        self.make_sets(vertex_list)

    def find(self, node):
        current_node = node

        while current_node.parent_node is not None:
            current_node = current_node.parent_node

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id
    
    def merge(self, node_1, node_2):
        index1 = self.find(node_1)
        index2 = self.find(node_2)

        if index1 == index2:
            return
        
        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.height < root2.height:
            root1.parent_node = root2
        elif root1.height > root2.height:
            root2.parent_node = root1
        else:
            root1.parent_node = root2
            root2.height = root2.height + 1

    def make_sets(self, vertex_list):
        for v in vertex_list:
            self.make_set(v)

    def make_set(self, vertex):
        node = Node(0, len(self.root_nodes), None)
        vertex.node = node
        self.root_nodes.append(node)
        self.set_count = self.set_count + 1
        self.node_count = self.node_count + 1


class KruskalAlgorithm:
    def spanning_tree(self, vertex_list, edge_list):
        disjoint_set = DisjoinSet(vertex_list)
        spanning_tree = []

        edge_list.sort()

        for edge in edge_list:
            u = edge.start_vertex
            v = edge.target_vertex

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                spanning_tree.append(edge)
                disjoint_set.merge(u.node, v.node)

        for edge in spanning_tree:
            print(edge.start_vertex.name, " - ", edge.target_vertex.name)


vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)


vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)
vertexList.append(vertex7)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)

algorithm = KruskalAlgorithm()
algorithm.spanning_tree(vertexList, edgeList)			
