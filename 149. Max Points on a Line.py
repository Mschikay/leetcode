from collections import defaultdict
from decimal import *


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        if len(points) <= 1: return len(points)
        ans = float("-inf")
        for i in range(len(points)):
            d = defaultdict(lambda: 0)
            same = 1
            maxk = float("-inf")
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                k = Decimal(y1 - y2) / Decimal(x1 - x2) if x1 - x2 != 0 else float("inf")
                d[k] = d[k] + 1
            # print(i, d, same)
            if d.values():
                maxk = max(maxk, max(d.values()) + same)
            else:
                maxk = max(maxk, same)
            ans = max(ans, maxk)
        return ans
