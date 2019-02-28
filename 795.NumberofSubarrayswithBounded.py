class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        start = end = -1
        res = 0

        for i in range(len(A)):
            if A[i] < L:
                i += 1
                res += end - start
                continue

            if A[i] > R:
                start = end = i
                continue

            end = i
            res += end - start
        return res