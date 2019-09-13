from collections import defaultdict


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        ans = 0
        d = defaultdict()
        for i, v in enumerate(presum):
            if v not in d:
                d[v] = i
        for i in range(1, len(presum)):
            if presum[i] - k in d:
                ans = max(ans, i - d[presum[i] - k])
        return ans

1,2,3
0,1,3,6