from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        for l in d.values():
            for i in range(1, len(l)):
                if l[i] - l[i - 1] <= k:
                    return True
        return False


from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = defaultdict(lambda: float("-inf"))
        for i, v in enumerate(nums):
            if i - d[v] <= k:
                return True
            d[v] = i
        return False