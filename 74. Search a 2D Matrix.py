

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

        # if not matrix or not len(matrix[0]): return False
        #
        # def less(target):
        #     m, n = len(matrix), len(matrix[0])
        #     i, j, res = m - 1, 0, 0
        #     while i >= 0 and j < n:
        #         if matrix[i][j] < target:
        #             j += 1
        #             res += i + 1
        #         else:
        #             i -= 1
        #     return res
        #
        # if less(target) == less(target + 1):
        #     return False
        # return True
