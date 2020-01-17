from list import ListNode, MyList


def iterate_and_find_overlap(bigger_list, smaller_list, skip_length):
    large_iter, small_iter = bigger_list.head, smaller_list.head

    for _ in range(skip_length):
        large_iter = large_iter.next

    while large_iter and small_iter:
        if large_iter is small_iter:
            return True
        large_iter = large_iter.next
        small_iter = small_iter.next
    
    return False

            
def overlap_non_cycle(list1, list2):
    len1 = list1.length()
    len2 = list2.length()

    if len1 > len2:
        length = len1 - len2
        return iterate_and_find_overlap(list1, list2, length)
    else:
        length = len2 - len1
        return iterate_and_find_overlap(list2, list1, length)
    

def overlap_maybe_cycle(list1: MyList, list2: MyList):
    root1, root2 = list1.has_cycle(), list2.has_cycle()

    # they don't have cycle
    if not root1 and not root2:
        overlap_non_cycle(list1, list2)
    # one of it does not have a cycle
    elif (root1 and not root2) or (root2 and not root1):
        return None

    # both have cycle
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break

    # If both cycles are disjoint 
    if temp is not root1:
        return None
    
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    # L1 and L2 in same cycle, locate overlapping node if they
    # first overlap before cycle starts.
    stem1_length, stem2_length = distance(list1, root1), distance(list2, root2)
    if stem1_length > stem2_length:
        list2, list1 = list1, list2
    
    for _ in range(abs(stem1_length - stem2_length)):
        list2 = list2.next

    while list1 is not list2 and list1 is not root1 and list2 is not root2:
        list1, list2 = list1.next, list2.next

    return list1 if list1 is list2 else root1


if __name__ == "__main__":
    node1_1 = ListNode(1)

    listing1 = MyList(node1_1)
    node2_1 = ListNode(2)
    node1_1.next = node2_1
    node3_1 = ListNode(3)
    node2_1.next = node3_1

    print("lenght list 1: " + str(listing1.length()))

    node1_2 = ListNode(5)
    listing2 = MyList(node1_2)
    node2_2 = ListNode(7)
    node1_2.next = node2_2
    node3_2 = ListNode(8)
    node2_2.next = node3_2
    node4_2 = ListNode(9)
    node3_2.next = node4_2

    # create overlap without loop
    node3_1.next = node3_2

    print("lenght list 2: " + str(listing2.length()))
    print("list has overlap " + str(overlap_non_cycle(listing1, listing2)))
