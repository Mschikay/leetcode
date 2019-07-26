'''nlogn'''
class Solution:
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)
        items = list(counts.items())
        items.sort(key=lambda item:(-item[1],item[0]))
        return [item[0] for item in items[0:k]]


'''nlogk build a heap with max size k  '''

from collections import Counter, defaultdict
from heapq import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dword = Counter(words)
        dNum = defaultdict(list)
        for ky, v in dword.items():
            dNum[v].append(ky)
        wordsNum = list(dNum.keys())

        def split(l, h):
            if l == h: return l
            b, v = h, wordsNum[h]
            while l < h:
                while l < h and wordsNum[l] > v:
                    l += 1
                wordsNum[b], b = wordsNum[l], l
                while l < h and wordsNum[h] <= v:
                    h -= 1
                wordsNum[b], b = wordsNum[h], h
            wordsNum[b] = v
            return l

        l, h = 0, len(wordsNum) - 1
        while l <= h:
            m = split(l, h)
            num = sum([len(dNum[i]) for i in wordsNum[:m + 1]])
            if num <= k:
                l = m + 1
            else:
                h = m - 1

        h = []
        heapify(h)
        for i in wordsNum[:l + 1]:
            heappush(h, (-i, sorted(dNum[i])))
        ans = []
        while h:
            ans += heappop(h)[1]

        return ans[:k]


import collections
import heapq


class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            if len(heap) < k:
                heapq.heappush(heap, Word(value, key))
            else:
                heapq.heappushpop(heap, Word(value, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]


class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other): # less than
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word