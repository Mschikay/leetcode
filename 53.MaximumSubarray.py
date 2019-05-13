# transfer function: f(i) = f(i) + f(i - 1) if f(i - 1) > 0 else 0. 94%
class Solution:
    def maxSubArray(self, nums):
        dp = [nums[0]] * len(nums)
        m = nums[0]
        rs = re = start = end = 0

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                end = i
                dp[i] = nums[i] + dp[i - 1]
            else:
                start = end = i
                dp[i] = nums[i]

            if m < dp[i]:
                rs = start
                re = end
                m = dp[i]
        return nums[rs:re + 1]
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

import sys

# if we use constant space 35%
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr = nums[0]
#         res = nums[0]
#         for i in range(1, len(nums)):
#             curr = max(nums[i] + curr, nums[i])
#             res = max(res, curr)
#         return res
#
#
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         def leftsum(nums, l, h):
#             left = 0
#             maxLeft = float("-inf")
#             for i in range(h, l - 1, -1):
#                 left += nums[i]
#                 maxLeft = max(left, maxLeft)
#             return maxLeft if maxLeft != float("-inf") else 0
#
#         def rightsum(nums, l, h):
#             right = 0
#             maxRight = float("-inf")
#             for i in range(l, h + 1):
#                 right += nums[i]
#                 maxRight = max(right, maxRight)
#
#             return maxRight if maxRight != float("-inf") else 0
#
#         def maxSum(nums, l, h):
#             if l == h:
#                 return nums[l]
#             mid = (l + h) // 2
#             cross = leftsum(nums, l, mid) + rightsum(nums, mid + 1, h)
#             return max(maxSum(nums, l, mid), cross, maxSum(nums, mid + 1, h))
#
#         return maxSum(nums, 0, len(nums) - 1)

