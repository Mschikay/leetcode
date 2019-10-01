class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2 and not s3: return True
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp)):
            dp[i][0] = s2[i - 1] == s3[i - 1] and dp[i - 1][0]
        for j in range(1, len(dp[0])):
            dp[0][j] = s1[j - 1] == s3[j - 1] and dp[0][j - 1]
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                dp[i][j] = dp[i - 1][j] and s2[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]
        return dp[-1][-1]
