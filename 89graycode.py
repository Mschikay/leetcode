class Solution:
    def find(self, n):
        # n = 1:
        # 0
        # 0
        # 1
        # 0 + 2 ^ 0 < -- i = 0
        #
        # n = 2:
        # 00
        # 0
        # 01
        # 1
        # 11
        # 1 + 2 ^ 1 < -- i = 1
        # 10
        # 0 + 2 ^ 1
        #
        # n = 3:
        # 000
        # 0
        # 001
        # 1
        # 011
        # 3
        # 010
        # 2
        # 110
        # 2 + 2 ^ 2 < -- i = 2
        # 111
        # 3 + 2 ^ 2
        # 101
        # 1 + 2 ^ 2
        # 100
        # 0 + 2 ^ 2
        if n == 0:
            return [0]

        half = self.find(n-1)
        return half + [h + pow(2, n-1) for h in reversed(half)]

    def grayCode(self, n):
        visited = {}
        res = []

        def bt(i, before, path):
            if visited.get(before, None):
                return
            visited[before] = 1

            if i == pow(2, n):
                res.append(path + [before])
                return

            for b in range(n):
                next = before[:b] + str(abs(int(before[b]) - 1)) + before[b+1:]
                bt(i+1, next, path + [before])

        bt(1, "0" * n, [])
        print(res)
        return [int(r, 2) for r in res[0]]


if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(9))