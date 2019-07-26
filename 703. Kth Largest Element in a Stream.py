class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.nums.sort()

    def add(self, val: int) -> int:
        l, h = 0, len(self.nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if self.nums[mid] < val:
                l = mid + 1
            else:
                h = mid - 1
        self.nums = self.nums[:l] + [val] + self.nums[l:]
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for n in nums:
            if len(self.nums) < self.k:
                heappush(self.nums, n)
            else:
                heappushpop(self.nums, n)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)