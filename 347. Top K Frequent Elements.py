from collections import Counter
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = []
        heapify(h)

        for num, f in freq.items():
            if len(h) < k:
                heappush(h, (f, num))
            else:
                heappushpop(h, (f, num)) # the new element only need to be greater than the min in former top K
        ans = [x[1] for x in h]
        return ans