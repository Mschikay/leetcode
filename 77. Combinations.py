# n^k
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(curr, i, ans):
            if len(curr) == k:
                ans.append(curr)
                return
            for j in range(i, n + 1):
                dfs(curr + [j], j + 1, ans)

        ans = []
        dfs([], 1, ans)
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:

        if k > n: return []
        if k == 1: return [[i] for i in range(1, n + 1)]
        pre = self.combine(n - 1, k - 1)
        for p in pre: p.append(n)

        return pre + self.combine(n - 1, k)

        '''
        第一个结点是（n, k）,结点的两条边指向（n - 1，k - 1），（n - 1, k）
        时间复杂度是结点的数量
        空间复杂度是结果的空间 + 图（树）的深度（max(n - k, k)）
        '''