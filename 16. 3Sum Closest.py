import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dif = float("inf")
        res = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                newDif = abs(s - target)
                if newDif < dif:
                    dif = newDif
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return s
        return res
