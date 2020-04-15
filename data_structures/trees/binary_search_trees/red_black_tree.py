# BST data structure.
# One extra field which is color.
# Properties they have to satisfy:
# 1. Every node is either red or black.
# 2. The root and the leaves are all black(nils). All nodes not having a child
#    are made to point to nil children.
# 3. Every red node has black parent.
# 4. All simple path(which means no vertices are repeated) from a node x to a
#    descendant leaf of x, all such paths have same number of black nodes on
#    them. #black nodes = black_height(x) which does not include x itself.
# 5. Every internal node has 2-4 children(done by merging the child red nodes
#    into the parent black node).
# 6. every leaf has same depth namely black_height(root)
# red black trees have height h <= 2log(n+1) = O(log(n))

# Queries -> search, min, max, successor, predecessor
# Updates(Inserts and deletes) ->
#   - BST operations
#   - color changes
#   - restructuring of links via rotations

# Rotation


class node:

    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class red_black:

    def __init__(self, root):
        self.root = root
