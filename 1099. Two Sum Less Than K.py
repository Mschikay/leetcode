class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        l, r = 0, len(A) - 1
        ans = -1
        while l < r:
            s = A[l] + A[r]
            if s < K:
                ans = max(ans, s)
                l += 1
            else:
                r -= 1
        return ans