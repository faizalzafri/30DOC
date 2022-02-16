#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

current_count = 0;
max_count = 0;

while n >= 1:
    rem = n % 2
    if rem == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
    n = n // 2
print(max_count)
