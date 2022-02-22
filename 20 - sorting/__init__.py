#!/bin/python3

import math
import os
import random
import re
import sys


def swap(arr, index):
    tmp = arr[index]
    arr[index] = arr[index + 1]
    arr[index + 1] = tmp


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    total_swaps = 0

    for i in range(n):
        numberOfSwaps = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swap(a, j)
                numberOfSwaps += 1
        total_swaps += numberOfSwaps

    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(total_swaps, str(a[0]),
                                                                                     str(a[n - 1])))
