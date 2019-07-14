class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 1

        d = [1] * 2 + [0 for i in range(n - 1)]
        for i in range(2, len(d)):
            for j in range(i):
                d[i] += d[j] * d[i - 1 - j]
            # print(i, d[i])
        return d[i]


class Solution:
    def numTrees(self, n: int) -> int:
        # if not n: return 1
        # elif n == 1: return 1
        # elif n == 2: return 2
        # else:
        #     res = 0
        #     for i in range(1, n + 1):
        #         res += self.numTrees(n - i) * self.numTrees(i - 1)
        #     return res

        if not n:
            return 1
        elif n == 1:
            return 1
        nums = [1, 1] + [None] * (n - 1)

        def helper(n):
            if nums[n]:
                return nums[n]
            else:
                res = 0
                for i in range(n):
                    res += helper(n - i - 1) * helper(i)
                nums[n] = res
                return res

        return helper(n)