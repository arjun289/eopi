def count_bits(x):
    """
    Returns number of bits set to 1 in a digit.

    Example
    -------
    3 = 0011b
    count_bits(3) = 2
    """

    num_bits = 0

    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def digit_sign(digit):
    """
    Returns the sign of the digit.
    """
    return -(digit < 0)


if __name__ == "__main__":
    print(digit_sign(3))
