class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cheapest = [[float("inf") for i in range(n)] for i in range(K + 1)]
        cheapest[0][src] = 0
        for f in flights:
            if f[0] == src:
                cheapest[0][f[1]] = f[2]
        for i in range(1, len(cheapest)):
            for j in range(len(cheapest[i])):
                cheapest[i][j] = cheapest[i - 1][j]
            for f in flights:
                cheapest[i][f[1]] = min(cheapest[i - 1][f[0]] + f[2], cheapest[i][f[1]])
        return -1 if cheapest[-1][dst] == float("inf") or src == dst else cheapest[-1][dst]


# The time complexity would be O(E log(E) )? Every node i is inserted in_degree(i) times into the min_queue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)

        for u, v, cost in flights:
            graph[u][v] = cost

        heap = [(0, src, K + 1)]
        while heap:
            cost, u, k = heapq.heappop(heap)

            if u == dst:
                return cost
            if k > 0:
                for v in graph[u]:
                    heapq.heappush(heap, (cost + graph[u][v], v, k - 1))

        return -1


'''use dfs: overflow'''
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.ans = float("inf")
        edge = defaultdict(list)
        for a, b, c in flights:
            edge[a].append((b, c))

        def search(curr, num, price, v):
            if num < 0: return
            if curr == dst:
                self.ans = min(self.ans, price)
                return
            for n, p in edge[curr]:
                if n not in v:
                    v.add(n)
                    search(n, num - 1, price + p, v)
                    v.remove(n)
            return

        v = set()
        search(src, K + 1, 0, v)
        return -1 if self.ans == float("inf") else self.ans



'''时间复杂度是VlogV + E
    如果没有heap就是V + E
    E是0-V^2
'''
from collections import defaultdict
from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edge = defaultdict(list)
        for a, b, c in flights:
            edge[a].append((c, b))
        h = []
        heapify(h)
        heappush(h, (0, src, -1))
        ans = -1
        while h:
            price, curr, stop = heappop(h)
            if curr == dst:
                ans = price
                break
            if stop < K:
                for p, n in edge[curr]:
                    heappush(h, (price + p, n, stop + 1))
        return ans
