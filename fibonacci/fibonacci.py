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


if __name__ == '__main__':
    print(fibonacci(10))
   
