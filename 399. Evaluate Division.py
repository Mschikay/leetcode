from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def path(start, end, d):
            visited = set()
            q = deque()
            q.append((start, 1.0))
            while q:
                x, res = q.pop()
                if x == end:
                    return res
                for n in d[x].keys():
                    if n not in visited:
                        visited.add(n)
                        q.append((n, res * d[x][n]))

        def find(a, root):
            if a not in root:
                root[a] = a
            if a != root[a]:
                root[a] = find(root[a], root)
            return root[a]

        equa = defaultdict(dict)
        root = defaultdict(str)
        for i in range(len(equations)):
            d1, d2, res = equations[i][0], equations[i][1], values[i]
            equa[d1][d2] = res
            equa[d2][d1] = 1 / res
            root[find(d1, root)] = find(d2, root)

        ans = []
        for q1, q2 in queries:
            if q1 not in equa or q2 not in equa:
                ans.append(-1.0)
            elif find(q1, root) != find(q2, root):
                ans.append(-1.0)
            else:
                ans.append(path(q1, q2, equa))

        return ans



