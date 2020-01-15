def biggest_hourglasses(arr: list) -> int:
    """ Input: 6 x 6 2D array of integers representing 16 hourglasses
        Output: the sum of the largest hourglasses in given array

        There is 16 hourglasses in 6 x 6 array: 1 1 1 0 0 0
                                                0 1 0 0 0 0
                                                1 1 1 0 0 0
                                                0 0 0 0 0 0
                                                0 0 0 0 0 0
                                                0 0 0 0 0 0

        Hourglasses graphical pattern: a b c
                                         d
                                       e f g

        Sum of hourglass is a sum of (a, b, c, d, e, f, g)

    """
    assert all(len(arr[x]) == 6 for x in range(len(arr))), '6 x 6 array expected, got:\n{}'.format(arr)

    hourglasses = []

    for i in range(0, 4):
        for j in range(0, 4):
            current_hourglasses = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hourglasses.append(current_hourglasses)
    return max(hourglasses)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(biggest_hourglasses(arr))
