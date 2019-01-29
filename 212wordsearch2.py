
from collections import deque

# key refers to the word that you are inserting or searching in the trie
# insertion and searching cost O(l) when L is length of key
# The memory requirements of trie is O(26 * l * N) N is number of keys in trie
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board:
            return []

        trie = {}

        for word in words:
            t = trie
            for w in word:
                t.setdefault(w, {})
                t = t[w]
            t["#"] = "#"

        results = []

        def dfs(wordDict, k, j, visited, path):
            if k < 0 or k > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or visited.get((k, j), None):
                return

            if board[k][j] in wordDict:
                if wordDict[board[k][j]].get("#", None):
                    results.append(path + board[k][j])

                visited[(k, j)] = 1
                dfs(wordDict.get(board[k][j]), k+1, j, visited, path+board[k][j])
                dfs(wordDict.get(board[k][j]), k-1, j, visited, path+board[k][j])
                dfs(wordDict.get(board[k][j]), k, j+1, visited, path+board[k][j])
                dfs(wordDict.get(board[k][j]), k, j-1, visited, path+board[k][j])
                visited[(k, j)] = None
            return

        # for dfs(), f(n) = 4 * f(n - 1) = 4^(l-1) * f(1)
        # so the cost is k * j * 4^(l-1), l is the max length of the tree.
        # There are many trees in trie
        # if you use pure dfs without trie: k * j * N * 4^(l - 1), you need to traverse every key
        for k in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie, k, j, {}, "")

        res = set(results)
        return res


if __name__ == "__main__":
    s = Solution()
    board = [["a","a"]]
    words = ["aa", "a"]
    # words = ["apple", "fan", "fuel"]
    print(s.findWords(board, words))

