from collections import defaultdict


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        l = len(intervals)
        i = j = 0
        ans = []
        while i < l and j < l:
            curr = intervals[i]
            while j < l and intervals[j][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[j][1])
                j += 1
            ans.append(curr)
            i = j
        return ans


'''use union find'''
root = [i for i in range(len(intervals))]


def find(i):
    if i != root[i]:
        root[i] = find(root[i])
    return root[i]


for i in range(len(intervals)):
    m, n = intervals[i]
    for j in range(i + 1, len(intervals)):
        p, q = intervals[j]
        if m <= p <= n <= q or p <= m <= q <= n or m <= p <= q <= n or p <= m <= n <= q:
            root[find(i)] = find(j)

d = defaultdict(list)
for i in range(len(root)):
    k = find(i)
    if not d[k]:
        d[k] = intervals[i]
    else:
        d[k][0], d[k][1] = min(d[k][0], intervals[i][0]), max(d[k][1], intervals[i][1])
ans = []
for k, v in d.items():
    ans.append(v)
return ans