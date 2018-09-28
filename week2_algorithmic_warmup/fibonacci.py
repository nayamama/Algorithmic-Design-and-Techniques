# Uses python3


# naive algorithm
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# bottom_up method
def fib_list(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append((arr[i - 1] + arr[i - 2]) % 10)

    return arr[n] % 10


n = int(input())
print(fib_list(n))
