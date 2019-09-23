# Separate an array of numbers [1,2,3,4,5] into a set of even and
# odd partitions [1,2,3,4,5] => [2,4,1,3,5].


def even_odd_filter(source):
    next_even, next_odd = 0, len(source) - 1

    while next_even < next_odd:
        if source[next_even] % 2 == 0:
            next_even += 1
        else:
            source[next_even], source[next_odd] = source[next_odd], source[
                                                                      next_even
                                                                    ]
            next_odd -= 1
    return source


if __name__ == "__main__":
    check_list = [1, 2, 3, 4, 5]
    new_list = even_odd_filter(check_list)

    print(new_list)
