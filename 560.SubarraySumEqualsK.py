# easy veresion
# value = 0
#
# for start in range(1, num+1):
#     for end in range(start+1, num+1):
#         if end > num:
#             continue
#         if (start + end) / 2 > num / (end - start + 1):
#             break
#         elif (start + end) / 2 == num / (end-start+1):
#             print(start, end)
#             value += 1
#         else:
#             continue
#
# return value+1
#


# time consuming!!
# def subarraySum(self, nums: List[int], k: int) -> int:
#     def dfs(total, i, value):
#         if i >= len(nums):
#             return value
#         if total + nums[i] == k:
#             value += 1
#         return dfs(total + nums[i], i + 1, value)
#
#     value = 0
#     for idx in range(len(nums)):
#         value += dfs(0, idx, 0)
#
#     return value


def subarraySum(self, nums, k):
    sums = {0: 1}  # prefix sum array
    res = s = 0
    for n in nums:
        s += n  # increment current sum
        res += sums.get(s - k, 0)  # check if there is a prefix subarray we can take out to reach k
        sums[s] = sums.get(s, 0) + 1  # add current sum to sum count
    return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        res = subSum = 0

        for n in nums:
            subSum += n
            res += prefixSum.get(subSum - k, 0)
            prefixSum.setdefault(subSum, 0)
            prefixSum[subSum] += 1

        return res