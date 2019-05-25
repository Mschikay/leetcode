class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        itvs = sorted(intervals, key=lambda itv: itv[0])
        l = r = 0
        res = []
        while r < len(itvs):
            maxr = itvs[l][1]
            while r < len(itvs) and itvs[r][0] <= maxr:
                maxr = max(maxr, itvs[r][1])
                r += 1
            res.append([itvs[l][0], maxr])
            l = r
        if r< len(itvs):
            res += itvs[r:]
        return res