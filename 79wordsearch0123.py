import copy

class Solution(object):
    # time exceed error
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board or not word:
            return False

        for i in range(len(board)):
            board[i] = ['0'] + board[i] + ['0']
        board = [['0'] * len(board[0])] + board + [['0'] * len(board[0])]

        def dfs(i, k, j, visited):
            print(i, k, j)
            if word[i] == board[k][j] and not visited[k][j] is True:
                if i == len(word) - 1:
                    return True
                else:
                    visited[k][j] = True
                    res = (dfs(i + 1, k + 1, j, visited)
                            or dfs(i + 1, k - 1, j, visited)
                            or dfs(i + 1, k, j - 1, visited)
                            or dfs(i + 1, k, j + 1, visited))
                    visited[k][j] = False
                    return res
            return False

        for k in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                visit = [[False] * len(board[0])] * len(board)
                result = dfs(0, k, j, visit)
                if result:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(s.exist(board, word))