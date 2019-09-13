class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        ans = 0
        for i in range(len(s)):
            if s[i] == ")":
                if st and s[st[-1]] == "(":
                    st.pop()
                    left = -1 if not st else st[-1]
                    ans = max(ans, i - left)
                else:
                    st.append(i)
            else:
                st.append(i)
        return ans


'''dp'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                dp[i + 1] = 0
            else:
                j = i - dp[i] - 1
                if j >= 0 and s[j] == "(":
                    dp[i + 1] = dp[i] + 2 + dp[j]
            ans = max(ans, dp[i + 1])
        return ans

