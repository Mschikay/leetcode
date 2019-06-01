from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        nt = Counter(t)
        todo = len(nt)
        cur = defaultdict(lambda: 0)
        ans = ""
        l = r = 0
        minlen = float("inf")
        while r < len(s):
            if s[r] in t:
                cur[s[r]] += 1
                if cur[s[r]] == nt[s[r]]: todo -= 1
            while not todo and l <= r:
                if s[l] in t:
                    if r - l < minlen:
                        ans = s[l: r + 1]
                        minlen = r - l
                    cur[s[l]] -= 1
                    if cur[s[l]] < nt[s[l]]: todo += 1
                l += 1
            r += 1
        return ans
