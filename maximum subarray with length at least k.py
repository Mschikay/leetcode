class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        '''
        1, max(nums)
        n, sum(nums)
        '''
        if len(nums) < k: return -1
        premin = [nums[0]]
        m = float("inf")
        presum = nums[0]
        for i in range(1, k):
            presum += nums[i]
            m = min(m, presum)
            premin.append(m)
        ans = presum
        for i in range(k, len(nums)):
            presum += nums[i]
            m = min(m, presum)
            premin.append(m)
            ans = max(ans, presum - premin[i - k])
        return ans