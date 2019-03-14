class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        target = int(sumNums / 2)

        try:
            assert target * 2 == sumNums
        except:
            return False

        dp = [False for i in range(sumNums)]
        dp = [True] + dp
        for i in range(len(nums)):
            res = []
            for j in range(len(dp)):
                if dp[j] == True:
                    subSum = j + nums[i]
                    if subSum > sumNums:
                        continue
                    res.append(subSum)
            for r in res:
                dp[r] = True
            if dp[target] is True:
                return True

        return False