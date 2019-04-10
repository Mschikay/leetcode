# 行列有序的矩阵

## 378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

    matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],
    k = 8,

    return 13.

```python
# 二分法
# O(log(max - min) * n *log(n)）,找到一个数，对每一行做二分插入
# 如果这个数在当前行是最小的，那么后面不需要再做了 后面的数字会更大
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            total = 0
            for row in matrix:
                if mid < row[0]:
                    break
                total += bisect.bisect_right(row, mid)
                
            if total < k:
                lo = mid+1
            else:
                hi = mid
        return lo
```
**Note: You may assume k is always valid, 1 ≤ k ≤ n2.**


## 373. Find K Pairs with Smallest Sums
