# problem-solving

![unittests](https://github.com/rafaeltardivo/problem-solving/workflows/unittests/badge.svg)

Programming exercises from [HackerRank](https://www.hackerrank.com/) and [Codility](https://www.codility.com/).

## Description

Every exercise should contain a docstring with its description and its asymptotic analysis, such as:

```python
"""Checks if two words could form an anagram by removing spaces,
    sorting and comparing them.

    Complexity: O(nlogn), since both words are sorted.

    Args:
        word_one (str): first word to be compared.
        word_two (str): second word to be compared.
    Returns:
        True if they are an anagram. False if not.
"""
```

Also, **every solution should have at least one unit test** ;)

## Using pre-commit

pre-commit is a group os scripts that are added in the `pre-commit` hook in your local git repo. What means that every time you type `git commit` those script will be executed, checking and improving the code quality and pattern.

More information at: https://pre-commit.com/

1) Install pre-commit following this guide: https://pre-commit.com/#installation
2) Install the hooks on your project: In your local repository, run: `pre-commit install`
3) Test if it's working fine running `pre-commit run`
