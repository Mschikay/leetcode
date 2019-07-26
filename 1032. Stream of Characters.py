from collections import defaultdict, deque


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = defaultdict()
        wordlen = 0
        for word in words:
            wordlen = max(wordlen, len(word))
            d = self.trie
            for c in reversed(word):
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]
            d["end"] = 1

        self.maxlen = wordlen
        self.pool = deque()
        self.poollen = -1

    def query(self, letter: str) -> bool:
        self.pool.append(letter)
        if self.poollen == self.maxlen:
            self.pool.popleft()
        else:
            self.poollen += 1

        def dfs(i, word, wordDict):
            if i < 0 and "end" not in wordDict: return False
            if "end" in wordDict:
                return True
            else:
                if word[i] in wordDict:
                    return dfs(i - 1, word, wordDict[word[i]])
                return False

        return dfs(self.poollen, self.pool, self.trie)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)