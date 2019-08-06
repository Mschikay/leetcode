'''brute force'''
from collections import deque


class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 1: return 1

        v = set()
        q = deque()
        q.append((A, 0))
        step = 0
        while q:
            curr, step = q.popleft()
            if curr == B: break
            tolist = list(curr)
            for i in range(1, len(curr)):
                for j in range(i):
                    tolist[j], tolist[i] = tolist[i], tolist[j]
                    s = "".join(tolist)
                    if s not in v:
                        v.add(s)
                        q.append((s, step + 1))
                    tolist[j], tolist[i] = tolist[i], tolist[j]
        return step


'''a little bit better'''
from collections import deque


class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 1: return 1

        def getNext(x):
            i = 0
            while x[i] == B[i]: i += 1
            for j in range(i + 1, len(x)):
                if x[j] == B[i]:
                    yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]

        v = set()
        q = deque()
        q.append((A, 0))
        step = 0
        while q:
            curr, step = q.popleft()
            if curr == B: break
            for n in getNext(curr):
                if n not in v:
                    v.add(n)
                    q.append((n, step + 1))
        return step


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        visited = {A}

        q = collections.deque()
        q.append(A)

        print(A)
        print(self.swap(A, 0, 1))

        cnt = 0
        while q:
            size = len(q)
            cnt = cnt + 1
            for i in range(size):

                cur = q.popleft()
                j = 0
                while j < len(cur) and cur[j] == B[j]:
                    j = j + 1

                for k in range(j + 1, len(cur)):
                    if cur[k] == B[k] or cur[j] != B[k]:
                        continue
                    nextWord = self.swap(cur, j, k)
                    if nextWord == B:
                        return cnt

                    if nextWord not in visited:
                        visited.add(nextWord)
                        q.append(nextWord)

        return cnt

    def swap(self, cur: str, j: int, k: int) -> str:

        a = cur[j]
        b = cur[k]

        return cur[:j] + b + cur[j + 1: k] + a + cur[k + 1:]

