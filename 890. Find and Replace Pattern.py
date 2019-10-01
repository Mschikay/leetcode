# for i in range(len(word)):
#     if word[i] not in dw and pattern[i] not in dp:
#         dw[word[i]] = pattern[i]
#         dp[pattern[i]] = word[i]
#     else:
#         if not word[i] in dw or not pattern[i] in dp:
#             return False
#         else:
#             if dw[word[i]] != pattern[i]:
#                 return False
# return True