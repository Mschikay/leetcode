# def maxProfit(prices):
#     N = len(prices)
#
#     def dfs(s):
#         maxp = 0
#         if s >= N:
#             return 0
#
#         for start in range(s, N):
#             maxprofit = 0
#             for i in range(start + 1, N):
#                 if prices[i] > prices[start]:
#                     profit = dfs(i + 1) + prices[i] - prices[start]
#                     maxprofit = max(maxprofit, profit)
#             maxp = max(maxprofit, maxp)
#         return maxp
#     return dfs(0)
#
# print(maxProfit([3,2,6,5,0,3]))

def maxProfit(prices):
    i = 0
    valley = prices[0]
    peak = prices[0]
    maxprofit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        print(valley, peak)
        maxprofit += peak - valley

    return maxprofit


print(maxProfit([7,1,6,0,10,4]))