# Write a program which takes an array of n integers, where A[i] denotes the
#  maximum you can advance from index l, and retums whether it is possible to
# advance to the last index starting from the beginning of the array.


def can_reach_end(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        i += 1

    return furthest_reach_so_far >= last_index

# Write a program which takes as input a sorted array and updates it so that
# all duplicates have been removed and the remaining elements have been shifted
# left to fill the emptied indices. Return the number of valid elements.


def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index
    
