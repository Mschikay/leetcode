nums = [2, 7, 11, 15]
target = 9

def test():
    l = 0
    r = len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1
        else:
            r -= 1
    return []

print(test())