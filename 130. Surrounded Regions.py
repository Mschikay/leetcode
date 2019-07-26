'''dfs'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            h, w = len(board), len(board[0])

            def searchZero(i, j, v, points):
                if i < 0 or j < 0 or i >= h or j >= w:
                    return False
                if board[i][j] == "X": return True

                res = True
                points.append((i, j))
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (x, y) not in v:
                        v.add((x, y))
                        if not searchZero(x, y, v, points):
                            res = False
                return res

            v = set()
            for i in range(h):
                for j in range(w):
                    if (i, j) not in v and board[i][j] == "O":
                        points = []
                        v.add((i, j))
                        if searchZero(i, j, v, points):
                            for x, y in points:
                                board[x][y] = "X"


'''bfs'''
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def search(i, j, v):
            q = deque()
            q.append((i, j))
            res = []
            flip = True
            while q:
                i, j = q.pop()
                res.append((i, j))
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                        flip = False
                        continue
                    if (x, y) not in v and board[x][y] == "O":
                        v.add((x, y))
                        q.append((x, y))
            return res if flip else []

        v = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in v:
                    v.add((i, j))
                    points = search(i, j, v)
                    for x, y in points: board[x][y] = "X"


