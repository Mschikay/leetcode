# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
#
# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.
#
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
#
# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
#
# Example 1:
#
#
#
# Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# Output: [1,0]
# Explanation:
# Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # events = []
        # useworker = [False for i in range(len(workers))]
        # usebike = [False for i in range(len(bikes))]
        # for i in range(len(bikes)):
        #     for j in range(len(workers)):
        #         bike, worker = bikes[i], workers[j]
        #         distance = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
        #         events.append((distance, j, i))
        # events = sorted(events, key=lambda x:(x[0], x[1], x[2]))
        # ans = [-1 for i in range(len(workers))]
        # for event in events:
        #     i, j = event[1], event[2]
        #     if not useworker[i] and not usebike[j]:
        #         ans[i] = j
        #         useworker[i] = True
        #         usebike[j] = True
        # return ans
        N = 2000
        buckets = [[] for _ in range(N + 1)]
        paired_workers = set()
        paired_bikes = set()
        m, n = len(workers), len(bikes)
        result = [0] * m
        # construct the buckets
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                buckets[dist].append((i, j))
        # retrieve the workers from the buckets
        for i in range(N + 1):
            if len(buckets[i]) != 0:
                for w, b in buckets[i]:
                    if w not in paired_workers and b not in paired_bikes:
                        result[w] = b
                        paired_workers.add(w)
                        paired_bikes.add(b)
        return result