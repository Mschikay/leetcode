# time exceed
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A: return -1

        sums = [0]
        for a in A:
            sums.append(sums[-1] + a)
        print(sums)

        def find(l, h):
            if l == h - 1: return l if sums[l] >= K else float("inf")
            mid = (l + h) // 2
            res = min(find(l, mid), find(mid, h))
            left = sums[l:mid]
            for left in range(l, mid):
                right = mid
                while right < h and sums[right] - sums[left] < K:
                    right += 1
                if right < h:
                    res = min(res, right - left)
            return res

        res = find(1, len(sums))
        return -1 if res == float("inf") else res