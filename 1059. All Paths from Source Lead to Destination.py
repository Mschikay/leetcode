from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        def dfs(curr, v):
            if curr == destination and not graph[curr]: return True
            hasNext = False
            for n in graph[curr]:
                if n in v:
                    return False
                else:
                    hasNext = True
                    v.add(n)
                    if not dfs(n, v): return False
                    v.remove(n)
            if hasNext: return True
            return False

        v = set()
        return dfs(source, v)