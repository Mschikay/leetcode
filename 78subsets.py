import copy
from pprint import pprint


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return None

        if nums == []:
            return []

        result = [[]]
        return self.recursive(nums, [], 0, result)

    def recursive(self, nums, subset, offset, result):
        for n in range(offset, len(nums)):
            result.append(subset + [nums[n]])
            self.recursive(nums, subset + [nums[n]], n + 1, result)

        return result


if __name__ == '__main__':
    s = Solution()
    pprint(s.subsets([1, 2, 3]))
