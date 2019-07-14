class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # if not nums: return 0
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     m = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             m = max(m, dp[j])
        #     dp[i] = m + 1
        # return max(dp)

        def insert(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return l

        new = []
        for n in nums:
            if not new or n > new[-1]:
                new.append(n)
            else:
                idx = insert(new, n)
                new[idx] = n
        return len(new)