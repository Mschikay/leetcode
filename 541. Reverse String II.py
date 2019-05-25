class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        while l < len(s):
            r = min(l + k, len(s))
            s = s[:l] + s[l:r][::-1] + s[r:]
            l = l + 2 * k
        return s