class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        counter = 0
        l = r = 0
        maxlen = 0
        while r < len(A):
            if not A[r]:
                counter += 1
            r += 1
            while l < r and counter > K:
                if not A[l]: counter -= 1
                l += 1
            maxlen = max(maxlen, r - l)

        return maxlen