class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        p = [i for i in range(4 * N * N)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * N + c)
                if val in '/ ':
                    p[find(root + 0)] = find(root + 1)
                    p[find(root + 2)] = find(root + 3)
                if val in '\ ':
                    p[find(root + 0)] = find(root + 2)
                    p[find(root + 1)] = find(root + 3)

                # north/south
                if r + 1 < N: p[find(root + 3)] = find(root + 4 * N)
                if r - 1 >= 0: p[find(root + 0)] = find(root - 4 * N + 3)
                # east/west
                if c + 1 < N: p[find(root + 2)] = find(root + 4 + 1)
                if c - 1 >= 0: p[find(root + 1)] = find(root - 4 + 2)

        return sum(p[x] == x for x in range(len(p)))