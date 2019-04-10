# 20 4
# 1
# 2
# 5
# 10

m = 20
n = 4
a = [1, 2, 5, 10]
a.sort()
a.reverse()

res = []


def dfs(a, sum, i):
    res.append(sum)
    print(i)
    if i > len(a):
        return
    else:
        sum += a[i]
        for y in range(i, len(a)+1):
            dfs(a, sum, y)

print(dfs(a, 0, 0))