class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def smallerThan(x):
            i, j, res = n - 1, 0, 0
            while i >= 0 and j < n:
                if matrix[i][j] > x:
                    i -= 1
                else:
                    res += i + 1
                    j += 1
            return res

        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo <= hi:
            mi = (hi - lo) // 2 + lo
            if smallerThan(mi) < k:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo


from heapq import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        h = []
        for i in range(len(matrix)):
            heappush(h, (matrix[i][0], i, 1))

        v, i, j = h[0]
        for _ in range(k - 1):
            if j < len(matrix):
                heapreplace(h, (matrix[i][j], i, j + 1))
            else:
                heappop(h)
            v, i, j = h[0]
        return v