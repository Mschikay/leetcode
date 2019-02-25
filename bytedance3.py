n, k = [int(x) for x in input().split()]
strs = []
for i in range(n):
    strs.append(input())


def dfs(strList):
    result = []
    if len(strList) == 1:
        return strList

    for s in range(len(strList)):
        newStrList = strList[:s] + strList[s + 1:]
        rest = dfs(newStrList)
        for r in rest:
            result += [strList[s] + r]
    return result


perm = dfs(strs)
permdict = {}
result = {}
#print(len(perm))
length = len(perm[0])
total = []

for p in perm:
    if permdict.get(p, None):
        total.append(result[permdict[p]] - k)
        continue

    num = 0
    for x in range(1, length):
        if p[x] !=  p[0]:
            continue
        mutate = p[x:] + p[0:x]
        permdict.setdefault(mutate, p)
        if mutate == p:
            num += 1
    num += 1
    result[p] = num
    total.append(result[p] - k)

print(total.count(0))