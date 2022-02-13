#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

template = '{} x {} = {} \n'
result = ''
for i in range(1, 11):
    product = n * i
    result = result + template.format(n, i, product)
print(result)
