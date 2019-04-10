class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if A is None or B is None or C is None or D is None:
            return []

        pair1 = {}
        pair2 = {}
        length = len(A)
        for i in range(length):
            for j in range(length):
                sum1, sum2 = A[i] + B[j], C[i] + D[j]
                key1, key2 = pair1.setdefault(sum1, []), pair2.setdefault(sum2, [])
                key1.append([i, j])
                key2.append([i, j])

        res = 0
        for k, v in pair1.items():
            target = -k
            targetValue = pair2.get(target, [])
            res += len(v) * len(targetValue)

        return res

# REFINED
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if A is None or B is None or C is None or D is None:
            return []

        pair = {}
        for a in A:
            for b in B:
                pair[a + b] = pair.get(a + b, 0) + 1

        res = 0
        for c in C:
            for d in D:
                res += pair.get(-c - d, 0)

        return res
