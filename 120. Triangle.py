class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0] for i in range(len(triangle[-1]))]
        end = 2
        for i in range(1, len(triangle)):
            cur = [d for d in dp]
            for j in range(end):
                if j == 0:
                    cur[j] = dp[j] + triangle[i][j]
                elif j == end - 1:
                    cur[j] = dp[j - 1] + triangle[i][j]
                else:
                    cur[j] = min(dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j])
            end += 1
            dp = cur
        return min(dp)