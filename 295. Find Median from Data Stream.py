from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller_max_heap = []
        self.greater_min_heap = []
        heapify(self.smaller_max_heap)
        heapify(self.greater_min_heap)

    def addNum(self, num: int) -> None:
        if not self.smaller_max_heap or num < -self.smaller_max_heap[0]:
            heappush(self.smaller_max_heap, -num)
        else:
            heappush(self.greater_min_heap, num)

        '''when max_heap length - min_heap length <= 1: it is balanced. '''
        if len(self.smaller_max_heap) - len(self.greater_min_heap) == 2:
            heappush(self.greater_min_heap, -heappop(self.smaller_max_heap))
        elif len(self.greater_min_heap) > len(self.smaller_max_heap):
            heappush(self.smaller_max_heap, -heappop(self.greater_min_heap))

    def findMedian(self) -> float:
        if not self.smaller_max_heap: return None
        if len(self.smaller_max_heap) > len(self.greater_min_heap): return -self.smaller_max_heap[0]
        return (-self.smaller_max_heap[0] + self.greater_min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()