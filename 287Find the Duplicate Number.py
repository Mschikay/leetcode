class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        low = 1
        high = len(nums)
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
