class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        N = len(nums)
        minp = [nums[0]] * N
        maxp = [nums[0]] * N
        res = nums[0]
        for i in range(1, len(nums)):
            minp[i] = min(nums[i], minp[i - 1] * nums[i], maxp[i - 1] * nums[i])
            maxp[i] = max(nums[i], minp[i - 1] * nums[i], maxp[i - 1] * nums[i])
            res = max(res, maxp[i])
        return res
