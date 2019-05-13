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