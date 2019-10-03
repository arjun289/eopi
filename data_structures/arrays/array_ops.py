# increment an arbitary precision integer using arrays.
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i-1] += 1
        arr[i] = 0
    if arr[0] == 10:
        arr.append(0)
        arr[0] = 1
    return arr


if __name__ == "__main__":
    arr = [9, 9]
    print(plus_one(arr))
