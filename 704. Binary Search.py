class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums: return -1
        # l, h = 0, len(nums) - 1
        # while l <= h:
        #     mid = (l + h) // 2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] < target:
        #         l = mid + 1
        #     if nums[mid] > target:
        #         h = mid - 1
        # return -1

        try:
            return nums.index(target)
        except:
            return -1