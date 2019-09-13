from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum1 = nums[i] + nums[j]
                d[sum1].append((i, j))

        result = set()
        for key, v1 in d.items():
            if target - key not in d: continue
            v2 = d[target - key]
            for (i, j) in v1:
                for (m, n) in v2:
                    if i != m and i != n and j != m and j != n:
                        res = [nums[i], nums[j], nums[m], nums[n]]
                        res.sort()
                        result.add(tuple(res))
        return list(result)


from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                l, r = j + 1, len(nums) - 1
                t = target - nums[i] - nums[j]
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        rr, ll = nums[r], nums[l]
                        while r > l and nums[r] == rr:
                            r -= 1
                        while l < r and nums[l] == ll:
                            l += 1
                    elif s < t: l += 1
                    else: r -= 1
        return res