from collections import Counter

from collections import Counter, defaultdict


class Solution:
    def minSubArrayLen(self, s, nums):# 如果是找恰好是这个值的可以用preSum
        preSum = [0]
        for n in nums:
            preSum.append(n + preSum[-1])
        d = defaultdict(int)
        for i, p in enumerate(preSum):
            d[p] = i
        minLen = float("inf")
        for i in range(1, len(preSum)):
            if preSum[i] - s in d.keys():
                minLen = min(minLen, i - d[preSum[i] - s])

        return 0 if minLen == float("inf") else minLen


class Solution:
    def minSubArrayLen(self, s, nums):
        if nums is None or len(nums) == 0:
            return 0

        l = r = 0
        curr = 0
        minLen = float("inf")
        while r < len(nums):
            while r < len(nums) and curr < s:
                curr += nums[r]
                r += 1

            while l < r and curr >= s:
                if curr >= s:
                    minLen = min(r - l, minLen)
                curr -= nums[l]
                l += 1

        while l < r and curr >= s:
            if curr >= s:
                minLen = min(r - l, minLen)
            curr -= nums[l]
            l += 1

        return 0 if minLen == float("inf") else minLen


import sys

# A not elegant solution
# import sys
#
# class Solution:
#     def minSubArrayLen(self, s, nums):
#         if nums is None or len(nums) == 0:
#             return 0
#
#         l = r = 0
#         subSum = nums[l]
#         minLength = sys.maxsize
#
#         while True:
#             if subSum >= s:
#                 length = r - l + 1
#                 if minLength > length:
#                     minLength = length
#                 subSum -= nums[l]
#                 l += 1
#
#             else:
#                 r += 1
#                 if r >= len(nums):
#                     break
#                 subSum += nums[r]
#
#             if l > r:
#                 r = l
#                 if r >= len(nums):
#                     break
#                 subSum = nums[l]
#
#         if minLength == sys.maxsize:
#             return 0
#         return minLength

class Solution:
    def minSubArrayLen(self, s, nums):
        if nums is None or len(nums) == 0:
            return 0

        l = 0
        subSum = 0
        minLength = len(nums) + 1 # this step is tricky

        for r, v in enumerate(nums):
            subSum += v
            while l <= r:
                if subSum < s:
                    break
                else:
                    minLength = min(minLength, r - l + 1)
                    subSum -= nums[l]
                    l += 1
        return minLength if minLength <= len(nums) else 0


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(15, [1,2,3,4,5]))