class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            cur = nums[i + 1:i + k + 1]
            for c in cur:
                if abs(c -nums[i]) <= t:
                    return True
        return False