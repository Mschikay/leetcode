from collections import defaultdict


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False

        d = defaultdict(str)

        def find(w):
            if w not in d:
                d[w] = w
            if w != d[w]:
                d[w] = find(d[w])
            return d[w]

        for w1, w2 in pairs:
            d[find(w1)] = find(w2)

        # print(d)
        for w1, w2 in zip(words1, words2):
            if find(d[w1]) != find(d[w2]): return False
        return True
