class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [0 for i in range(len(edges) * 2)]
        rank = [0 for i in range(len(edges) * 2)]

        def find(x):
            if not p[x]: return x
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            elif rank[px] == rank[py]:
                p[py] = x
                rank[x] += 1
            elif rank[px] < rank[py]:
                p[px] = py
            else:
                p[py] = px
            return True

        for x, y in edges:
            if not union(x, y): return [x, y]



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        Parent = [ i for i in range(len(edges)+1) ]

        def find(i):
            if Parent[i] != i:
                Parent[i] = find(Parent[i])
            return Parent[i]

        def union(i, j):
            p1, p2 = find(i), find(j)
            Parent[p1] = p2

        def connected(i, j):
            return find(i) == find(j)

        for e in edges:
            if connected(e[0], e[1]):
                return e
            union(e[0], e[1])