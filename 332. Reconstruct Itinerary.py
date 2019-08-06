class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        # print(targets)

        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)

        dfs('JFK')
        return route[::-1]

hy
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for d, t in tickets:
            graph[d].append(t)

        def search(airport, path, num, ans):
            if num == len(tickets):
                ans += path
                return True
            for n in sorted(graph[airport]):
                graph[airport].remove(n)
                if search(n, path + [n], num + 1, ans):
                    return True
                graph[airport].append(n)
            return False

        ans = []
        search("JFK", ["JFK"], 0, ans)
        return ans

