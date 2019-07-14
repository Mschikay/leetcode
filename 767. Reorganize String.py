from collections import Counter
from heapq import *


class Solution:
    def reorganizeString(self, S: str) -> str:
        d = Counter(S)
        h = []
        heapify(h)
        for k, v in d.items():
            heappush(h, (-v, k))

        ans = ""
        while h:
            h0 = heappop(h)
            ans += h0[1]

            if not h: break
            h1 = heappop(h)
            ans += h1[1]

            if h0[0] + 1:
                heappush(h, (h0[0] + 1, h0[1]))
            if h1[0] + 1:
                heappush(h, (h1[0] + 1, h1[1]))

        if len(ans) == len(S): return ans
        return ""