nums = [1,1,2,5,4,6,7,8]
'''
1 2 1

'''
for i in range(len(nums)):
    while nums[nums[i] - 1] != nums[i]:
        j = nums[i]
        nums[i], nums[j - 1] = nums[j - 1], nums[i]
