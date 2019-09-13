class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        ans = 0
        for i in range(len(nums) - 2):
            target = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                res = nums[l] + nums[r]
                if res > target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
        return ans


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def search(arr, t):
        #     l, r = 0, len(arr) - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if arr[mid] < t:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return l

        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                res += bisect.bisect_left(nums[j + 1:], nums[i] + nums[j])
        return res