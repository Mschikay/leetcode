from collections import deque
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # dp = [0] + [float("inf") for i in range(n)]
        # for i in range(1, len(dp)):
        #     for j in range(1, int(pow(i, 0.5)) + 1):
        #         dp[i] = min(dp[i - j ** 2] + 1, dp[i])
        # return dp[-1]

        #         v = set()
        #         perfect = []
        #         queue = deque()
        #         for i in range(1, n + 1):
        #             if i ** 2 > n:
        #                 break
        #             perfect.append(i ** 2)
        #             v.add(i ** 2)
        #             queue.append((i ** 2, 1))

        #         while queue:
        #             curr, num = queue.popleft()
        #             if curr == n: return num
        #             num += 1
        #             for p in perfect:
        #                 if p + curr <= n and p + curr not in v:
        #                     v.add(p + curr)
        #                     queue.append((p + curr, num))

        if n < 2: return n

        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1

        res = 0
        q = {n}
        while q:
            succ = set()
            for x in q:
                for y in squares:
                    if y > x:
                        break
                    elif y == x:
                        return res + 1
                    succ.add(x - y)
            res += 1
            q = succ
        return res