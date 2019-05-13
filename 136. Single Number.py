from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # i, j = 0, 1
        # while j < len(nums):
        #     if nums[i] == nums[j]:
        #         i += 2
        #         j = i + 1
        #         continue
        #     return nums[i]
        # return nums[i]

        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] = d[n] + 1
        for k in d.keys():
            if d[k] == 1:
                return k