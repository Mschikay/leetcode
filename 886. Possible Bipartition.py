from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        def possible(i, status, d):
            for n in d[i]:
                if n in status:
                    if status[n] == status[i]: return False
                else:
                    status[n] = -1 * status[i]
                    possible(n, status, d)
            return True

        d = defaultdict(list)
        status = defaultdict(int)

        for x, y in dislikes:
            d[x].append(y)
            d[y].append(x)

        status[1] = 1
        return possible(1, status, d) and len(status) == len(d)


'''bfs'''
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for x, y in dislikes:
            g[x].append(y)
            g[y].append(x)

        q = deque()
        q.append(1)
        status = defaultdict(int)
        status[1] = 1
        l = 0
        while q:
            node = q.pop()
            l += 1
            for n in g[node]:
                if n in status:
                    if status[n] == status[node]: return False
                else:
                    status[n] = -1 * status[node]
                    q.append(n)

        return l == len(g)

