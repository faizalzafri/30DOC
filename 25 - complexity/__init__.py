import math


def is_prime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False

    for x in range(2, int(sqrt_n + 1)):
        if n % x == 0:
            return False
    return True


cases = int(input())
for i in range(cases):
    nums = int(input())
    if is_prime(nums):
        print('Prime')
    else:
        print('Not prime')
