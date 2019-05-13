# O(n ** 2)
#
#
# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         ages.sort()
#         res = 0
#         for b in range(0, len(ages) - 1):
#             for a in range(b + 1, len(ages)):
#                 if ages[b] > 0.5 * ages[a] + 7:
#                     if ages[b] == ages[a]:
#                         res += 2
#                     else:
#                         res += 1
#                 else:
#                     break
#         return res


