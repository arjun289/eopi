# Write an Aletrnation program that takes an array A of n numbers, and
# rearranges A's elements to get a new array having the property that
# B[0] <= B[1] >= Bl2 <= B[3] >= B[4] <= B[5] >= ....


def alternation(numbers):
    arr_len = len(numbers)
    for i in range(arr_len-1):
        if i % 2 == 0 and numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        elif i % 2 != 0 and numbers[i] < numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


def alternation_1(numbers):
    for i in range(len(numbers)):
        numbers[i:i+2] = sorted(numbers[i:i+2], reverse=i % 2)
    return numbers


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(alternation_1(numbers))
