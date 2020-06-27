def nsmaller_item(array_one, array_two):
    """Find the smaller element of each array.

        Complexity: O(N).

        Args:
            array_one (list): first list of numbers to be compared.
            array_two (list): second list of numbers to be compared.
        Returns:
            smaller number of each array.
    """
    size = len(array_one)

    for i in range(size - 1):
        if array_one[i] > array_one[i + 1]:
            smaller_one = array_one[i + 1]

    size = len(array_two)
    
    for i in range(size - 1):
        if array_two[i] > array_two[i + 1]:
            smaller_two = array_two[i + 1]

    return smaller_one, smaller_two


if __name__ == '__main__':
    print(nsmaller_item([3, 5, 1, 2, 22], [2, 4, 1, 7, 9]))