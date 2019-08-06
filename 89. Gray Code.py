from decimal import Decimal


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        total = pow(2, n)
        self.ans = None

        def dfs(v, curr, ten, l):
            if l == total:
                self.ans = ten
                return True
            for i in range(len(curr)):
                newCurr = curr[:i] + str(1 - int(curr[i])) + curr[i + 1:]
                if newCurr not in v:
                    v.add(newCurr)
                    if dfs(v, newCurr, ten + [int(newCurr.encode(), 2)], l + 1): return True
                    v.remove(newCurr)
            return False

        v = set()
        v.add("0" * n)
        dfs(v, "0" * n, [0], 1)
        return self.ans

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(2**n):
            ans.append(i ^ (i >> 1))
        return ans