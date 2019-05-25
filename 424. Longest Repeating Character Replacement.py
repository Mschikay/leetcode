from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        j = i = 0
        ans = 0
        while j < len(s):
            d[s[j]] += 1
            while sum(d.values()) - max(d.values()) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        i = 0
        ans = 0
        mx = 0
        for j in range(len(s)):
            d[s[j]] += 1
            mx = max(mx, d[s[j]])
            while j - i + 1 - mx > k:
                d[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
