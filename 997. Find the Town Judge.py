class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        JContenders = [0]*(N+1)
        for i in trust:
            JContenders[i[0]] -= 1
            JContenders[i[1]] += 1
        for i in range(1, N+1):
            if JContenders[i] == N-1:
                return i
        return -1


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inDegree = [0 for i in range(N + 1)]
        outDegree = [0 for i in range(N + 1)]
        for a, b in trust:
            outDegree[a] += 1
            inDegree[b] += 1

        judge = False
        ans = -1
        for i in range(1, len(inDegree)):
            if inDegree[i] == N - 1 and not outDegree[i]:
                if judge:
                    return -1
                else:
                    judge = True
                    ans = i
        return ans