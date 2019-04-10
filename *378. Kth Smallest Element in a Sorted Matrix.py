import bisect


class Solution:
    def kthSmallest(self, matrix, k):
        # 用最大堆的方法 始终保持k个数 更大的数丢弃 但这样没有用到matrix的特性

        # 二分法
        # O(log(max - min) * n *log(n)）,找到一个数，对每一行做二分插入
        # 优化一下可以到
        # O(log(max - min) * n + n * log(n)）
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            total = 0
            for row in matrix:
                if mid < row[0]:
                    break
                total += bisect.bisect_right(row, mid)

            if total < k:
                lo = mid + 1
            else:
                hi = mid
        return lo


# 有问题
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if matrix is None or len(matrix) == 0:
            return None
        if k == 1:
            return matrix[0][0]

        total = 0
        remainK = pow(len(matrix), 2) - k
        i = 0
        for i in range(remainK):
            total += i
            if total >= remainK:
                break
        if i == 0:
            loc = len(matrix) - 1
        else:
            loc = len(matrix) - i
        restK = pow(loc + 1, 2)
        remain = k - restK
        print(total, i, loc, restK, remain)

        if remain > 0:
            xy = []
            for i in range(loc + 1):
                xy += matrix[i][loc + 1:]
            end = len(matrix) - 1
            for i in range(loc + 1, len(matrix)):
                xy += matrix[i][0:end]
                end -= 1
            xy.sort()
            return xy[remain - 1]
        else:
            xy = []
            for i in range(loc + 1):
                print(i)
                xy += matrix[i][0:loc + 1]
            xy.sort()
            print(xy)
            return xy[k - 1]