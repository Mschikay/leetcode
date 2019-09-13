

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: -1)
        i = 0
        maxlen = 0
        for j in range(len(s)):
            if d[s[j]] >= i:
                i = d[s[j]] + 1
            d[s[j]] = j
            maxlen = max(maxlen, j - i + 1)
        return maxlen



from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = defaultdict(lambda: 0)
        r = l = res = 0
        for r in range(len(s)):
            num[s[r]] += 1
            while num[s[r]] > 1:
                num[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res