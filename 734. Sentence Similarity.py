from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        m = defaultdict(set)
        for w1, w2 in pairs:
            m[w1].add(w2)
            m[w2].add(w1)
        if len(words1) != len(words2):
            return False
        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if w2 not in m[w1] and w1 not in m[w2]:
                return False
        return True