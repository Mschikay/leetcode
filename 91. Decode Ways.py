class Solution:
    def numDecodings(self, s: str) -> int:
        d = {}
        d[len(s)] = 1

        def helper(idx):
            st = s[idx:]

            if idx in d.keys():
                return d[idx]
            elif not st:
                return 0
            elif st[0] == "0":
                return 0
            elif len(st) == 1:
                return 1
            else:
                num = helper(idx + 1)
                pre = st[:2]
                if int(pre) <= 26:
                    num += helper(idx + 2)
            d[idx] = num
            return num

        return helper(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0": return 0
        dp = [0 for i in range(len(s) + 1)]
        if "1" <= s[0:2] <= "26": dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i + 1] += dp[i]
            if "1" <= s[i - 1:i + 1] <= "26":
                    dp[i + 1] += dp[i - 1]
        return dp[-1]