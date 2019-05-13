class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if A is None:
            return False
        nums = {}
        for i, v in enumerate(A):
            nums[v] = nums.get(v, 0) + 1

        newA = [n for n in nums.keys()]
        newA.sort()

        for a in newA:
            if nums.get(a, 0) == 0:
                continue

            nexta = None
            if a < 0:
                nexta = a / 2
            elif a > 0:
                nexta = a * 2
            else:
                continue

            if nums.get(nexta, 0) == 0:
                return False
            else:
                nums[nexta] = nums[nexta] - nums[a]
                nums[a] = 0

        for k, v in nums.items():
            if k == 0:
                if v % 2 != 0:
                    return False
            else:
                if v != 0:
                    return False

        return True
