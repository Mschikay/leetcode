from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dictp = Counter(p)
        n = len(p)
        res = []
        i, j = 0, n - 1
        dicts = Counter(s[i:j+1])
        while j < len(s):
            if dicts == dictp:
                res.append(i)
            dicts[s[i]] -= 1
            if not dicts[s[i]]: del dicts[s[i]]
            i += 1
            j += 1
            if j < len(s):
                dicts[s[j]] += 1
        return res


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        ss = [0] * 26
        pp = [0] * 26
        i, j, res = 0, len(p) - 1, []

        for x in p:
            pp[ord(x) - ord("a")] += 1
        for x in range(i, j + 1):
            ss[ord(s[x]) - ord("a")] += 1

        while j < len(s):
            if ss == pp:
                res.append(i)
            ss[ord(s[i]) - ord("a")] -= 1
            i += 1
            j += 1
            if j < len(s):
                ss[ord(s[j]) - ord("a")] += 1
        return res

# use only one pointer

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        ss = [0] * 26
        pp = [0] * 26
        n = len(p)
        i, j, res = 0, len(p) - 1, []

        for x in p:
            pp[ord(x) - ord("a")] += 1
        for i in range(len(s)):
            ss[ord(s[i]) - ord("a")] += 1
            if i >= n:
                ss[ord(s[i - n]) - ord("a")] -= 1
            if ss == pp:
                res.append(i - n + 1)
        return res