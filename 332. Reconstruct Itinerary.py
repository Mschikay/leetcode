from collections import defaultdict, Counter


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)

        tickets.sort()

        for s, t in sorted(tickets, reverse=True):
            edges[s].append(t)
        print(edges)

        res = []

        def query(s):
            while edges[s]:
                query(edges[s].pop())
            res.append(s)

        query("JFK")
        return res[::-1]

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

