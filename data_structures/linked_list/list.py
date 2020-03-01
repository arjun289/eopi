class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data) + "->"


class MyList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def length(self):
        step, node = 0, self.head
        while node:
            step += 1
            node = node.next
        return step

    def size(self):
        self.size
            
    def search_list(self, key):
        L = self.head
        while L and L.data != key:
            L = L.next

        return L

    def __str__(self):
        L = self.head
        string = ""
        while L:
            string = string + str(L.data) + "->"
            L = L.next
        return string + "Null"

    # O(1)
    def insertStart(self, node):
        self.size += 1

        if self.head:
            node.next = self.head.next
            self.head = node
        else:
            self.head = node

    def insertEnd(self, node):
        self.size += 1
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.head = node

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_after(self, node):
        if node.next is not None:
            L = node.next
            node.next = L.next
            L.next = None

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def deletion_from_list(self, node_to_delete):
        temp_node = node_to_delete.next
        node_to_delete.data = temp_node.data
        node_to_delete.next = temp_node.next
        temp_node.next = None

    def delete_kth_last(self, k):
        iter_1 = self.head
        for _ in range(k):
            iter_1 = iter_1.next
        
        iter_2 = self.head
        while iter_1:
            iter_1 = iter_1.next
            iter_2 = iter_2.next

        iter_2.next = iter_2.next.next

    def has_cycle(self):
        fast = slow = self.head

        def cycle_len(end):
            start, step = end, 0
            while True:
                step += 1
                start = start.next
                if start is end:
                    return step

        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

            if slow is fast:
                # move an iterator till cycle length
                cycle_len_iter = self.head
                for _ in range(cycle_len(slow)):
                    cycle_len_iter = cycle_len_iter.next
                
                # take another iter from head and move the cycle_len_iter in 
                # tandem
                it = self.head
                while it is not cycle_len_iter:
                    it = it.next
                    cycle_len_iter = cycle_len_iter.next
                return it
        
        return None

    def cyclic_right_shift(self, length):
        
        if not self.head:
            return
        list_length = self.length()
        if length > list_length:
            length = length % list_length

        head = self.head
        iter_head, iter_tail = head, head

        for _ in range(length):
            iter_tail = iter_tail.next
        
        while iter_tail.next is not None:
            iter_head = iter_head.next
            iter_tail = iter_tail.next
        
        temp = iter_head.next
        iter_head.next = None
        iter_tail.next = head
        self.head = temp


if __name__ == "__main__":
    node1 = ListNode(1)

    listing = MyList(node1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3

    print(listing)
    print(listing.length())
    listing.cyclic_right_shift(5)
    
    print(listing)