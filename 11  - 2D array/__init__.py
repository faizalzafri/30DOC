#!/bin/python3

import math
import os
import random
import re
import sys


def get_hourglass_sum(matrix, row, column):
    curr_sum = 0
    curr_sum += matrix[row - 1][column - 1]
    curr_sum += matrix[row - 1][column]
    curr_sum += matrix[row - 1][column + 1]
    curr_sum += matrix[row][column]
    curr_sum += matrix[row + 1][column - 1]
    curr_sum += matrix[row + 1][column]
    curr_sum += matrix[row + 1][column + 1]
    return curr_sum


if __name__ == '__main__':

    arr = []
    current_sum = 0;
    max_sum = -99
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(1, 5):
        for j in range(1, 5):
            current_sum = get_hourglass_sum(arr, i, j)
            if current_sum > max_sum:
                max_sum = current_sum

    print(max_sum)
