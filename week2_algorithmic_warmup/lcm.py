# Uses python3
import sys
from functools import reduce


# naive method
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


# better method
def lcm_from_greater(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            res = greater
            break
        greater += 1

    return res


# lcm using gcd
def euclid_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm_using_gcd(a, b):
    return a * b // euclid_gcd(a, b)


# lcm of more than 2 numbers
def lcm_array(*args):
    return reduce(lcm_using_gcd, args)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_using_gcd(a, b))
    print(lcm_array(*range(1, 10)))

