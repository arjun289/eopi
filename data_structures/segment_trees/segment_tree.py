from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        self.array = array
        
        length = len(array)
        height = (int)(ceil(log2(length)))
        max_size = 2 * (int)(2**height) - 1

        self.array_length = length
        self.segment_tree_length = max_size
        self.segment_tree = [0] * max_size
        self._build(0, 0, length-1)

    def _build(self, node, start, end):
        if start == end:
            self.segment_tree[node] = self.array[start]
        else:
            mid = (start+end) // 2
            self._build(2*node+1, start, mid)
            self._build(2*node+2, mid+1, end)

            self.segment_tree[node] = self.segment_tree[2*node+1] + \
                self.segment_tree[2*node+2]

    def update(self, index, value):
        if index < 0 or index > self.array_length:
            print("Invalid index")
            return -1

        self.array[index] = self.array[index] + value
        self._update_util(0, 0, self.array_length - 1, index, value)

    def _update_util(self, node, start, end, index, value):
        pass


if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11]
    sol = SegmentTree(array)
    print(sol.segment_tree)
