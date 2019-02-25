class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or nums == []:
            return []

        currMax = [nums[0]]
        for n in range(1, len(nums)):
            currMax.append(max(nums[n], nums[n] + currMax[n - 1]))
        return max(currMax)
