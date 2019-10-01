class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        dp = [[0 for i in range(m + 1)] for j in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


'''
if the number of items are infinite,
the transition function becomes:
use the first i items, with weight no more than w:
    f[i][w] = max(f[i - 1][w - kA[i - 1]] + kV[i - 1]), k >= 0     
'''