from collections import deque


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def isBorder(i, j):
            if 0 <= i + 1 < h and 0 <= j < w and not A[i + 1][j]: return True
            if 0 <= i - 1 < h and 0 <= j < w and not A[i - 1][j]: return True
            if 0 <= i < h and 0 <= j + 1 < w and not A[i][j + 1]: return True
            if 0 <= i < h and 0 <= j - 1 < w and not A[i][j - 1]: return True
            return False

        def findBorder(i, j, visited, border):
            if i < 0 or i >= h or j < 0 or j >= w or (i, j) in visited or not A[i][j]: return
            if isBorder(i, j):
                border.append((i, j))
            visited.add((i, j))
            findBorder(i + 1, j, visited, border)
            findBorder(i - 1, j, visited, border)
            findBorder(i, j + 1, visited, border)
            findBorder(i, j - 1, visited, border)
            return

        h, w = len(A), len(A[0])
        i = j = 0
        for i in range(h):
            for j in range(w):
                if A[i][j]: break
            if A[i][j]: break
        visited = set()
        border = []
        findBorder(i, j, visited, border)

        q = deque()
        for i, j in border:
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
                    if A[x][y]: return 0
                    visited.add((x, y))
                    q.append((x, y, 1))

        while q:
            i, j, step = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
                    visited.add((x, y))
                    if A[x][y]: return step
                    q.append((x, y, step + 1))