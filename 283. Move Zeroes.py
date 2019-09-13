class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        while r < len(nums):
            while r < len(nums) and not nums[r]:
                r += 1
            if r < len(nums):
                nums[l] = nums[r]
                l += 1
                r += 1
        for i in range(l, len(nums)):
            nums[i] = 0
