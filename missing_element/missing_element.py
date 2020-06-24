def missing_element(array_one, array_two):
    """Find the missing element between two sets.

        Complexity: O(1).

        Args:
            array_one (list): first list of numbers to be compared.
            array_two (list): first list of numbers to be compared.
        Returns:
            set containing differences.
    """
    one = set(array_one)
    two = set(array_two)
    return one.difference(two)

if __name__ == '__main__':
    print(missing_element([1, 2, 3, 4], [1, 2, 3]))

