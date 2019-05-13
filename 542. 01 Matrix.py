# Do a BFS on multiple sources: the squares of the given matrix that have a 0.
# Every time you visit a node, it will be from a path of predecessors that is of shortest distance to a zero.
# the former elements must be closer than the latter

# Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use
# yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

import collections

class Solution:
    def updateMatrix(self, A):
        R, C = len(A), len(A[0])
        def neighbors(r, c):
            for cr, cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        q = collections.deque([((r, c), 0)
                for r in range(R)
                for c in range(C)
                if A[r][c] == 0])
        seen = {x for x,_ in q}
        ans = [[0]*C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            print(r, c)
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))

        return ans

s = Solution()
s.updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]]
)

