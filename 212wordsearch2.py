from collections import defaultdict


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board:
            return []

        trie = defaultdict()
        for w in words:
            d = trie
            for c in w:
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]
            d["/"] = 1
        h, w = len(board), len(board[0])

        def dfs(visited, wd, curr, i, j, ans):
            if "/" in wd and wd["/"]:
                ans.append(curr)
                wd["/"] = 0 # 这是用来去重的
            if i < 0 or i >= h or j < 0 or j >= w or (i, j) in visited:
                return
            if board[i][j] in wd:
                visited.add((i, j))
                dfs(visited, wd[board[i][j]], curr + board[i][j], i - 1, j, ans)
                dfs(visited, wd[board[i][j]], curr + board[i][j], i + 1, j, ans)
                dfs(visited, wd[board[i][j]], curr + board[i][j], i, j - 1, ans)
                dfs(visited, wd[board[i][j]], curr + board[i][j], i, j + 1, ans)
                visited.remove((i, j))
            return

        ans = []
        for i in range(h):
            for j in range(w):
                visited = set()
                dfs(visited, trie, "", i, j, ans)
        return ans