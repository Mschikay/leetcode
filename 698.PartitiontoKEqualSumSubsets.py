class Solution:
    def canPartitionKSubsets(self, nums, k):
        target = sum(nums) // k
        try:
            assert target == sum(nums) / k
        except:
            return False

        def dfs(subSum, i, used, subK):
            print(used)

            if subSum == target:
                subK += 1
                if subK == k:
                    if sum(used) == len(used):
                        return True
                    else:
                        return False
                else:
                    for j in range(0, len(nums)):
                        if used[j] == 1:
                            continue
                        if dfs(0, j, used, subK):
                            return True
                    return False

            if subSum < target:
                for j in range(i, len(nums)):
                    if used[j] == 1:
                        continue
                    used[j] = 1
                    if dfs(subSum+nums[j], j+1, used, subK):
                        return True
                    used[j] = 0
                return False

            return False

        return dfs(0, 0, [0 for i in range(len(nums))], 0)


if __name__ == "__main__":
    s = Solution()
    print(s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))