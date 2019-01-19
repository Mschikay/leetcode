

'''
append是作为一个整体追加
extend是整体且字符串会被拆分
insert是整体并且是特定位置添加
'''

#这是最长子序列？？？？
# def solve(string):
#     length = 1
#     i = 1
#     res = [string[0]]+[""] * (len(string)-1)
#     while i < len(string):
#         res[i] = res[i-1]
#         if string[i] not in res[i]:
#             res[i] = res[i] + string[i]
#         else:
#             j = i-1
#             while string[j] not in res[i]:
#                 res[i] = string[j:i+1]
#                 j -= 1
#         i += 1
#     print(res)
#     return


def solve(string):
    charmap = dict()
    length = 1
    i = 1
    res = [string[0]]+[""] * (len(string)-1)
    flag = 0
    while i < len(string):
        res[i] = res[i-1]
        # 如果这是一个没有重复出现的字母，那么这个位置的最优结果加上这个字母
        if string[i] not in res[i]:
            res[i] = res[i] + string[i]
        #如果重复了，就往前找开始重复的地方 这个位置的最优结果为一个新的字符串
        #比如在第3个位置就是"sw"，第6个位置是ekw
        else:
            if charmap[string[i]] >= flag:
                flag = charmap[string[i]] + 1
            res[i] = string[flag:i+1]
        charmap[string[i]] = i
        # 存最长子串的长度
        if len(res[i]) >= length:
            length = len(res[i])
        i += 1
    for substring in res:
        if len(substring) == length:
            print(substring)
    return


if __name__ == "__main__":
    solve("awswekwo")

