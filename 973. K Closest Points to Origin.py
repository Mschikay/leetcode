from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sort = []
        heapify(sort)
        for i in range(len(points)):
            p = points[i]
            heappush(sort, (p[0] ** 2 + p[1] ** 2, i))
        ans = []
        for i in range(K):
            top = heappop(sort)
            ans.append(points[top[1]])
        return ans



from heapq import *


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        def split(l, r):
            buck = l
            buckp = points[buck]
            buckdis = dist(points[buck])
            while l < r:
                while r > l and dist(points[r]) > buckdis:
                    r -= 1
                points[buck], points[r] = points[r], points[buck]
                buck = r
                while l < r and dist(points[l]) <= buckdis:
                    l += 1
                points[buck], points[l] = points[l], points[buck]
                buck = l
            points[buck] = buckp
            return buck

        l, r = 0, len(points) - 1
        while l <= r:
            buck = split(l, r)
            if buck >= K:
                r = buck - 1
            else:
                l = buck + 1
        return points[:l]

