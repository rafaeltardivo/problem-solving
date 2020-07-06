def n_missing_element(array_one, array_two):
    """Find the missing element between two sets.

        Complexity: O(N).

        Args:
            array_one (list): first list of numbers to be compared.
            array_two (list): second list of numbers to be compared.
        Returns:
            list containing differences.
    """
    one = set(array_one)
    two = set(array_two)
    return list(one.difference(two))


def n_missing_element_dic(array_one, array_two):
    """Find the missing element between two sets.

        Complexity: O(N).

        Args:
            array_one (list): first list of numbers to be compared.
            array_two (list): second list of numbers to be compared.
        Returns:
            list containing differences.
    """
    element_counter = dict()
    differences = list()

    for item in array_one:
        if item not in element_counter:
            element_counter[item] = 1
        else:
            element_counter[item] += 1

    for item in array_two:
        if item not in element_counter:
            element_counter[item] = 1
        else:
            element_counter[item] -= 1

    for item in element_counter:
        if element_counter[item] != 0:
            differences.append(item)

    return differences
