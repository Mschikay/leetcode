class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > mid:
                h = mid - 1
            else:
                l = mid + 1
        return l


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= (i + 1) ^ nums[i]
        return res


## WITH DUPLICATE
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 1
        n = len(nums)
        while i < len(nums):
            if nums[i] == n:
                if len(nums) == n:
                    nums.append(nums[i])
                i += 1
                continue

            if nums[i] == i or nums[i] == nums[nums[i]]:
                i += 1
                continue

            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)