class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find(l, h):
            if l == h:
                return l
            mid = (l + h) // 2
            if nums[mid] > nums[mid + 1]:
                return find(l, mid)
            return find(mid + 1, h)

        return find(0, len(nums) - 1)
