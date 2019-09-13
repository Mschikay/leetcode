from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        l = r = 0
        d = defaultdict(lambda: 0)
        counter = 0
        while r < len(s):
            d[s[r]] += 1
            if d[s[r]] == 1: counter += 1
            r += 1
            while l < r and counter > 2:
                d[s[l]] -= 1
                if not d[s[l]]: counter -= 1
                l += 1
            maxlen = max(maxlen, r - l)
        return maxlen


from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch = defaultdict(lambda:0)
        l = r = res = 0
        for r in range(len(s)):
            ch[s[r]] += 1
            while len(ch) > 2:
                ch[s[l]] -= 1
                if not ch[s[l]]:
                    ch.pop(s[l])
                l += 1
            res = max(res, r - l + 1)
        return res