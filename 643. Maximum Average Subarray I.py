class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        a = s / k
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            a = max(a, s / k)
        return a