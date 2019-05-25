class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = nums[-1]
        l, h = 0, len(nums) -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > end:
                l = mid + 1
            if nums[mid] <= end:
                h = mid - 1
        return nums[l]