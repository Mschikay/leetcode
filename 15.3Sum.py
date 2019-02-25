class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        try:
            assert nums is not None and len(nums) >= 3
        except:
            return []

        res = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1

                elif nums[i] + nums[l] + nums[r] < 0: # 不相等的情况下 不用考虑数字是否重复 反正重复情况下也不可能等于0
                    l += 1
                else:
                    r -= 1

            while i < len(nums) - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res