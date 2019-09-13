class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        root = [i for i in range(n)]
        N = n
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        for i, j in edges:
            fi, fj = find(i), find(j)
            if fi == fj: return False
            N -= 1
            root[fi] = fj
        return N == 1