class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [1]
        i2 = i3 = i5 = 0
        i = 1
        while i < n:
            num.append(min(2 * num[i2], 3 * num[i3], 5 * num[i5]))
            if num[-1] == 2 * num[i2]:
                i2 += 1
            if num[-1] == 3 * num[i3]:
                i3 += 1
            if num[-1] == 5 * num[i5]:
                i5 += 1
            i += 1
        return num[-1]


from heapq import *


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = [1]
        heapify(h)
        i = 0
        v = set()
        ans = 0
        while i < n:
            ans = heappop(h)
            if ans not in v:
                v.add(ans)
                heappush(h, ans * 2)
                heappush(h, ans * 3)
                heappush(h, ans * 5)
                i += 1
        return ans
