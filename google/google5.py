# 拼写检查


class Solution:
    def check(self, document, dictionary):
        trie = {}
        for word in dictionary:
            wordDict = trie
            for w in word:
                curr = wordDict.setdefault(w, {})
                wordDict = curr

        res = []
        for dd in document:
            wordDict = trie
            for d in dd:
                curr = wordDict.get(d, None)
                if curr is None:
                    res.append(dd)
                    break
                wordDict = curr
        return res

    def checkHash(self, document, dictionary):
        wordDict = {}
        for d in dictionary:
            wordDict.setdefault(d, True)

        res = []
        for d in document:
            if wordDict.get(d, False):
                pass
            else:
                res.append(d)
        return res


if __name__ == "__main__":
    s = Solution()
    document = ["abc", "ac", "bcd"]
    dictionary = ["eab", "eaa", "daf", "dfa"]
    print(s.checkHash(document, dictionary))