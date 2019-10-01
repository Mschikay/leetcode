from heapq import *


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap: return 0
        visited = [[False for i in range(len(heightMap[0]))] for j in range(len(heightMap))]
        waterline = [[0 for i in range(len(heightMap[0]))] for j in range(len(heightMap))]
        h = []
        w = len(heightMap[0])
        l = len(heightMap)
        heapify(h)
        for i in range(w):
            waterline[0][i] = heightMap[0][i]
            heappush(h, (heightMap[0][i], 0, i))
            visited[0][i] = True
            waterline[l - 1][i] = heightMap[l - 1][i]
            heappush(h, (heightMap[l - 1][i], l - 1, i))
            visited[l - 1][i] = True
        for i in range(l):
            waterline[i][0] = heightMap[i][0]
            heappush(h, (heightMap[i][0], i, 0))
            visited[i][0] = True
            waterline[i][w - 1] = heightMap[i][w - 1]
            heappush(h, (heightMap[i][w - 1], i, w - 1))
            visited[i][w - 1] = True

        ans = 0
        while h:
            line, i, j = heappop(h)
            ans += line - heightMap[i][j]
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= l or y < 0 or y >= w or visited[x][y]: continue
                visited[x][y] = True
                if heightMap[x][y] >= line:
                    waterline[x][y] = heightMap[x][y]
                else:
                    waterline[x][y] = line
                heappush(h, (waterline[x][y], x, y))
        return ans

