'''
Binary search is not fast at all!
Counter.items() seems quicker than Counter.keys()????
'''
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        d = d1 & d2
        res = []
        for k in d.keys():
            res += [k] * d[k]
        return res

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        d = d1 & d2
        res = []
        for k, v in d.items():
            res += [k] * v
        return res