from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        d = defaultdict(lambda: 0)
        maxlen = 0
        for r in range(len(s)):
            d[s[r]] += 1
            if len(d) <= k: maxlen = max(maxlen, r - l + 1)
            else:
                while l < r and len(d) > k:
                    d[s[l]] -= 1
                    if not d[s[l]]: d.pop(s[l])
                    l += 1
        return maxlen