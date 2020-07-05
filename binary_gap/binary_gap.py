def n_binary_gap(number):
    """Returns the greatest binary gap on the number.
    ex: The number 529 has binary representation 1000010001 and contains
    two binary gaps: one of length 4 and one of length 3.

    Complexity: O(n).

    Args:
        number (int): number to conver to be converted to binary.
    Returns:
        Length of the greatest gap or 0.
    """
    bin_repr = format(number, "b")
    size = len(bin_repr)

    for n in range(size - 1):
        if bin_repr[n] == "1":
            zeroes = bin_repr[n:].split("1")
            if len(zeroes) > 2:
                return len(max(zeroes))
            break
    return 0
