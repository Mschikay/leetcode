from collections import deque, defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ret = node

        q = deque()
        q.append(node)
        d = {}
        newNode = Node(node.val, [])
        d[node] = newNode
        while q:
            node = q.popleft()
            newNode = d[node]
            for n in node.neighbors:
                if n in d:
                    newNode.neighbors.append(d[n])
                else:
                    newNei = Node(n.val, [])
                    d[n] = newNei
                    newNode.neighbors.append(newNei)
                    q.append(n)

        return d[ret]


from collections import deque, defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}

        def dfs(node):
            newNode = Node(node.val, [])
            d[node] = newNode
            for n in node.neighbors:
                if n in d:
                    newNode.neighbors.append(d[n])
                else:
                    newNode.neighbors.append(dfs(n))
            return newNode

        dfs(node)
        return d[node]
