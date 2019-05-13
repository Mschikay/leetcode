from collections import deque


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [None] * len(A)
        A = deque(sorted(A))
        B = deque(sorted([(B[i], i) for i in range(len(B))]))

        last = len(res) - 1
        head = 0
        while A and B:
            a = A.popleft()
            b, idx = B.popleft()

            if a > b:
                res[idx] = a

            else:
                B.appendleft((b, idx))
                last = B.pop()[1]
                res[last] = a

        return res
