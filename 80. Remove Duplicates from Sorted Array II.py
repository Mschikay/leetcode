class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 0
        for n in nums:
            if tail < 2 or n != nums[tail - 1] or n != nums[tail - 2]:
                nums[tail] = n
                tail += 1
        return tail 