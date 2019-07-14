class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #         area = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        #         for i in range(len(matrix)):
        #             for j in range(len(matrix[0])):
        #                 if not i and not j:
        #                     area[i][j] = [0, 1][matrix[i][j] == "1"]
        #                 elif not i:
        #                     area[i][j] = area[i][j - 1] + [0, 1][matrix[i][j] == "1"]
        #                 elif not j:
        #                     area[i][j] = area[i - 1][j] + [0, 1][matrix[i][j] == "1"]
        #                 else:
        #                     area[i][j] = area[i - 1][j] + area[i][j - 1] - area[i - 1][j - 1] + [0, 1][matrix[i][j] == "1"]

        area = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if not i or not j:
                        # area[i][j] = [0, 1][matrix[i - 1][j] == "1"] + 1
                        area[i][j] = 1
                    else:
                        area[i][j] = min(area[i - 1][j], area[i][j - 1], area[i - 1][j - 1]) + 1
                    m = max(m, area[i][j])

        return m ** 2