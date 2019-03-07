class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == "":
            return ""

        start = 0
        end = 0
        maxLength = 0
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i - 1][j + 1]
                else:
                    dp[i][j] = False

                if dp[i][j] is True:
                    if i - j > maxLength:
                        start = j
                        end = i
                        maxLength = i - j

        return s[start:end + 1]