class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float("inf")
        maxpro = 0
        for p in prices:
            minp = min(minp, p)
            maxpro = max(maxpro, p - minp)
        return maxpro
