def fibonacci(n):
    """Recursively returns fibonacci sequence from n to 0.
    Args:
        n(int): number for sequence calculation.
    Returns:
        sequence sum.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


cache = dict()
def dynamic_fibonacci(n):
    """Recursively returns fibonacci sequence from n to 0.
        Uses memoization for better performance.
    Args:
        n(int): number for sequence calculation.
    Returns:
        sequence sum.
    """
    if n <= 1:
        return n

    if not cache.get(n):
        cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)

    return cache[n]

if __name__ == '__main__':
    print(fibonacci(10))
    print(dynamic_fibonacci(10))
   
