class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l, h = 0, len(nums) - 1
        # while l < h:
        #     print(l)
        #     mid = (l + h) // 2
        #     if nums[mid] > nums[h]:
        #         l = mid + 1
        #     elif nums[mid] < nums[l]:
        #         h = mid
        #     elif nums[l] <= nums[mid] <= nums[h]:
        #         h -= 1
        # return nums[l]
        x = float("inf")
        for n in nums:
            x = min(x, n)
        return x