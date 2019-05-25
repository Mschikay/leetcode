class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, a1, a2 = len(s1), [0] * 26, [0] * 26
        for s in s1:
            a1[ord(s) - ord("a")] += 1

        for i in range(len(s2)):
            a2[ord(s2[i]) - ord("a")] += 1
            if i >= n:
                a2[ord(s2[i - n]) - ord("a")] -= 1
            if a2 == a1:
                return True
        return False


from collections import Counter, defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1 = Counter(s1)
        d2 = defaultdict(lambda: 0)
        l = r = 0
        while r < len(s2):
            d2[s2[r]] += 1
            if r >= len(s1):
                d2[s2[l]] -= 1
                if d2[s2[l]] == 0: d2.pop(s2[l])
                l += 1

            if d2 == d1: return True
            r += 1
        return False

