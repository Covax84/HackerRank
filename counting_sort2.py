#!/bin/python3
# Why all these imports?!
import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def counting_sort2(arr: list) -> list:
    """ Counting sort. Now the actual one.
        Step 1: frequency analysis, step 2: building sorted array.
    """
    freq = [0] * 100
    sorted_arr = []
    for digit in arr:
        freq[digit] += 1
    for i in range(len(freq)):
        if freq[i] != 0:
            sorted_arr += [i] * freq[i]
    return sorted_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = counting_sort2(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

test_arr = [0, 2, 1, 2, 3, 4, 5, 6, 7, 12, 12, 4, 5, 6, 7, 8, 9, 0]
print(counting_sort2(test_arr))
