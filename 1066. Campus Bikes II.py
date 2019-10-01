# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
#
# We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.
#
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
#
# Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        memo = {}
        self.distance = float("inf")

        def search(iw, useb, curr):
            if iw == len(workers):
                if curr < self.distance:
                    self.distance = curr
            else:
                for i in range(len(bikes)):
                    if not useb[i]:
                        useb[i] = True
                        dis = abs(bikes[i][0] - workers[iw][0]) + abs(bikes[i][1] - workers[iw][1])
                        search(iw + 1, useb, curr + dis)
                        useb[i] = False

        search(0, [False for i in range(len(bikes))], 0)
        return self.distance