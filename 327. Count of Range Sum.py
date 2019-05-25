class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums: return 0
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)

        def find(l, h):
            mid = (l + h) // 2
            if mid == l:
                if lower <= sums[l] <= upper:
                    return 1
                return 0

            res = find(l, mid) + find(mid, h)
            left = sums[l:mid]
            for le in left:
                i = mid
                while i < h and sums[i] - le < lower: i += 1
                j = i
                while j < h and sums[j] - le <= upper: j += 1
                res += j - i
            sums[l:h] = sorted(sums[l:h])
            return res

        return find(1, len(sums))