class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data) + "->"


class MyList:

    def __init__(self, head=None):
        self.head = head

    def length(self):
        step, node = 0, self.head
        while node:
            step += 1
            node = node.next
        return step
            
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


if __name__ == "__main__":
    node1 = ListNode(1)

    listing = MyList(node1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3

    listing.insert_after(node2, ListNode(4))
    print(listing)
    print(listing.has_cycle())
    node3.next = node2
    print(listing.has_cycle())
