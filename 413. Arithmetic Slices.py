#   2 pointers
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cnt = 0
        l, r = 0, 1
        while r < len(A) - 1:
            while r < len(A) - 1 and A[r + 1] - A[r] == A[r] - A[r - 1]:
                r += 1
            if r > l + 1:
                cnt += (r - l) * (r - l - 1) // 2
            l = r
            r += 1
        return cnt
#   dp, more space O(n)
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         dp = [0]*len(A)
#         sum = 0
#         for i in range(2, len(A)):
#             if A[i] - A[i-1] == A[i-1] - A[i-2]:
#                 dp[i] = dp[i-1] + 1
#                 sum += dp[i]

#         return sum

# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         cnt = 0
#         for s in range(len(A) - 2):
#             diff = A[s+1] - A[s]
#             for e in range(s+2, len(A)):
#                 if A[e] - A[e-1] == diff:
#                     cnt += 1
#                 else:
#                     break

#         return cnt