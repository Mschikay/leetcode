from collections import Counter

from collections import Counter, defaultdict


class Solution:
    def minSubArrayLen(self, s, nums):  # 如果是找恰好是这个值的可以用preSum
        preSum = [0]
        for n in nums:
            preSum.append(n + preSum[-1])
        d = defaultdict(int)
        for i, p in enumerate(preSum):
            d[p] = i
        minLen = float("inf")
        for i in range(1, len(preSum)):
            if preSum[i] - s in d.keys():
                minLen = min(minLen, i - d[preSum[i] - s])

        return 0 if minLen == float("inf") else minLen

        '''2 pointers'''
        i = j = 0
        ans = float("inf")
        res = 0
        while j < len(nums):
            res += nums[j]
            j += 1
            while res >= s:
                ans = min(ans, j - i)
                res -= nums[i]
                i += 1
        return ans if ans != float("inf") else 0

    '''binary search'''
    def minSubArrayLen(self, s, nums):
        preSum = [0]
        for n in nums:
            preSum.append(n + preSum[-1])

        def findMinLen(l, h):
            last = preSum[h]
            while l <= h:
                mid = (l + h) // 2
                if last - preSum[mid] < s:
                    h = mid - 1
                else:
                    l = mid + 1
            return h

        l, minLen = 0, len(preSum)
        for r, v in enumerate(preSum):
            if v >= s:
                l = findMinLen(l, r)
                minLen = min(minLen, r - l)

        return 0 if minLen == len(preSum) else minLen
