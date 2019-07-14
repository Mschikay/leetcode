class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.area = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        self.getArea()

    def getArea(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if not i and not j:
                    self.area[i][j] = self.matrix[i][j]
                elif not i:
                    self.area[i][j] = self.area[i][j - 1] + self.matrix[i][j]
                elif not j:
                    self.area[i][j] = self.area[i - 1][j] + self.matrix[i][j]
                else:
                    self.area[i][j] = self.area[i - 1][j] + self.area[i][j - 1] - self.area[i - 1][j - 1] + \
                                      self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not row1 and not col1:
            return self.area[row2][col2]
        elif not row1:
            return self.area[row2][col2] - self.area[row2][col1 - 1]
        elif not col1:
            return self.area[row2][col2] - self.area[row1 - 1][col2]
        else:
            return self.area[row2][col2] - self.area[row1 - 1][col2] - self.area[row2][col1 - 1] + self.area[row1 - 1][
                col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)