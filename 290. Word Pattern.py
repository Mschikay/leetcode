class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        s = string.split(" ")
        if len(s) != len(pattern): return False
        dp = {}
        sset = set()
        for i in range(len(pattern)):
            if pattern[i] not in dp:
                if s[i] in sset: return False
                dp[pattern[i]] = s[i]
            else:
                if s[i] != dp[pattern[i]]: return False
            sset.add(s[i])
        return True