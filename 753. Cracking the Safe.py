class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = pow(k, n)
        d = ""
        for i in range(k):
            d += str(i)

        def dfs(rest, cur, v):
            if not rest: return cur

            if n == 1:
                pre = ""
            else:
                pre = cur[-(n - 1):]
            for s in d:
                if pre + s not in v:
                    v.add(pre + s)
                    string = dfs(rest - 1, cur + s, v)  # a path can be guaranteed to be found
                    if string: return string
                    v.remove(pre + s)
            return None

        visited = set()
        visited.add("0" * n)
        return dfs(total - 1, "0" * n, visited)

