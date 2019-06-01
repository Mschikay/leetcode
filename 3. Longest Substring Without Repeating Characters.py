

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
