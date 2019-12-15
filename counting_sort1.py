#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def counting_sort1(arr: list) -> list:
    """ Not an actual counting sort.
        Just a frequency analysis.
    """
    freq = [0] * 100
    for digit in arr:
        freq[digit] += 1
    return freq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = counting_sort1(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
