from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        r = 0
        d = defaultdict(lambda: 0)
        ans = 0
        for l in range(len(s)):
            while r < len(s) and len(d) < k:
                d[s[r]] += 1
                r += 1
            if len(d) >= k:
                ans += len(s) - r + 1
            else:
                break
            d[s[l]] -= 1
            if not d[s[l]]:
                d.pop(s[l])
        return ans