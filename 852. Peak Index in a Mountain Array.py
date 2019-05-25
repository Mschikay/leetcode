class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, h = 0, len(A) - 1
        while l < h:
            mid = (l + h) // 2
            if A[mid] > A[mid + 1]:
                h = mid
            else:
                l = mid + 1
        return l
