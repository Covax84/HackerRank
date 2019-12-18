def repeated_string(s: str, n: int) -> int:
    """ Input: string(s) of characters(repeated infinitely many times)
        and number(n)
        Output: number of 'a' in the first n characters in an infinite string
    """
    if n > len(s):
        return s.count('a') * (n // len(s)) + s[:int(n % len(s))].count('a')
    return s[:n].count('a')


# string = 'aba'
# number = 10
# print(repeated_string(string, number))
