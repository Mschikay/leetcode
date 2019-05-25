class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def search(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    h = mid - 1
                if arr[mid] < target:
                    l = mid + 1
            return l

        if not nums: return 0
        dp = [nums[0]]
        for n in nums:
            if n > dp[-1]:
                dp.append(n)
            else:
                dp[search(dp, n)] = n
        return len(dp)