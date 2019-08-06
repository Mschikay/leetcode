class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i, curr, res, l, ans):
            if l == k and res == n:
                ans.append(curr)
                return
            if l > k or res > n: return
            for j in range(i + 1, 10):
                dfs(j, curr + [j], res + j, l + 1, ans)
            return

        ans = []
        dfs(0, [], 0, 0, ans)
        return ans