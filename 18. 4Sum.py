# O(n ** 3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        res = []
        i = 0
        j = 1

        while i < len(nums) - 3:
            while j < len(nums) - 2:
                prei, prej, l, r = nums[i], nums[j], j + 1, len(nums) - 1
                newT = target - (nums[i] + nums[j])

                while l < r:
                    curSum = nums[l] + nums[r]
                    if curSum >= newT:
                        if curSum == newT:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        while nums[r] == nums[r + 1] and r > l:
                            r -= 1
                    else:
                        l += 1
                        while nums[l] == nums[l - 1] and r > l:
                            l += 1
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j += 1

            i += 1
            j = i + 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
                j = i + 1

        return res

# O(n ** 2)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in d:
                    d[sum2].append((i, j))
                else:
                    d[sum2] = [(i, j)]

        result = set()
        for key, v1 in d.items():
            v2 = d.get(target - key, [])
            for (i, j) in v1:
                for (m, n) in v2:
                    if i != m and m != j and i != n and j != n:
                        res = [nums[i], nums[j], nums[m], nums[n]]
                        res.sort()
                        result.add(tuple(res))
        return list(result)
