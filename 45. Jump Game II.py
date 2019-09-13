from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        q = deque()
        q.append((0, 0))
        v = set()

        while q:
            i, step = q.popleft()
            v.add(i)
            if i + nums[i] >= len(nums) - 1:
                return step + 1
            else:
                for x in range(1, nums[i] + 1):
                    if i + x not in v:
                        v.add(i + x)
                        q.append((i + x, step + 1))

