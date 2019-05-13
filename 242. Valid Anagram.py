from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        d = defaultdict(lambda: 0)
        for ss in s:
            d[ss] += 1
        for tt in t:
            d[tt] -= 1

        return not s and not t or set(d.values()) == {0}


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        d = defaultdict(lambda: 0)
        dd = defaultdict(lambda: 0)
        for ss in s:
            d[ss] += 1
        for tt in t:
            dd[tt] += 1

        return d == dd


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        d = Counter(s)
        dd = Counter(t)

        return d == dd