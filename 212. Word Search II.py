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

        def dfs(wd, curr, i, j, ans):
            if "/" in wd and wd["/"]:
                ans.append(curr)
                wd["/"] = 0
            if i < 0 or i >= h or j < 0 or j >= w or not board[i][j]:
                return
            if board[i][j] in wd:
                ch = board[i][j]
                d = wd[board[i][j]]
                board[i][j] = 0
                dfs(d, curr + ch, i - 1, j, ans)
                dfs(d, curr + ch, i + 1, j, ans)
                dfs(d, curr + ch, i, j - 1, ans)
                dfs(d, curr + ch, i, j + 1, ans)
                board[i][j] = ch
            return

        ans = []
        for i in range(h):
            for j in range(w):
                dfs(trie, "", i, j, ans)
        return ans