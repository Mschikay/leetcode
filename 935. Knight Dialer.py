class Solution:
    def knightDialer(self, N: int) -> int:
        d = {}
        d[1] = [6, 8]
        d[2] = [7, 9]
        d[3] = [4, 8]
        d[4] = [3, 9, 0]
        d[5] = []
        d[6] = [1, 7, 0]
        d[7] = [2, 6]
        d[8] = [1, 3]
        d[9] = [4, 2]
        d[0] = [4, 6]

        dp = [[0] * 10 for i in range(N)]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if not i:
                    dp[i][j] = 1
                else:
                    for x in d[j]:
                        dp[i][j] += dp[i - 1][x]

        MOD = pow(10, 9) + 7
        return sum(dp[N - 1][:]) % MOD


class Solution:
    def knightDialer(self, N: int) -> int:
        a = [1,1,1,1,1,1,1,1,1,1]
        b = [0,0,0,0,0,0,0,0,0,0]
        for i in range(N-1):
            b[0] = a[4]+a[6]
            b[1] = a[6]+a[8]
            b[2] = a[7]+a[9]
            b[3] = a[4]+a[8]
            b[4] = a[0]+a[3]+a[9]
            b[6] = a[0]+a[1]+a[7]
            b[7] = a[2]+a[6]
            b[8] = a[1]+a[3]
            b[9] = a[2]+a[4]
            a = b
            b = [0,0,0,0,0,0,0,0,0,0]
        return sum(a)%(10**9+7)