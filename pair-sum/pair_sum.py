
def pair_sum(numbers, expected_result):
    """Find pairs which sum results in expected_result.

        Complexity: O(n^2), since both words are sorted.

        Args:
            numbers(list): list of numbers.
            expected_result(int): expected result for pairs.
        Return:
            list containing pairs whose sum matches expected_result.
    """
    pairs = list()
    size = len(numbers)
    
    for i in range(size - 1):
        lower_bound = i
        j = size -1
        
        while(j > lower_bound):
            pair = numbers[i] + numbers[j]
            if pair == expected_result:
                pairs.append((numbers[i], numbers[j]))
            j -= 1
    return pairs


if __name__ == '__main__':
    print(pair_sum([4, 1, 2,  5, 3], 6))
