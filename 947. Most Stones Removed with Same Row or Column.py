class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i, visited):
            res = 0
            for s in range(len(stones)):
                if s in visited: continue
                if stones[s][0] == stones[i][0] or stones[s][1] == stones[i][1]:
                    visited.add(s)
                    res += 1 + dfs(s, visited)
            return res

        ans = 0
        visited = set()
        for i in range(len(stones)):
            if i not in visited:
                visited.add(i)
                ans += dfs(i, visited)
        return ans