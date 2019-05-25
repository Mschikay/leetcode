class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] >= target:
                break
            l, r, t = i + 1, len(nums) - 1, target - nums[i]
            while l < r:
                res = nums[l] + nums[r]
                if res >= t:
                    r -= 1
                else:
                    ans += r - l
                    l += 1
        return ans