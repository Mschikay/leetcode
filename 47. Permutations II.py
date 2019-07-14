class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, curr, ans, v):
            if len(curr) == len(nums):
                ans.append(curr)
            currv = set()
            for j in range(len(nums)):
                if j in v or nums[j] in currv: continue
                v.add(j)
                currv.add(nums[j])
                dfs(j + 1, curr + [nums[j]], ans, v)
                v.remove(j)

        ans = []
        v = set()
        dfs(0, [], ans, v)
        return ans