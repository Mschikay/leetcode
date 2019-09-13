'''in the worst case, it could be n * k, on average it is n * log(k)'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def split(l, r):
            b, v = l, nums[l]
            while l < r:
                while l < r and nums[r] > v:
                    r -= 1
                nums[b], b = nums[r], r
                while l < r and nums[l] <= v:
                    l += 1
                nums[b], b = nums[l], l
            nums[b] = v
            return b

        l, h = 0, len(nums) - 1
        while l <= h:
            m = split(l, h)
            if m < k:
                l = m + 1
            else:
                h = m - 1
        return nums[l]


from heapq import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for num in nums:
            if len(h) == k:
                heappushpop(h, num)
            else:
                heappush(h, num)
        return h[0]
