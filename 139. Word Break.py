import collections
# Time Limit Exceeded dfs
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(word, i):
            if word[0:i] in wordDict:
                if i == len(word):
                    return True
                else:
                    newWord = word[i:]
                    for j in range(1, len(newWord) + 1):
                        if dfs(newWord, j):
                            return True
                    return False
            else:
                if i == len(word):
                    return False
                else:
                    for j in range(i + 1, len(word) + 1):
                        if dfs(word, j):
                            return True
                    return False

        return dfs(s, 1)

    def bfs(self, s, wordDict):
        # BFS
        queue = collections.deque()
        visited = set()
        queue.appendleft(0)
        visited.add(0)
        while len(queue) > 0:
            curr_index = queue.pop()
            for i in range(curr_index, len(s)+1):
                if i in visited:
                    continue
                if s[curr_index:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.add(i)
        return False

    # use dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if s[i - len(w) + 1:i + 1] == w and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
                    break
        return d[-1]