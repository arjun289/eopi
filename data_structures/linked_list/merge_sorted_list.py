from list import MyList
from list import ListNode


def merge_sorted_list(L1, L2):
    head = tail = ListNode()
    L1, L2 = L1.head, L2.head

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    head = head.next

    return MyList(head)


if __name__ == "__main__":
    n1_3 = ListNode(7)
    n1_2 = ListNode(5, n1_3)
    n1_1 = ListNode(2, n1_2)

    L1 = MyList(n1_1)

    n2_3 = ListNode(6)
    n2_2 = ListNode(4, n2_3)
    n2_1 = ListNode(3, n2_2)

    L2 = MyList(n2_1)

    print(L1)
    print(L2)

    merged_list = merge_sorted_list(L1, L2)

    print(merged_list)
