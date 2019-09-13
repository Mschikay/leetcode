class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        res = 0
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            t = target - nums[i]
            while l < r:
                if nums[l] + nums[r] < t:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            i += 1
        return res


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        res = 0
        nums.sort()
        i = 0

        for l in range(len(nums) - 2):
            for r in range(l + 2, len(nums)):
                t = target - nums[l] - nums[r]
                arr = nums[l + 1:r]
                res += bisect.bisect_left(arr, t)
        return res