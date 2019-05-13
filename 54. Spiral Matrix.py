class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        hBegin = 0
        hEnd = len(matrix) - 1
        wBegin = 0
        wEnd = len(matrix[0]) - 1
        res = []
        while hBegin <= hEnd and wBegin <= wEnd:
            for j in range(wBegin, wEnd + 1):
                res.append(matrix[hBegin][j])
            hBegin += 1
            for j in range(hBegin, hEnd + 1):
                res.append(matrix[j][wEnd])
            wEnd -= 1
            if hBegin <= hEnd:
                for j in range(wEnd, wBegin - 1, -1):
                    res.append(matrix[hEnd][j])
                hEnd -= 1
            if wBegin <= wEnd:
                for j in range(hEnd, hBegin - 1, -1):
                    res.append(matrix[j][wBegin])
                wBegin += 1
        return res