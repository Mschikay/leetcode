class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == None or nums == []:
            return []

        currMax = [nums[0]]
        currMin = [nums[0]]
        for n in range(1, len(nums)):
            currMax.append(max(max(currMax[n - 1] * nums[n], currMin[n - 1] * nums[n]), nums[n]))
            currMin.append(min(min(currMax[n - 1] * nums[n], currMin[n - 1] * nums[n]), nums[n]))

        return max(currMax)



