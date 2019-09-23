def quick_sort(low, high, arr):
    if (low < high):
        p_index = partition(low, high, arr)
        quick_sort(low, p_index-1, arr)
        quick_sort(p_index+1, high, arr)


def partition(low, high, arr):
    """
    Paritioning based on taking the first element as pivot.
    """
    pivot = arr[low]
    pivot_index = low
    low += 1
    while(low < high):
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
        
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return high


if __name__ == "__main__":
    prob = [10, 9, 6, 15, 8, 3, 11, 10]
    quick_sort(0, len(prob) - 1, prob)
    print(prob)
