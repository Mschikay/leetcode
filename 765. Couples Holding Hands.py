class Solution:

    def minSwapsCouples(self, row):
        root = [i if not i % 2 else i -1 for i in range(len(row))]
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        num = len(row) // 2
        for i in range(0, len(row), 2):
            x, y = row[i], row[i + 1]
            if find(x) == find(y): continue
            else:
                root[find(x)] = find(y)
                num -= 1
        return len(row) // 2 - num


class Solution:
    def minSwapsCouples(self, row):
        d = {}
        for i, v in enumerate(row):
            d[v] = i
        ans = 0
        for i in range(0, len(row), 2):
            x, y = row[i], row[i + 1]
            if x // 2 != y // 2:
                ans += 1
                p = 0
                if x % 2:
                    p = x - 1
                else:
                    p = x + 1
                ip = d[p]
                row[ip] = y
                d[y] = ip

        return ans
