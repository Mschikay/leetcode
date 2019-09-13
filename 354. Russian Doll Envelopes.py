'''dp, time limit exceed'''


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        envelopes.sort()
        heights = [h for w, h in envelopes]
        dp = [1 for i in range(len(heights))]
        ans = 0

        for i in range(len(dp)):
            m = 0
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and heights[i] > heights[j]:
                    m = max(m, dp[j])
            dp[i] = m + 1
            ans = max(ans, dp[i])
        return ans


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        ans = []

        def insert(t):
            l, h = 0, len(ans) - 1

            while l <= h:
                m = (l + h) // 2
                if ans[m] < t:
                    l = m + 1
                else:
                    h = m - 1
            ans[l] = t

        ans = [envelopes[0][1]]
        for w, h in envelopes[1:]:
            if h > ans[-1]:
                ans.append(h) # if height is higher than before, its width must be wider than before. because
                                # envelopes with the same width are sorted from highest to lowest
            else:
                insert(h)
        return len(ans)