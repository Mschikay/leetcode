# from collections import defaultdict
from heapq import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dst = [float("inf")] * (N + 1)
        dst[K] = 0
        for i in range(N):
            for s, t, e in times:
                dst[t] = min(dst[t], dst[s] + e)
        return -1 if float("inf") in dst[1:] else max(dst[1:])


from collections import defaultdict
from heapq import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[float("inf") for i in range(N + 1)] for i in range(N + 1)]
        for t in times:
            graph[t[0]][t[1]] = t[2]

        q = []
        heapify(q)
        q.append((0, K))
        v = set()
        dst, i = 0, K

        while q:
            dst, i = heappop(q)
            if i in v: continue
            graph[K][i] = dst
            v.add(i)
            if len(v) >= N: return max(graph[K][1:])

            for j in range(len(graph[i])):
                if j not in v and graph[i][j] != float("inf"):
                    heappush(q, (dst + graph[i][j], j))

        return -1
