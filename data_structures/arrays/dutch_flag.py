# Write a program that takes an array A and an index i into A, and rearranges
# the elements such that all elements less than A[r] (the "pivot") appear
# first, followed by elements equal to the pivot, followed by elements greater
# than the pivot.


def dutch_flag_partition(pivot_index, arr):
    low = 0
    high = len(arr) - 1
    pivot = arr[pivot_index]

    while low < high:
        while True:
            if arr[low] < pivot:
                low += 1
            else:
                break
        while True:
            if arr[high] >= pivot:
                high -= 1
            else:
                break
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]


# Assuming that keys take one of three values, reorder the array so that all
# objects with the same key appear together. The order of the subarrays is
# not important. For example, both Figures 5.1(b) and 5.1(c) on Page 40 are
# valid answers for Figure 5.1(a) on Page 40. Use O(1) additional
# sPace and o(n) time. key =?> 0,1,2
def object_same_key_together(arr):
    pivot1 = 0
    pivot2 = 0

    # find first occurence of 1
    for i in range(len(arr)):
        if arr[i] == 1:
            pivot1 = i
            break

    dutch_flag_partition(pivot1, arr)

    for i in range(len(arr)):
        if arr[i] == 2:
            pivot2 = i
            break

    dutch_flag_partition(pivot2, arr)


if __name__ == "__main__":
    arr = [0, 1, 2, 0, 2, 1, 1, 1, 2, 0, 0]
    object_same_key_together(arr)
    print(arr)
