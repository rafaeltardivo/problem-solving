def nlogn_anagram(word_one, word_two):
    """Checks if two words could form an anagram by removing spaces,
    sorting and comparing them.

    Complexity: O(nlogn), since both words are sorted.

    Args:
        word_one (str): first word to be compared.
        word_two (str): second word to be compared.
    Returns:
        True if they are an anagram. False if not.
    """
    if len(word_one) != len(word_two):
        return False

    word_one = word_one.replace(" ", "")
    word_two = word_one.replace(" ", "")
    return sorted(word_one) == sorted(word_two)


def n_anagram(word_one, word_two):
    """Checks if two words could form an anagram by removing spaces,
    sorting and comparing them.

    Complexity: O(n).

    Args:
        word_one (str): first word to be compared.
        word_two (str): second word to be compared.
    Returns:
        True if they are an anagram. False if not.
    """
    word_one = word_one.replace(" ", "")
    word_two = word_one.replace(" ", "")

    if len(word_one) != len(word_two):
        return False

    letter_counter = dict()

    for letter in word_one:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    for letter in word_two:
        if letter in letter_counter:
            letter_counter[letter] -= 1
        else:
            letter_counter[letter] = 1

    for key in letter_counter:
        if letter_counter[key] != 0:
            return False

    return True
