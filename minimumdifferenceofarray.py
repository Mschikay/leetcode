def solution1(A):
    # write your code in Python 3.6
    l = 0
    r = len(A) - 1
    sumL = A[l]
    sumR = A[r]
    while True:
        if sumL <= sumR:
            l += 1
            if l < r:
                sumL += A[l]
            else:
                return abs(sumL - sumR)
        else:
            r -= 1
            if l < r:
                sumR += A[r]
            else:
                return abs(sumL - sumR)


import sys


def solution(A):
    # write your code in Python 3.6
    minDiff = sum(A) - 2 * A[0]
    diff = sum(A) - 2 * A[0]

    for i in range(1, len(A)-1):
        diff = diff - 2 * A[i]
        minDiff = min(minDiff, abs(diff))

    return minDiff

print(solution1([1, 2, -3, -4, 5, 6]))