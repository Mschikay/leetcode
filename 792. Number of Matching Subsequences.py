from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, v in enumerate(S):
            d[v].append(i)
        res = 0
        for word in words:
            prev = []
            for i in range(len(word)):
                if word[i] not in d: break
                for idx in d[word[i]]:
                    if not prev or idx > prev[-1]:
                        prev.append(idx)
                        break
            if len(prev) == len(word): res += 1

        return res

class Solution:
    def numMatchingSubseq(self, S, words):
        def check(s, i):
            for c in s:
                i = S.find(c, i) + 1
                if not i:
                    return False
            return True

        return sum((check(word, 0) for word in words))

'''with binary'''
from collections import defaultdict
from bisect import *

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, v in enumerate(S):
            d[v].append(i)
        res = 0
        def check(word):
            prev = -1
            for c in word:
                if c not in d: return 0
                idx = bisect_left(d[c], prev)
                if idx >= len(d[c]): return 0
                prev = d[c][idx] + 1
            return 1

        for w in words:
            res += check(w)
        return res