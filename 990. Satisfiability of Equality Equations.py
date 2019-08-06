class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        notequal = []
        root = {}

        def find(c):
            if root[c] != c:
                root[c] = find(root[c])
            return root[c]

        for e in equations:
            a, b = e[0], e[-1]
            if a not in root:
                root[a] = a
            if b not in root:
                root[b] = b
            if e[1:3] == "==":
                root[find(a)] = find(b)
            else:
                notequal.append((a, b))

        for a, b in notequal:
            if find(a) == find(b):
                return False
        return True


class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        graph = collections.defaultdict(set)
        notEquals = []

        def canMeet(u, target, visited):
            if u == target:
                return True
            visited.add(u)
            for v in graph[u]:
                if v in visited:
                    continue
                if canMeet(v, target, visited):
                    return True
            return False

        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                notEquals.append((a, b))
                continue
            u, v = eq.split('==')
            graph[u].add(v)
            graph[v].add(u)

        for u, v in notEquals:
            if canMeet(u, v, set()):
                return False
        return True