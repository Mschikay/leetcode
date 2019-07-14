class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        maxlen = 0
        for i in range(len(s)):
            if s[i] == ")":
                if st and s[st[-1]] == "(":
                    st.pop()
                    if st: l = st[-1]
                    else: l = -1
                    maxlen = max(i - l, maxlen)
                    continue
            st.append(i)
        return maxlen


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 1: return 0
        dp = [0] * len(s)
        maxlen = 0

        for i in range(1, len(s)):
            if s[i] == ")":
                n = dp[i - 1]
                sym = i - 1 - n
                if sym >= 0 and s[sym] == "(":
                    dp[i] = dp[i - 1] + 2
                    if sym - 1 >= 0:
                        dp[i] += dp[sym - 1]
                maxlen = max(maxlen, dp[i])

        return maxlen