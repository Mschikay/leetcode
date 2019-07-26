from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = defaultdict()
        wordset = set(wordDict)

        def search(w):
            if w == "": return []
            if w in d:
                return d[w]

            res = []
            for i in range(1, len(w) + 1):
                if w[:i] in wordset:
                    if i == len(w): res.append(w[:i])
                    for item in search(w[i:]):
                        res.append(w[:i] + " " + item)

            d[w] = res
            return res

        return search(s)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s):
            if not s: return []
            if s in dic: return dic[s]
            res = []
            for x in wordDict:
                if s.startswith(x):
                    if len(s) == len(x): res.append(x)
                    for y in dfs(s[len(x):]):
                        res.append(x + ' ' + y)
            dic[s] = res
            return res

        dic = {}
        return dfs(s)