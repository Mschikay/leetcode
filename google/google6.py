# 给两个String, 一个是26个字母，一个是任意1-100,000长度的string, 求在s2上总共走过的距离。 例如
#      s1 = abcdefghijklmnopqrstuvwxyz
#      s2 = cba-baidu 1point3acres
# c: [0 - 2]  = 2
# b: [2 - 1] = 1
# a: [1 - 0] = 1
#
# 最终return 2 + 1 + 1 = 4

class Solution:
    def passtime(self, keyboard, word):
        keydict = {}
        for i, k in enumerate(keyboard):
            keydict[k] = i

        step = keydict.get(word[0])
        if len(word) == 1:
            return step

        i = 1
        l = r = 0
        step = keydict[word[0]]

        while i < len(word):
            while i < len(word) and keydict[word[i]] <= keydict[word[i-1]]:
                print(i, l)
                l = i
                i += 1
                continue
            step += keydict[word[r]] - keydict[word[l]]
            r = l

            while i < len(word) and keydict[word[i]] > keydict[word[i-1]]:
                print(i, r)
                r = i
                i += 1
                continue

            step += keydict[word[r]] - keydict[word[l]]

        return step


if __name__ == "__main__":
    s = Solution()
    print(s.passtime("adefghijklmnopqrsyztuvwxbc", "abccc"))