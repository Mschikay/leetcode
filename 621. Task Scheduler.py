from collections import Counter
from heapq import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = []
        heapify(h)
        for k, v in d.items():
            heappush(h, (-v, k))

        ans = 0
        while h:
            cur = 0
            popped = []
            while h and cur < n + 1:
                ans += 1
                cur += 1
                num, v = heappop(h)
                if num + 1: popped.append((num + 1, v))
            if popped and cur < n + 1:
                ans += n + 1 - cur
            for p in popped:
                heappush(h, p)

        return ans
