def jumping_on_clouds(c: list) -> int:
    """ Input: an array of clouds (map of allowed(0) and not allowed(1) positions(normal or thunder clouds))
        Output: minimal number of jumps to reach the last cloud (end of array) if jump length 1 or 2
    """
    costs = [0, 1] + [0] * (len(c) - 2)
    for i in range(2, len(c)):
        if c[i] == 1:
            costs[i] = float('inf')
            continue
        costs[i] = min(costs[i-1], costs[i-2]) + 1
    return costs[-1]


map = [0, 0, 1, 0, 0, 1, 0]
print(jumping_on_clouds(map))
