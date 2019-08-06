from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        status = defaultdict(bool)

        def search(i, v):
            if i in status:
                return status[i]

            res = True
            for n in graph[i]:
                if n in v:
                    res = False
                else:
                    v.add(n)
                    if n in status:
                        if not status[n]:
                            res = False
                    else:
                        if not search(n, v):
                            res = False
                    v.remove(n)
            status[i] = res
            return status[i]

        ans = []
        for i in range(len(graph)):
            v = set()
            if search(i, v): ans.append(i)

        return ans