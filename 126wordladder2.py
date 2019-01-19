from collections import deque
import copy


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
        d = {}
        newList = copy.deepcopy(wordList)
        if not beginWord or not endWord:
            return []
        if beginWord not in wordList:
            newList = wordList + [beginWord]
        for word in newList:
            for i in range(len(word)):
                template = word[0:i]+'/'+word[i+1:]
                d.setdefault(template, [])
                d[template].append(word)

        hash = set()
        hash.add(endWord)
        wordDistance = {endWord: 1}
        queue = deque()
        queue.append(endWord)

        # BFS
        while queue:
            word = queue.popleft()
            step = wordDistance.get(word)

            for i in range(len(word)):
                key = word[0:i] + '/' + word[i+1:]
                neighbors = d.get(key, [])
                for neighbor in neighbors:
                    if neighbor not in hash:
                        hash.add(neighbor)
                        queue.append(neighbor)
                        wordDistance[neighbor] = step + 1
        # DFS
        results = []

        def paths(word, path):
            step = wordDistance.get(word)
            path.append(word)

            if word == endWord:
                results.append(path)
                return

            for i in range(len(word)):
                key = word[0:i] + '/' + word[i + 1:]
                neighbors = d.get(key, [])
                if not neighbors:
                    continue
                for neighbor in neighbors:
                    if wordDistance.get(neighbor) and wordDistance.get(neighbor) == step - 1:
                        # newPath = copy.deepcopy(path)
                        paths(neighbor, path)

        # get results
        paths(beginWord, [])

        return results

    def findLadders2(self, beginWord, endWord, wordList):
        # or
        # from begin to end: BFS (为了记下最短路径是多少)
        # from end to begin: DFS（通过最短路径搜寻即可，搜到的点要往前插入数组）

        d = {}
        newList = copy.deepcopy(wordList)
        if not beginWord or not endWord:
            return []
        if beginWord not in wordList:
            newList = wordList + [beginWord]
        for word in newList:
            for i in range(len(word)):
                template = word[0:i] + '/' + word[i + 1:]
                d.setdefault(template, [])
                d[template].append(word)

        # print(d)

        paths = []

        def dfs(path, word, hash):
            path.append(word)
            # print(path, word)
            if word == endWord:
                paths.append(path)
                return

            for i in range(len(word)):
                key = word[0:i] + '/' + word[i+1:]
                neighbors = d.get(key, [])
                for neighbor in neighbors:
                    if neighbor not in hash:
                        newHash = copy.deepcopy(hash)
                        newHash.add(neighbor)
                        newPath = copy.deepcopy(path)
                        dfs(newPath, neighbor, newHash)
            return

        exist = set()
        exist.add(beginWord)
        dfs([], beginWord, exist)
        # print(paths)
        if not paths:
            return []
        newPath = []
        minLen = len(min(paths, key=len))
        for p in paths:
            if len(p) == minLen:
                newPath.append(p)
        return newPath


if __name__ == "__main__":
    s = Solution()
    print(s.findLadders2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))