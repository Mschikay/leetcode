import operator


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #         pairs = [[float("-inf"), float("-inf")]] + pairs
        #         dp = [0] * len(pairs)

        #         def dfs(i):
        #             if dp[i]: return dp[i]
        #             dp[i] = 1
        #             for j in range(len(pairs)):
        #                 if pairs[i][-1] >= pairs[j][0]: continue
        #                 dp[i] = max(dp[i], 1 + dfs(j))
        #             return dp[i]

        #         dfs(0)
        #         return max(dp) - 1
        pairs = sorted(pairs, key=operator.itemgetter(1))
        cur, ans = float("-inf"), 0
        for x, y in pairs:
            if x > cur:
                ans += 1
                cur = y
        return ans