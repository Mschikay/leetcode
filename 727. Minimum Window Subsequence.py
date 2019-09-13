from collections import defaultdict, Counter


class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S or not T: return ""
        m, n = len(S), len(T)
        dp = [[float("inf") for i in range(m + 1)] for i in range(n + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if T[i - 1] == S[j - 1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + dp[i][j - 1]
            if min(dp[i]) == float("inf"): return ""

        ans = min(dp[-1][:])
        idx = dp[-1].index(ans)
        return S[idx - ans:idx]