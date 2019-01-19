from collections import deque


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


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("flogs", "slaps", ["slogs","flops","flogs","slags","flaps","slops","flags","slaps"]))

