from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        l = r = 0
        longest = 0
        while True:
            while r < len(s) and d[s[r]] == 0:
                d[s[r]] = d[s[r]] + 1
                r += 1
            longest = max(longest, r - l)
            if r >= len(s):
                break
            while d[s[r]] > 0:
                d[s[l]] -= 1
                l += 1
        return longest


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength