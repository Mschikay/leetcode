# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
#
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

from collections import defaultdict


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        l = len(words[0])
        trie = {}
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]

        def search(currDict, row, curr, ans):
            if len(curr) == l:
                ans.append(curr)
                return
            if len(row) == l:
                search(trie, "", curr + [row], ans)
            elif not row:
                pre = ""
                if curr:
                    for i in range(len(curr)):
                        pre += curr[i][len(curr)]
                for p in pre:
                    if p in currDict:
                        currDict = currDict[p]
                    else:
                        return
                for k in currDict:
                    search(currDict[k], pre + k, curr, ans)
            else:
                for k in currDict:
                    search(currDict[k], row + k, curr, ans)
            return

        ans = []
        search(trie, "", [], ans)
        return ans


from collections import defaultdict

'''since do this character by character, the maximum depth of recursion could be l(word)^2'''
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        l = len(words[0])
        trie = {}
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = defaultdict()
                d = d[c]

        def search(currDict, row, curr, ans):
            if len(curr) == l:
                ans.append(curr)
                return
            if len(row) == l:
                search(trie, "", curr + [row], ans)
            else:
                if len(row) >= len(curr):
                    for k in currDict:
                        search(currDict[k], row + k, curr, ans)
                else:
                    i = len(row)
                    key = curr[i][len(curr)]
                    if key in currDict:
                        search(currDict[key], row + key, curr, ans)
            return

        ans = []
        search(trie, "", [], ans)
        return ans



'''
        suppose the maximum branches is max(trie[prefix]), the length of the words, N
        and the maximum depth is the length of each word, l
        so time: N^l
'''

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        squares = []
        trie = {}
        for word in words:
            prefix = ""
            for i in range(len(word) - 1):
                prefix += word[i]
                if prefix in trie:
                    trie[prefix].append(word)
                else:
                    trie[prefix] = [word]
        size = len(words[0])

        def find_candidates(squares, square):
            size_of_square = len(square)
            if size_of_square == size:
                squares.append(square)
                return

            prefix = ''
            for word in square:
                prefix += word[size_of_square]
            if prefix not in trie:
                return

            for candidate in trie[prefix]:
                find_candidates(squares, square + [candidate])

        for word in words:
            square = [word]
            find_candidates(squares, square)

        return squares



