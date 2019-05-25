        if not matrix or not len(matrix[0]): return False

        def less(target):
            m, n = len(matrix), len(matrix[0])
            i, j, res = m - 1, 0, 0
            while i >= 0 and j < n:
                if matrix[i][j] < target:
                    j += 1
                    res += i + 1
                else:
                    i -= 1
            return res

        if less(target) == less(target + 1):
            return False
        return True
