from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = defaultdict(int)
        presum[0] = 1
        currsum = 0
        for n in nums:
            currsum += n
            if currsum - k in presum:
                ans += presum[currsum - k]
            presum[currsum] += 1
        return ans