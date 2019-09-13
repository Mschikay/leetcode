class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i = j = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            del nums[i + 1:j]
            j = i + 1
            i = j


class Solution(object):
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1
                nums[i] = nums[j]
        return i + 1