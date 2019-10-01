from collections import Counter
from heapq import *
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k: return s
        d = Counter(s)
        h = []
        heapify(h)
        for key, v in d.items():
            heappush(h, (-v, key))
        ans = ""
        while h:
            again = []
            remain = k
            while remain:
                if h:
                    num, curr = heappop(h)
                    ans += curr
                    if num + 1:
                        again.append((num + 1, curr))
                else:
                    break
                remain -= 1
            if remain:
                if again: return ""
            else:
                while again:
                    heappush(h, again.pop())
        return ans