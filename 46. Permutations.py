'''
                []
        1       2       3
    2   3    1  3    1  2
    3   2    3  1    2  1

time: n!

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr, ans, v):
            if len(v) == len(nums):
                ans.append(curr)
                return
            for j in range(len(nums)):
                if j in v: continue
                v.add(j)
                dfs(curr + [nums[j]], ans, v)
                v.remove(j)

        ans = []
        v = set()
        dfs([], ans, v)
        return ans

