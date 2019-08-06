class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #         mem = {}
        #         def dfs(w1, w2):
        #             if not w1 and not w2: return 0
        #             if not w1: return len(w2)
        #             if not w2: return len(w1)
        #             if (w1, w2) in mem: return mem[(w1, w2)]
        #             if w1[-1] != w2[-1]:
        #                 mem[(w1, w2)] = 1 + min(dfs(w1, w2[:-1]), dfs(w1[:-1], w2), dfs(w1[:-1], w2[:-1]))
        #             else:
        #                 mem[(w1, w2)] = dfs(w1[:-1], w2[:-1])
        #             return mem[(w1, w2)]

        #         return dfs(word1, word2)

        dist = [[0 for i in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for x in range(len(word2)):
            dist[0][x + 1] = 1 + dist[0][x]
        for x in range(len(word1)):
            dist[x + 1][0] = 1 + dist[x][0]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dist[i + 1][j + 1] = dist[i][j]
                else:
                    dist[i + 1][j + 1] = 1 + min(dist[i + 1][j], dist[i][j + 1], dist[i][j])
        return dist[-1][-1]