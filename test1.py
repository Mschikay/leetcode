from collections import defaultdict

def q1(S1, S2):
    d = defaultdict(int)
    for s in range(len(S1)):
        d[S1[s]] = s
    step = abs(d[S2[0]] - d[S1[0]])
    for i in range(1, len(S2)):
        step += abs(d[S2[i]] - d[S2[i - 1]])
    return step

# [-1, 7, 0, 7, 8]
def Solution(A):
    preSum = [0]
    for a in A:
        preSum.append(preSum[-1] + a)
    length = len(A)
    level = 1
    maxVal = float("-inf")
    res = 0
    while (1 << level - 1) - 1 < length:
        val = (preSum[(1 << level) - 1] if (1 << level) - 1 <= length else preSum[-1]) \
            - (preSum[(1 << level - 1) - 1] if (1 << level - 1) - 1 >= 0 else 0)
        if val > maxVal:
            maxVal = val
            res = level
            level += 1
    return res

print(Solution([0, 0, 1, 8,9]))

print(q2([15, 7, 0, 7, 8]))




# print(q1('abcdefghijklmnopqrstuvwxyz', 'cba'))