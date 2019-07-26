# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def split(l, r):
            buck = l
            buckv = nums[l]
            i, j = l, r
            while i < j:
                while i < j and nums[j] > buckv:
                    j -= 1
                nums[buck], buck = nums[j], j
                while i < j and nums[i] <= buckv:
                    i += 1
                nums[buck], buck = nums[i], i
            nums[buck] = buckv
            return buck

        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            mid = split(l, r)
            if mid < m:
                l = mid + 1
            else:
                r = mid - 1
        print(nums)
        if not m % 2:
            j = m + 2
        else:
            j = m + 1
        i = 1
        while i < m + 1 and j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if not i % 2:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]