class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1: return False
        d = [[] for i in range(len(stones))]

        d[1].append(1)

        for i in range(2, len(stones)):
            for j in range(i):
                for k in d[j]:
                    if abs(stones[i] - stones[j] - k) <= 1:
                        d[i].append(stones[i] - stones[j])

        if len(d[-1]): return True
        return False


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cheapest = [float("inf") for i in range(n)]
        for x in flights:
            if x[0] == src:
                cheapest[x[1]] = x[2]

        for i in range(K):
            cur = [c for c in cheapest]
            for u, v, c in flights:
                cur[v] = min(cur[v], cheapest[u] + c)
            cheapest = cur

        return -1 if cheapest[dst] == float("inf") else cheapest[dst]