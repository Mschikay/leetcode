class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bs(l, h, res):
            if l > h:
                return
            if l == h:
                if nums[l] == target:
                    res.append(l)
            mid = (l + h) // 2
            if nums[mid] >= target:
                bs(l, mid - 1, res)
            if nums[mid] == target:
                res.append(mid)
            if nums[mid] <= target:
                bs(mid + 1, h, res)

        l, h = 0, len(nums) - 1
        res = []
        bs(l, h, res)
        return [res[0], res[-1]] if res != [] else [-1, -1]