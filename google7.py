# 水滴到根，多孩子树，每个孩子有个int，表示多长时间到这个孩子，问多久能到所有孩子， 迭代很容易

from heapq import *

class Graph:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children

    def __lt__(self, other):
        return self.val < other.val

class Solution:

    def time(self, root, child):

        i = 0
        queue = []
        heappush(queue, (0, root))
        visited = set()
        visited.add(root)
        timeConsumed = timeTotal = timeChild = 0

        while i < len(queue):
            timeConsumed, node = heappop(queue)
            if node == child:
                timeChild = timeConsumed

            for c in node.children:
                if c in visited:
                    continue
                else:
                    visited.add(c)
                    heappush(queue, (timeConsumed+node.val, c))

        timeTotal = timeConsumed

        return timeChild, timeTotal


if __name__ == "__main__":
    g1 = Graph(1)
    g2 = Graph(3)
    g3 = Graph(4)
    g4 = Graph(2)
    g5 = Graph(2)
    g6 = Graph(8)
    g7 = Graph(9)
    g8 = Graph(4)
    g9 = Graph(1)

    g1.children = [g2, g3, g4]
    g2.children = [g5, g6]
    g5.children = [g6, g7, g8]
    g7.children = [g6, g8]
    g8.children = [g9]

    s = Solution()
    print(s.time(g1, g6))