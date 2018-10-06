# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def last_dig_of_sum_of_fib(n):
    """
    fib(1) + fib(2) + ... + fib(n) = fib(n+2)-1
    """
    if n < 2:
        return n

    p_period = 60
    n %= p_period

    arr = [1, 1]
    for _ in range(n):
        arr.append((arr[-1] + arr[-2]) % 10)

    return (arr[-1] - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(last_dig_of_sum_of_fib(n))
