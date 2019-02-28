class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        try:
            nums is not None and nums != []
        except:
            return []

        l = 0
        r = len(nums) - 1
        color = 0

        # while i <= r:
        #     if nums[i] == 0:
        #         nums[l], nums[i] = nums[i], nums[l]
        #         l = l + 1
        #         i += 1
        #     elif nums[i] == 1:
        #         i += 1
        #     elif nums[i] == 2:
        #         nums[r], nums[i] = nums[i], nums[r]
        #         r = r - 1
        #     else:
        #         pass
        # print(nums)

        for i in range(2):
            while True:
                while nums[l] == color and l < r:
                    l += 1
                while nums[r] > color and r >= 0:
                    r -= 1
                if l >= r:
                    break
                nums[l], nums[r] = nums[r], nums[l]

            r = len(nums) - 1
            color = 1

