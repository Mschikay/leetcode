# O(n ** 2)
#
#
# class Solution:
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         res = float("-inf")
#         for i in range(len(A)):
#             sarr = i + A[i]
#             for j in range(i + 1, len(A)):
#                 res = max(res, sarr + A[j] - j)
#         return res


# O(n)
# from the last to the first, and make sure the j is always behind i
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = float("-inf")
        j = len(A) - 1
        for i in range(len(A) - 2, -1, -1):
            res = max(res, A[i] + i + A[j] - j)
            if A[i] - i > A[j] - j:
                j = i
        return res
