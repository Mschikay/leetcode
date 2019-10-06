class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                j = nums[i]
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] *= -1
        print(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(len(nums)):
            j = (nums[i] - 1) % l
            nums[j] += l
        ans = []
        for i in range(len(nums)):
            if nums[i] <= l:
                ans.append(i + 1)
        return ans