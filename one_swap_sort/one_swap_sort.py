def is_one_swap_sort(array):
    """Find if is possible to sort the array with only one swap.

        Complexity: O(N).

        Args:
            array_one (list): first list of numbers to be compared.
        Returns:
            True if is possible to sort with only one swap. False if
            is not.
    """
    size = len(array)
    swaps = 0

    for i in range(size - 1):
        if array[i] > array[i + 1]:
            swaps += 1
        if swaps > 1:
            break
    
    return swaps <= 1


if __name__ == '__main__':
    print(is_one_swap_sort([0, 1, 6, 5, 4]))