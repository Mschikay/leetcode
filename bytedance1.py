# 时间限制：1秒
#
# 空间限制：32768K
#
# 有 n 个字符串，每个字符串都是由 A-J 的大写字符构成。现在你将每个字符映射为一个 0-9 的数字，不同字符映射为不同的数字。这样每个字符串就可以看做一个整数，唯一的要求是这些整数必须是正整数且它们的字符串不能有前导零。现在问你怎样映射字符才能使得这些字符串表示的整数之和最大？
#
#
# 输入描述:
# 每组测试用例仅包含一组数据，每组数据第一行为一个正整数 n ， 接下来有 n 行，每行一个长度不超过 12 且仅包含大写字母 A-J 的字符串。 n 不大于 50，且至少存在一个字符不是任何字符串的首字母。
#
#
# 输出描述:
# 输出一个数，表示最大和是多少。
#
#
# 输入例子1:
# 2
# ABC
# BCA
#
# 输出例子1:
# 1875

n = int(input())
array = []
for i in range(n):
    array.append(input())

c = {}
maxLength = 0
initial = set()
for arr in array:
    initial.add(arr[0])
    if len(arr) > maxLength:
        maxLength = len(arr)
for arr in array:
    loc = maxLength - 1
    for i in range(len(arr) - 1, -1, -1):
        c.setdefault(arr[i], [0] * maxLength)
        c[arr[i]][loc] += 1
        loc -= 1
#print(c)
intC = []
for k, v in c.items():
    toInt = 0
    order = maxLength - 1
    for vl in range(len(v)):
        toInt += (v[vl]) * 10 ** (order)
        order -= 1
    intC.append((toInt, k))
intC.sort()

#print(intC)
#print(initial)
if intC[-1][1] in initial:
    for i in range(len(intC)):
        if intC[i][1] in initial:
            continue
        mappinZero = intC[i][0]
        zero = intC[i][1]
        intC.remove((mappinZero, zero))
        intC = [(mappinZero, zero)] + intC
        break
#print(intC)

mapping = {}
m = 9
for i in range(len(intC) - 1, -1, -1):
    k = intC[i][1]
    mapping[k] = m
    m -= 1
#print(mapping)

total = 0
for i in intC:
    total += i[0]*mapping[i[1]]
print(total)







