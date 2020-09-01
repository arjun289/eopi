# O(n) solution
def find_median(array1, array2):
    if array2 == [] and array1 == []:
        return None

    i = j = k = 0
    arr = [0] * (len(array1) + len(array2))

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            arr[k] = array1[i]
            i += 1
        else:
            arr[k] = array2[j]
            j += 1
        k += 1

    while i < len(array1):
        arr[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        arr[k] = array2[j]
        j += 1
        k += 1

    length = len(arr)

    if length % 2 == 0:
        return (arr[length // 2] + arr[(length // 2) - 1])/2
    else:
        return arr[length // 2]


if __name__ == "__main__":
    array1 = [1, 3, 4, 6]
    array2 = [2, 5, 7]

    result = find_median(array1, array2)
    print(result)
