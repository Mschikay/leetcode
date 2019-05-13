# 类似word ladder，对于一个单词删掉任何一个字母，如果新单词出现在给的词典里
# 那么就形成一个 chain： old word -> new word -> newer word,
# 求最长长度(return int) 比如给vector<string> w = {a,ba,bca,bda,bdca} 最长是4： bdca->bda->ba->a;. 1point3acres

class Solution:
    def longestChain(self, word, dictionary):

        def dfs(w):
            if w not in dictionary:
                return 0
            else:
                if len(w) == 1:
                    return 1
                res = 1
                maxR = 0
                for i in range(len(w)):
                    if i > 0 and w[i] == w[i - 1]:
                        continue
                    newWord = w[0:i] + w[i + 1:]
                    r = dfs(newWord)
                    if r > maxR:
                        maxR = r
                return res + maxR

        if word not in dictionary:
            return 0
        else:
            return dfs(word)


if __name__ == "__main__":
    s = Solution()
    word = 'bdca'
    dictionary = {"d", "ca", "acd", "bca", "bdca"}

    print(s.longestChain(word, dictionary))
