'''use trie'''
from collections import defaultdict


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        trie = defaultdict()
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]
            d["end"] = 1

        def dfs(i, word, wordDict, num):
            if i == len(word):
                if "end" in wordDict and num >= 1:
                    return True
                return False
            if "end" in wordDict:
                if dfs(i, word, trie, num + 1): return True
            if word[i] in wordDict:
                if dfs(i + 1, word, wordDict[word[i]], num): return True
            return False

        ans = []
        for w in words:
            if dfs(0, w, trie, 0): ans.append(w)

        return ans


'''use set'''
from collections import defaultdict

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def dfs(word, s):
            for i in range(1, len(word)):
                pre, sur = word[:i], word[i:]
                if pre in s and sur in s:
                    return True
                elif pre in s:
                    if dfs(sur, s): return True
                elif sur in s:
                    if dfs(pre, s): return True
            return False

        ans = []
        s = set(words)
        for w in words:
            if dfs(w, s): ans.append(w)

        return ans


'''much faster'''
from collections import defaultdict

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words,key=lambda t:len(t))
        word_dict = set()
        def isQualify(w):
            if w in word_dict:return True
            for i in range(1,len(w)):
                if w[:i] in word_dict and isQualify(w[i:]):return True
            return False
        res = []
        for w in words:
            if isQualify(w):res.append(w)
            word_dict.add(w)
        return res