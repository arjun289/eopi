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
            if arr[low] <= pivot:
                low += 1
            else:
                break
        while True:
            if arr[high] > pivot:
                high -= 1
            else:
                break
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]


if __name__ == "__main__":
    arr = [0, 1, 2, 0, 2, 1, 1]
    dutch_flag_partition(3, arr)
    print(arr)
