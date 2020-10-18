def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def palindrome(str):
    start = 0
    end = len(str) - 1

    while start < end:
        if str[start] == str[end]:
            start += 1
            end -= 1 
            continue
        else:
            return -1

    return 0


def is_palindrome_python(str):
    rev_str = str[::-1]

    if str == rev_str:
        return 0
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("before")
    print(arr)
    arr = reverse_array(arr)
    print("after")
    print(arr)

    str = 'radar'
    print(is_palindrome_python(str))
