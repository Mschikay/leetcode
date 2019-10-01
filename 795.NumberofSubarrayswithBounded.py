class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        l = r = -1
        ans = 0
        for i in range(len(A)):
            if L <= A[i] <= R:
                r = i
            elif A[i] > R:
                l = r = i
            ans += r - l
        return ans


