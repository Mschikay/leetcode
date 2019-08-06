from collections import defaultdict


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(i, j, dic):
            if i == len(pattern) and j == len(s): return True
            if i == len(pattern) or j == len(s): return False
            if pattern[i] in dic:
                l = len(dic[pattern[i]])
                if j + l <= len(s) and dic[pattern[i]] == s[j:j + l]:
                    if dfs(i + 1, j + l, dic): return True
                else:
                    return False
            else:
                for x in range(j + 1, len(s) + 1):
                    if s[j:x] in dic.values(): continue
                    dic[pattern[i]] = s[j:x]
                    if dfs(i + 1, x, dic): return True
                    dic.pop(pattern[i])
                return False

        d = defaultdict(str)
        return dfs(0, 0, d)


from collections import defaultdict


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def dfs(i, j, dic):
            if i == len(pattern) and j == len(s): return True
            if i == len(pattern) or j == len(s): return False
            if pattern[i] in dic:
                l = len(dic[pattern[i]])
                if j + l <= len(s) and dic[pattern[i]] == s[j:j + l]:
                    if dfs(i + 1, j + l, dic): return True
                else:
                    return False
            else:
                for x in range(j + 1, len(s) - (len(pattern) - i - 1) + 1): # CUT EDGES
                    if s[j:x] in dic.values(): continue
                    dic[pattern[i]] = s[j:x]
                    if dfs(i + 1, x, dic): return True
                    dic.pop(pattern[i])
                return False

        d = defaultdict(str)
        return dfs(0, 0, d)