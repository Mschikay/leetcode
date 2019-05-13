# DFS

# default every number on 1 works
# input: 4
# output:
# [False, True, True, True, False] 0
# [False, True, False, True, True] 1
# [False, True, True, False, True] 2
# [False, True, True, True, False] 3
# [False, False, True, True, True] 4
# [False, True, True, False, True] 5
# [False, True, False, True, True] 6
# [False, False, True, True, True] 7
class Solution:
    def countArrangement(self, N: int) -> int:
        def dfs(visited, loc, number, res):
            if number % loc == 0 or loc % number == 0:
                if loc == N:
                    return res + 1
                for newN in range(1, len(visited)):
                    if visited[newN]:
                        continue
                    visited[newN] = True
                    res = dfs(visited, loc + 1, newN, res)
                    visited[newN] = False
            return res

        visited = [False for i in range(N + 1)]
        return dfs(visited, 1, 1, 0)


#
class Solution:
    def countArrangement(self, N: int) -> int:
        def dfs(visited, loc, number, res):
            if loc == 0 or number % loc == 0 or loc % number == 0:
                if loc == N:
                    print(visited, res)
                    return res + 1
                for newN in range(1, len(visited)):
                    if visited[newN]:
                        continue
                    visited[newN] = True
                    res = dfs(visited, loc + 1, newN, res)
                    visited[newN] = False
            return res

        visited = [False for i in range(N + 1)]
        return dfs(visited, 1, 0, 0)

# 看不懂的一个解
# https://leetcode.com/problems/beautiful-arrangement/discuss/99758/3-liner-DFS-with-%22Trie%22-perspective-(detailed-explanation-with-picture-illustration)

