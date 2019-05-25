from bisect import bisect_left, insort_left


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # def BinaryInsert(arr, target):
        #     l, h = 0, len(arr) - 1
        #     while l <= h:
        #         mid = (l + h) // 2
        #         if arr[mid] >= target:
        #             h = mid - 1
        #         if arr[mid] < target:
        #             l = mid + 1
        #     return l

        res = []
        arr = []
        nums.reverse()
        for n in nums:
            idx = bisect_left(arr, n)
            res.append(idx)
            arr[idx:idx] = [n]
        return res[::-1]