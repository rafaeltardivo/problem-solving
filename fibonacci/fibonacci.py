def n_fibonacci(n):
    """Recursively returns fibonacci sequence from n to 0.

    Complexity: O(n).

    Args:
        n(int): number for sequence calculation.
    Returns:
        sequence sum.
    """
    if n <= 1:
        return n
    return n_fibonacci(n - 1) + n_fibonacci(n - 2)


cache = dict()


def n_dynamic_fibonacci(n):
    """Recursively returns fibonacci sequence from n to 0.
        Uses memoization for better performance.

    Complexity: O(n).

    Args:
        n(int): number for sequence calculation.
    Returns:
        sequence sum.
    """
    if n <= 1:
        return n

    if not cache.get(n):
        cache[n] = n_dynamic_fibonacci(n - 1) + n_dynamic_fibonacci(n - 2)

    return cache[n]
