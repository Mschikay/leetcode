class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        if not A: return 0
        if len(A) == 1: return 1

        root = {}
        for a in A: root[a] = a

        def find(w):
            if w != root[w]:
                root[w] = find(root[w])
            return root[w]

        l = len(A[0])

        def checkWord(w):
            for i in range(1, len(w)):
                for j in range(i):
                    w1 = w[:j] + w[i] + w[j + 1:i] + w[j] + w[i + 1:]
                    if w1 in root:
                        root[find(w1)] = find(w)

        def similar(w1, w2):
            dif = 0
            for i in range(l):
                if w1[i] != w2[i]:
                    dif += 1
                    if dif > 2: return False
            return True

        if l * l < len(A):
            for i in range(len(A)):
                checkWord(A[i])
        else:
            for i in range(1, len(A)):
                for j in range(i):
                    if similar(A[j], A[i]):
                        root[find(A[j])] = find(A[i])
        group = set()
        for w in A:
            group.add(find(w))
        return len(group)

