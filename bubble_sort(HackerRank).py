def bubble_sort(a: list) -> None:
    """ Bubble sort with counter of swaps and print. """
    swaps = 0
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                swaps += 1
    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(swaps, a[0], a[-1]))


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

bubble_sort(a)
