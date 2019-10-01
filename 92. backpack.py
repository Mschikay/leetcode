class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        dp = [[False for i in range(m + 1)] for j in range(len(A) + 1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, len(A) + 1):
            for w in range(1, m + 1):
                if A[i - 1] <= w:
                    dp[i][w] = dp[i - 1][w] or dp[i - 1][w - A[i - 1]]
                else:
                    dp[i][w] = dp[i - 1][w]
        for i in range(m, 0, -1):
            if dp[-1][i]: return i
        return 0
    