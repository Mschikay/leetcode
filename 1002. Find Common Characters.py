from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A: return []
        d = Counter(A[0])
        for a in A:
            d = Counter(a) & d

        res = []
        for k, v in d.items():
            res += [k] * v
        return res


from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A: return []
        d = Counter(A[0])
        for a in A:
            d = Counter(a) & d

        # res = []
        # for k, v in d.items():
        #     res += [k] * v
        return list(d.elements())


import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        B = [collections.Counter(a) for a in A]
        ans = []
        for s in 'abcdefghijklmnopqrstuvwxyz':
            m = min(b[s] for b in B)
            for _ in range(m):
                ans.append(s)
        return ans
