from collections import defaultdict
from heapq import *


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for p in prerequisites:
            indegree[p[0]] += 1
            d[p[1]].append(p[0])

        q = []
        heapify(q)
        for i in range(len(indegree)):
            if not indegree[i]:
                heappush(q, i)

        v = set()
        n = 0
        ans = []
        while q:
            numCourse = heappop(q)
            ans.append(numCourse)
            n += 1
            v.add(numCourse)
            for x in d[numCourse]: # 每条边访问了一次，做了v次heappush，所以time: E - V + VlogV 即 ElogV
                                    # worst case是ElogV 每次访问边时，都有新的结点可以加入，几乎做了E次heappush
                if x not in v:
                    indegree[x] -= 1
                    if not indegree[x]:
                        heappush(q, x)

        return ans if n == numCourses else []