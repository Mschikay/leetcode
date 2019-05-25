class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if mid % 2 == 0:
                if mid - 1 >= l and nums[mid] == nums[mid - 1]:  # left
                    h = mid - 2  # [0, ]
                elif mid + 1 <= h and nums[mid] == nums[mid + 1]:  # right
                    l = mid + 2  # [2, ]
                else:
                    return nums[mid]
            elif mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:  # right
                    l = mid + 1  # [2, ]
                elif mid + 1 <= h and nums[mid] == nums[mid + 1]:  # left
                    h = mid - 1  # [0, ]
                else:
                    return nums[mid]

        return nums[h]

