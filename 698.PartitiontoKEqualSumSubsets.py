class Solution:
    def canPartitionKSubsets(self, nums, k):
        target = sum(nums) // k
        try:
            assert target == sum(nums) / k
        except:
            return False

        print(target)

        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        def dfs(i, check, subTarget):
            if nums[i] + subTarget <= target:
                if nums[i] + subTarget == target:
                    if False not in check:
                        return True
                    for c in range(len(check)):
                        if check[c] is False:
                            check[c] = True
                            if dfs(c, check, 0):
                                return True
                        check[c] = False
                else:
                    for c in range(len(check)):
                        if check[c] is False:
                            check[c] = True
                            if dfs(c, check, nums[i] + subTarget):
                                return True
                        check[c] = False
                    
            return False

        return dfs(0, [True]+[False for i in range(len(nums)-1)], 0)


if __name__ == "__main__":
    s = Solution()
    s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3)