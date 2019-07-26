from collections import defaultdict


class WordFilter:

    def __init__(self, words: List[str]):
        self.index = defaultdict(lambda: -1)
        for i, w in enumerate(words):
            self.index[w] = i

        self.ordered = defaultdict()
        for w in words:
            d = self.ordered
            for c in w:
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]
            d["end"] = defaultdict()

        self.reversed = defaultdict()
        for w in words:
            d = self.reversed
            for c in reversed(w):
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]
            d["end"] = defaultdict()

    def f(self, prefix: str, suffix: str) -> int:
        def find(i, wd, s):
            if i >= len(s):
                return wd
            else:
                if s[i] in wd:
                    return find(i + 1, wd[s[i]], s)
            return defaultdict()

        def findwords(wd, curr, res, reverse):
            if "end" in wd:
                if reverse:
                    res.add(self.index[curr[::-1]])
                else:
                    res.add(self.index[curr])
            for k in wd.keys():
                if k != "end":
                    findwords(wd[k], curr + k, res, reverse)

        lastPreDict = find(0, self.ordered, prefix)
        lastSufDict = find(0, self.reversed, suffix[::-1])
        preIdx = set()
        sufIdx = set()

        findwords(lastPreDict, prefix, preIdx, False)
        findwords(lastSufDict, suffix[::-1], sufIdx, True)

        idx = preIdx & sufIdx
        return -1 if idx == set() else max(idx)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

class WordFilter:

    def __init__(self, words: List[str]):
        self.d = dict()
        for index, word in enumerate(words):
            N = len(word)
            for i in range(N + 1):
                for j in range(N + 1):
                    w = word[:i] + '#' + word[j:]
                    self.d[w] = index

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get(prefix + '#' + suffix, -1)
