class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for x in range(len(p)):
            if p[x] == "*":
                dp[0][x + 1] = dp[0][x]
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == "?":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j] or dp[i][j + 1]
        return dp[-1][-1]
