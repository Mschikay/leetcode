
'''domino'''
from collections import defaultdict
def solution(A, B):
    if not A or not B: return -1
    l1, l2 = len(A), len(B)
    if l1 != l2:
        return -1

    l, v1, v2 = l1, A[0], B[0]
    da = defaultdict(lambda: 0)
    db = defaultdict(lambda: 0)
    for i in range(l):
        a, b = A[i], B[i]
        if a not in (v1, v2) and b not in (v1, v2): return -1
        if a == b:
            if a == v1:
                l1 -= 1
            else:
                l2 -= 1
            continue
        if a in (v1, v2):
            da[a] += 1
        if b in (v1, v2):
            db[b] += 1

    ans = l
    if da[v1] + db[v1] >= l1:
        ans = min(da[v1], db[v1])
    if da[v2] + db[v2] >= l2:
        ans = min(ans, min(da[v2], db[v2]))
    return -1 if ans == l else ans


print(solution([2, 1, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2]))