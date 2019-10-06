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


'''a better solution'''
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        s = set()
        for p in pairs:
            s.add((p[0], p[1]))
        if len(words1) != len(words2):
            return False
        for i in range(len(words1)):
            if words1[i] == words2[i] or (words1[i], words2[i]) in s or (words2[i], words1[i]) in s:
                continue
            else:
                return False
        return True