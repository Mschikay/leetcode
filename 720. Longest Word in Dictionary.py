from collections import defaultdict


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        d = defaultdict()
        ans = ""
        for w in words:
            dd = d
            l = 0
            for i in range(len(w)):
                c = w[i]
                if c not in dd.keys():
                    if i == len(w) - 1:
                        dd[c] = defaultdict()
                        if len(w) > len(ans):
                            ans = w
                    else:
                        break
                dd = dd[c]
        return ans


class Solution:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        ans = set([''])
        longest = ''

        for word in words:
            if word[:-1] in ans:
                ans.add(word)
                if len(word) > len(longest):
                    longest = word

        return longest