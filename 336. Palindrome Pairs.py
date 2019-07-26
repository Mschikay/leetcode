class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(curr_str):
            return curr_str == curr_str[::-1]
        word_dict = {word: idx for idx,word in enumerate(words)}
        ans = []
        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                pref = word[:i]
                suff = word[i:]
                if is_palindrome(pref):
                    half = suff[::-1]
                    if half != word and half in word_dict:
                        ans.append((word_dict[half], idx))
                if i != len(word) and is_palindrome(suff):
                    half = pref[::-1]
                    if half !=word and half in word_dict:
                        ans.append((idx, word_dict[half]))
        return ans


from collections import defaultdict

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        d = {w: i for i, w in enumerate(words)}

        for w in words:
            for i in range(len(w) + 1):
                pre = w[:i]
                suf = w[i:]
                rpre = pre[::-1]
                rsuf = suf[::-1]
                if w != rsuf and pre == rpre and rsuf in d.keys():
                    res.append([d[rsuf], d[w]])

                if w != rpre and suf == rsuf and rpre in d.keys():
                    res.append([d[w], d[rpre]])
        return res
