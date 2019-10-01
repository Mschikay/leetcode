class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for i in range(len(A))]
        ma = A[0]
        for i in range(len(A)):
            if i < K:
                ma = max(ma, A[i])
                dp[i] = ma * (i + 1)
            else:
                ma = A[i]
                for m in range(1, K + 1):
                    ma = max(ma, A[i - m + 1])
                    dp[i] = max(dp[i], dp[i - m] + ma * m)
        return dp[-1]