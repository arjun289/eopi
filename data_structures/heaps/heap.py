CAPACITY = 20


class Heap:

    def __init__(self):
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    def insert(self, item):

        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1
        self.heapify_up(self.heap_size - 1)

    def heapify_up(self, index):
        parent_index = (index-1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.heapify_up(parent_index)
   
    def get_max(self):
        return self.heap[0]

    def swap(self, index_1, index_2):
        self.heap[index_2], self.heap[index_1] = self.heap[index_1], \
            self.heap[index_2]

    def poll(self):
        max = self.get_max()
        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size - 1
        self.fix_down(0)

        return max

    def fix_down(self, index):

        index_left = 2 * index + 1
        index_right = 2 * index + 2
        largest_index = index

        if index_left < self.heap_size and self.heap[index_left] > \
                self.heap[largest_index]:
            largest_index = index_left
        
        if index_right < self.heap_size and self.heap[index_right] > \
                self.heap[largest_index]:
            largest_index = index_right

        if index != largest_index:
            self.swap(index, largest_index)
            self.fix_down(largest_index)

    def heap_sort(self):
        size = self.heap_size

        for i in range(0, size):
            max = self.poll()
            print(max)


if __name__ == "__main__":
    heap = Heap()

    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(300)

    heap.heap_sort()
