class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        low = 1
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
                continue
            high = mid - 1
        return low

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums)
        while low < high:
            mid = (low + high) // 2

            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, f = nums[0], nums[0]
        s = nums[s]
        f = nums[nums[f]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]

        ans = nums[0]
        while ans != s:
            ans = nums[ans]
            s = nums[s]
        return ans