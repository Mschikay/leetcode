
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s is None or s == "":
            return 0

        # dp = [[1]*len(s)]*len(s) 用这种方法创建数组会发生引用错误 因为是浅拷贝！
        dp = [[1 for i in range(len(s))]for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                print(i, j)
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
                else:
                    if i - j > 2:
                        dp[i][j] = 2 + dp[i-1][j+1]
                    else:
                        dp[i][j] = 1 + i - j

                print(dp)
        return dp[len(s)-1][0]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))