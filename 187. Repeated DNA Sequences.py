from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(lambda: 0)
        f = defaultdict(list)
        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            d[cur] += 1
            f[d[cur]].append(cur)
        if d:
            mv = max(d.values())
            if mv > 1: return f[mv]
        return []

from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        first = set()
        res = set()
        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            if cur in first:
                res.add(cur)
            else:
                first.add(cur)
        return list(res)