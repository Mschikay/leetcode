class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones) - K) % (K - 1): return -1
        pre = [0]
        for s in stones: pre.append(pre[-1] + s)
        dp = [[[float("inf") for i in range(K + 1)] for i in range(len(stones))] for i in range(len(stones))]
        for i in range(len(stones)):
            dp[i][i][1] = 0

        for j in range(len(stones)):
            for i in range(j - 1, -1, -1):
                for k in range(2, K + 1):
                    for m in range(i, j, K - 1):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m + 1][j][k - 1])
                dp[i][j][1] = min(dp[i][j][1], dp[i][j][K] + pre[j + 1] - pre[i])

        return dp[0][len(stones) - 1][1]