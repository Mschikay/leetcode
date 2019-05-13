class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[1 for i in range(n)] for i in range(n)]

        hBegin = 0
        hEnd = n - 1
        wBegin = 0
        wEnd = n - 1
        v = 1
        while hBegin <= hEnd and wBegin <= wEnd:
            for i in range(wBegin, wEnd + 1):
                m[hBegin][i] = v
                v += 1
            hBegin += 1

            for i in range(hBegin, hEnd + 1):
                m[i][wEnd] = v
                v += 1
            wEnd -= 1

            if hBegin <= hEnd:
                for i in range(wEnd, wBegin - 1, -1):
                    m[hEnd][i] = v
                    v += 1
                hEnd -= 1

            if wBegin <= wEnd:
                for i in range(hEnd, hBegin - 1, -1):
                    m[i][wBegin] = v
                    v += 1
                wBegin += 1
        return m

# ???
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions