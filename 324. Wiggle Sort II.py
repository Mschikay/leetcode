# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?



class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         def split(l, r):
#             buck = l
#             buckv = nums[l]
#             i, j = l, r
#             while i < j:
#                 while i < j and nums[j] > buckv:
#                     j -= 1
#                 nums[buck], buck = nums[j], j
#                 while i < j and nums[i] <= buckv:
#                     i += 1
#                 nums[buck], buck = nums[i], i
#             nums[buck] = buckv
#             return buck

#         l, r = 0, len(nums) - 1
#         m = (l + r) // 2
#         while l <= r:
#             mid = split(l, r)
#             if mid < m:
#                 l = mid + 1
#             else:
#                 r = mid - 1

        x = sorted(nums)
        idx = len(nums) - 1
        for i in range(1, len(nums), 2):
            nums[i] = x[idx]
            idx -= 1
        for i in range(0, len(nums), 2):
            nums[i] = x[idx]
            idx -= 1