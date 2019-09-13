
'''dp'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = [[float("inf") for i in range(len(nums))] for j in range(m + 1)]
        pre = [nums[0]]
        for n in nums[1:]: pre.append(pre[-1] + n)
        for i in range(len(dp[0])):
            dp[1][i] = pre[i]
        for i in range(2, m + 1):
            for j in range(i - 1, len(dp[0])):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], pre[j] - pre[k]))

        return dp[m][-1]


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def subarrays_less_than_m(maximum):
            s = 0
            arrays = 1
            for n in nums:
                s += n
                if s > maximum:
                    s = n
                    arrays += 1

            return arrays

        l, h = max(nums), sum(nums)
        while l <= h:
            mid = (l + h) // 2
            if subarrays_less_than_m(mid) > m:
                l = mid + 1
            else:
                h = mid - 1
        return l