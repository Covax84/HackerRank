def factorial(n: int):
    """Calculate factorial n. Recurrent function."""
    if n < 0:
        raise ValueError('Expected n >= 0')
    elif n == 0:
        return 1
    return factorial(n - 1) * n
