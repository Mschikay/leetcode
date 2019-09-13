




def partition(nums):
    b, v = 0, nums[0]
    l, r = 0, len(nums) - 1
    while l < r:
        while l < r and not nums[r] % 2:
            r -= 1
        nums[b], b = nums[r], r
        while l < r and nums[l] % 2:
            l += 1
        nums[b], b = nums[l], l
    nums[b] = v
    print(nums)
    return nums

partition([2, 3, 41,2, 4,3,6,8,8,9,9,6])