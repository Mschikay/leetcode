class Solution:
    def minCut(self, s: str) -> int:
        boolean = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(boolean)):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i - j <= 2:
                        boolean[j][i] = True
                    else:
                        boolean[j][i] = boolean[j + 1][i - 1]

        dp = [[float("inf") for i in range(len(s) + 1)] for j in range(len(s))]
        dp[0][0] = 0
        for i in range(len(s)):
            dp[i][i + 1] = 1
        for i in range(len(s)):
            for j in range(i, -1, -1):
                for k in range(j, i + 1):
                    if boolean[k][i]:
                        dp[j][i + 1] = min(dp[j][i + 1], dp[j][k] + 1)
        return dp[0][-1] - 1


'''one dimention'''
class Solution:
    def minCut(self, s: str) -> int:
        boolean = [[False for i in range(len(s))] for j in range(len(s))]

        dp = [float("inf") for i in range(len(s) + 1)]
        dp[0] = 0
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i - j >= 3:
                        boolean[j][i] = boolean[j + 1][i - 1]
                    else:
                        boolean[j][i] = True
                    if boolean[j][i]:
                        dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[-1] - 1

