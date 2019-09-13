class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i, curr, left, right, ans):
            if right > left or left > n or right > n: return
            if i == n * 2:
                ans.append(curr)
                return
            dfs(i + 1, curr + "(", left + 1, right, ans)
            dfs(i + 1, curr + ")", left, right + 1, ans)
            return

        ans = []
        dfs(1, "(", 1, 0, ans)
        return ans


class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans