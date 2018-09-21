# Uses python3
"""
input:  10
        7 5 14 2 8 8 10 1 2 3
output: 140

MaxPairwiseProductFast(A[1...n]):
    index ← 1
    for i from 2 to n:
        if A[i] > A[index1]:
            index1 ← i
    swap A[index] and A[n]
    index ← 1
    for i from 2 to n − 1:
        if A[i] > A[index]:
            index ← i
    swap A[index] and A[n − 1]
    return A[n − 1] · A[n]
"""


def max_pair_wise_product(s):
    # find the largest number in array and put it in the end
    idx = 1
    for i in range(2, len(s)):
        if s[i] > s[idx]:
            idx = i
    s[idx], s[-1] = s[-1], s[idx]

    # find the second largest number in array and put it in the second from end
    idx = 1
    for i in range(2, len(s) - 1):
        if s[i] > s[idx]:
            idx = i
    s[idx], s[-2] = s[-2], s[idx]

    return s[-2] * s[-1]


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)
    print(max_pair_wise_product(a))
