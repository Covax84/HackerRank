def counting_valleys(n: int, s: str) -> int:
    """ Input: n - number of steps (climb or descend the mountain)
               s - steps sequence (U is for climbing, D is for descending)
        Output: number of valleys

        Default starting level is 0(sea level), there is
        a valley if we climb up from the pit to sea level.
    """
    current_level = 0
    valley_counter = 0
    for i in s:
        if i == 'U':
            current_level += 1
            if current_level == 0:
                valley_counter += 1
        elif i == 'D':
            current_level -= 1
    return valley_counter


# example_route = 'UDDUDUDDUU'
# counting_valleys(len(example_route), example_route)
