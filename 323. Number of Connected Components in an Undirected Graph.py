class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        for a, b in edges:
            if root[a] != root[b]:
                root[find(a)] = find(b)

        roots = set()
        for i in range(n):
            roots.add(find(i))
        return len(roots)


class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def union(a, b):
            uf[find(a)] = find(b)

        def find(a):
            while a != uf[a]:
                uf[a] = uf[uf[a]]
                a = uf[a]
            return a

        uf = [i for i in range(n)]
        res = n

        for a, b in edges:
            if find(a) != find(b):
                union(a, b)
                res -= 1

        return res