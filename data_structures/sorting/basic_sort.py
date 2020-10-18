
def bubble_sort(array):
    if array == []:
        return []

    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def selection_sort(array):
    if array == []:
        return []

    length = len(array)
    for i in range(0, length - 1):
        index = i
        for j in range(i+1, length-1):
            if array[j] < array[index]:
                index = j

        if index is not i:
            array[i], array[index] = array[index], array[i]

    return array


def insertion_sort_other(array):
    if array == []:
        return []

    length = len(array)
    i = 1
    while i < length:
        j = i-1
        while array[j] > array[i] and j >= 0:
            j = j - 1
        
        if array[j+1] > array[i]:
            array[i], array[j+1] = array[j+1], array[i]
        else:
            i += 1

    return array


def insertion_sort(array):
    if array == []:
        return []

    length = len(array)
    i = 0
    while i < length:
        j = i

        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j = j-1
        
        i += 1

    return array


def merge_sort(array, low, high):
    if len(array) <= 1:
        return array
    
    partition_index = (low+high) // 2
    left_sub_array = array[low:partition_index]
    length_left = len(left_sub_array)
    right_sub_array = array[partition_index:high]
    length_right = len(right_sub_array)

    left = merge_sort(left_sub_array, 0, length_left)
    right = merge_sort(right_sub_array, 0, length_right)
    array = merge(left, right)
    return array


def merge(left_array, right_array):
    length_left = len(left_array)
    length_right = len(right_array)
    i = 0
    j = 0
    k = 0
    arr = [0] * (length_left + length_right)

    while i < length_left and j < length_right:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < length_left:
        arr[k] = left_array[i]
        i += 1

    while j < length_right:
        arr[k] = right_array[j]
        j += 1
    
    return arr


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot = partition(array, low, high)
    quick_sort(array, low, pivot - 1)
    quick_sort(array, pivot + 1, high)

    return array


def partition(array, low, high):
    partition_index = (low+high) // 2
    
    array[high], array[partition_index] = array[partition_index], array[high]

    i = low
    for j in range(low, high):
        if array[j] > array[high]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[high] = array[high], array[i]

    return i


if __name__ == "__main__":

    # arr = [3, 1, 6, 5, 2, 4]
    # arr = insertion_sort(arr, 0, len(arr) - 1)

    arr = [3, 1, 6, 5, 2, 4]
    arr = merge_sort(arr, 0, len(arr))

    print(arr)
