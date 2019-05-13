from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord or not endWord or beginWord == endWord:
            return 0

        d = {}
        for word in wordList:
            for i in range(len(word)):
                template = word[0:i]+'/'+word[i+1:]
                d.setdefault(template, [])
                d[template].append(word)

        queue = deque((beginWord, 1))
        exist = set()
        while queue:
            w, step = queue.popleft()
            for j in range(len(w)):
                k = w[0:j]+'/'+w[j+1:]
                print(k)
                neighbors = d.get(k, [])
                for neighbor in neighbors:
                    if neighbor not in exist:
                        if neighbor == endWord:
                            return step + 1
                        exist.add(neighbor)
                        queue.append((neighbor, step + 1))
        return 0

    # And a method that saves space:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


# my solution with two ends:

from collections import defaultdict, deque


class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[0:i] + "_" + w[i + 1:]
                nei[key].append(w)

        def visitNext(queue, visit1, visit2):
            w, step = queue.popleft()
            for i in range(len(w)):
                key = w[0:i] + "_" + w[i + 1:]
                for n in nei[key]:
                    if n in visit2.keys():
                        return step + visit2[n]
                    else:
                        if n not in visit1.keys():
                            visit1[n] = step + 1
                            queue.append((n, step + 1))
            return None

        qBegin = deque()
        qBegin.append((beginWord, 1))
        qEnd = deque()
        qEnd.append((endWord, 1))
        vBegin = defaultdict(int)
        vBegin[beginWord] = 1
        vEnd = defaultdict(int)
        vEnd[endWord] = 1

        while qBegin and qEnd:
            ans = visitNext(qBegin, vBegin, vEnd)
            if ans:
                return ans
            ans = visitNext(qEnd, vEnd, vBegin)
            if ans:
                return ans

        return 0





if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("flogs", "slaps", ["slogs","flops","flogs","slags","flaps","slops","flags","slaps"]))

