#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def percentage(whole, fraction):
    return (fraction / 100) * whole


def solve(meal_cost, tip_percent, tax_percent):
    tip = percentage(meal_cost, tip_percent)
    tax = percentage(meal_cost, tax_percent)
    total = round(meal_cost + tip + tax)
    print(total)


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
