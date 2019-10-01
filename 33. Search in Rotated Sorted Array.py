class Solution:
    def search(self, nums, target):
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[h]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1


class Solution:
    def search(self, nums, target):
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[-1]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1 if h == -1 or nums[h] != target else h