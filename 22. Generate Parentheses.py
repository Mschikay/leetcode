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
