class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        nums.sort()
        dp = [[-1, 0] for i in range(len(nums))]
        dp[0] = [-1, 1]
        for i in range(1, len(nums)):
            loc, l = -1, 0
            for j in range(i):
                if not (nums[i] % nums[j]):
                    if dp[j][1] > l:
                        l = dp[j][1]
                        loc = j
            dp[i] = [loc, l + 1]

        loc, l = 0, 0
        for i in range(len(dp)):
            if dp[i][1] > l:
                loc, l = i, dp[i][1]
        ans = []
        while loc > -1:
            ans.append(nums[loc])
            loc = dp[loc][0]
        return ans[::-1]