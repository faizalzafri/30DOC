#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    reverse_arr = [int(arr[n - i - 1]) for i in range(n)]
    output_string = ''
    for i in reverse_arr:
        output_string += str(i) + ' '
    print(output_string)
