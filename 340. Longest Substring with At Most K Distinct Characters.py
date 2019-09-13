
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = ans = 0
        d = defaultdict(lambda: 0)
        for r in range(len(s)):
            d[s[r]] += 1
            while len(d) > k:
                d[s[l]] -= 1
                if not d[s[l]]:
                    d.pop(s[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans