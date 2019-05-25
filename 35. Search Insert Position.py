class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid - 1
                if h < l:
                    return h + 1
            elif nums[mid] < target:
                l = mid + 1
                if l > h:
                    return l
