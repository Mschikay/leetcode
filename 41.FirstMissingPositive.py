class Solution:
    def firstMissingPositive(self, nums):
        # try:
        #     assert nums is not None and nums != []
        # except:
        #     return 1
        #
        # l = 0
        # r = len(nums) - 1
        # saved = nums[l]
        # while l < r:
        #     while nums[r] > 0 and r > l:
        #         r -= 1
        #     nums[l] = nums[r]
        #     while nums[l] <= 0 and l < r:
        #         l += 1
        #     nums[r] = nums[l]
        # nums[l] = saved
        #
        # newNums = []
        # if saved <= 0:
        #     newNums = nums[l + 1:]
        # else:
        #     newNums = nums[l:]
        #
        # newNums.sort()
        # if newNums == None or len(newNums) == 0:
        #     return 1
        # if newNums[0] > 1:
        #     return 1
        # for i in range(1, len(newNums)):
        #     if newNums[i] > newNums[i - 1] + 1:
        #         return newNums[i - 1] + 1
        # return newNums[-1] + 1


        '''a much time and space saving way! With time O(n), and space O(1)'''
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n

        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 3]))