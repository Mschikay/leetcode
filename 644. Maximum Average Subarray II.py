# Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# Note:
#
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p = [nums[0]]
        for i in range(1, len(nums)):
            p.append(p[-1] + nums[i])

        def check(n):
            s = p[k - 1] - n * k
            if s >= 0: return True
            m = 0
            for i in range(k, len(nums)):
                s += nums[i] - n
                m = min(m, p[i - k] - (i - k + 1) * n)
                if s - m >= 0: return True
            return False

        h, l = max(nums), min(nums)
        while h - l > 0.00001:
            m = (h + l) / 2
            if check(m):
                l = m
            else:
                h = m
        return l
