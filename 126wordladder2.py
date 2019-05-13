from collections import deque, defaultdict

class Solution(object):
    def findLadders1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # 先用BFS从终点出发，存储每个点到终点的最短路径
        # 然后用深搜找路径

        nei = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[0:i] + "_" + w[i + 1:]
                nei[key].append(w)

        N = len(wordList)
        wd = defaultdict(lambda: N)
        q = deque()
        q.append((endWord, 0))
        visited = set()
        visited.add(endWord)
        step = 0
        while q:
            w, step = q.popleft()
            wd[w] = step
            for i in range(len(w)):
                key = w[0:i] + "_" + w[i + 1:]
                for n in nei[key]:
                    if n not in visited:
                        visited.add(n)
                        q.append((n, step + 1))
        if beginWord not in wordList:
            wd[beginWord] = step + 1

        # print(wd)

        def dfs(cur, path, res):
            if cur == endWord:
                res.append(path)
                return
            else:
                step = wd[cur]
                for i in range(len(cur)):
                    key = cur[0:i] + "_" + cur[i + 1:]
                    for n in nei[key]:
                        if wd[n] == step - 1:
                            dfs(n, path + [n], res)
                return

        res = []
        dfs(beginWord, [beginWord], res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findLadders2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))