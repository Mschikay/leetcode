from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sums = [[-1 for i in range(len(nums))] for i in range(len(nums))]
        # for i in range(len(sums)):
        #     for j in range(i, len(sums[0])):
        #         if i == j:
        #             sums[i][j] = nums[j]
        #         else:
        #             sums[i][j] = sums[i][j - 1] + nums[j]
        #         if j - i >= 1 and (k and not sums[i][j] % k or not k and not sums[i][j]): return True
        # return False

        for i in range(1, len(nums)):
            if not nums[i] and not nums[i - 1]: return True
        if not k: return False

        rem = defaultdict(list)
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        for i in range(len(pre)):
            mod = pre[i] % k
            if mod not in rem:
                rem[mod].append(i)
            else:
                if i - rem[mod][0] > 1 and pre[i] - pre[rem[mod][0]] >= k: return True
        return False