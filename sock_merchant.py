def sock_merchant(n: int, ar: list) -> int:
    """ The task is to count pairs of socks, so we have:
        Input: array of integers (each one represents the color of each sock)
        Output: number of pairs of integers
    """
    socks_types = set(ar)
    counter = 0
    for sock in socks_types:
        counter += ar.count(sock) // 2
    return counter


# n = 9
# ar = [1, 1, 1, 2, 2, 3, 3, 4, 5]
# print(sock_merchant(n, ar))
