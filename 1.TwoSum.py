from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
            x = target - n
            if x in d:
                if x != n:
                    return [i, d[x][0]]
                else:
                    if len(d[x]) > 1:
                        return [d[x][0], d[x][1]]



# use 2 pointers
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            x, y, res = nums[l], nums[r], nums[l] + nums[r]
            if res == target:
                return [d[x][0], d[x][1]] if x == y else [d[x][0], d[y][0]]
            elif res < target:
                l += 1
            else:
                r -= 1

