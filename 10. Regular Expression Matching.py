class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "" and (p == "" or set(p) == {"*"}): return True

        # dp[i][j] means s[:i] matches pattern[:j]
        d = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        d[0][0] = True

        for x in range(len(p)):
            if p[x] == "*":
                d[0][x + 1] = d[0][x - 1]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "*":
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        d[i + 1][j + 1] = d[i + 1][j - 1] or d[i + 1][j] or d[i][
                            j + 1]  # 0, 1, and multiple times, b-a*b, a-a*, aa-a*
                    else:
                        d[i + 1][j + 1] = d[i + 1][j - 1]  # count as empty
                elif s[i] == p[j] or p[j] == ".":
                    d[i + 1][j + 1] = d[i][j]

        return d[-1][-1]