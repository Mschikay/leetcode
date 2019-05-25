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

