# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def pisano_period(m):
    previous = 1
    current = 1

    result = 1
    while not (previous == 0 and current == 1):
        buffer = (previous + current) % m
        previous = current
        current = buffer

        result += 1
    return result


def fib_list(n, m):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % m)

    return arr[n]


def solution(n, m):
    return fib_list(n % pisano_period(m), m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(solution(n, m))
