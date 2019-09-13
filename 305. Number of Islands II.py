# 305. Number of Islands II
# Hard
#
# 600
#
# 10
#
# Favorite
#
# Share
# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# Explanation:
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        N = 0
        d = {}
        ans = []

        def find(i, j):
            if d[(i, j)] != (i, j):
                d[(i, j)] = find(d[(i, j)][0], d[(i, j)][1])
            return d[(i, j)]

        for i, j in positions:
            if (i, j) not in d:
                d[(i, j)] = (i, j)
                N += 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) in d:
                    f1, f2 = find(i, j), find(x, y) # the find includes path compression
                    if f1 != f2:
                        d[f1] = f2
                        N -= 1
            ans.append(N)
        return ans