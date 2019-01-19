import collections


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# My solution:
# class Solution:
#     # @param node, a undirected graph node
#     # @return a undirected graph node
#     def cloneGraph(self, node):
#         if not node:
#             return None
#
#         node_copy = UndirectedGraphNode(node.label)
#         vertex = {node.label: node_copy}
#         exist = {node.label: node}
#         graph = [node]
#
#         # add vertexes
#         for g in graph:
#             for n in g.neighbors:
#                 if n.label not in exist.keys():
#                     graph.append(n)
#                     vertex[n.label] = UndirectedGraphNode(n.label)
#                     exist[n.label] = n
#
#         # add edges
#         assert len(exist) == len(vertex)
#
#         for k, v in exist.items():
#             for n in exist[k].neighbors:
#                 vertex[k].neighbors.append(vertex[n.label])
#
#         return node_copy


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS
    def cloneGraph1(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:  # neighbor is not visited
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS iteratively
    def cloneGraph2(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS recursively
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                print('dic_before', len(dic))
                self.dfs(neighbor, dic)
                print('dic', len(dic))
            else:
                dic[node].neighbors.append(dic[neighbor])


if __name__ == "__main__":
    g0 = UndirectedGraphNode(0)
    g1 = UndirectedGraphNode(1)
    g2 = UndirectedGraphNode(2)

    g0.neighbors = [g1]
    g1.neighbors = [g0, g2]
    g2.neighbors = [g1, g2]

    s = Solution()
    # v = s.cloneGraph1(g0)
    v = s.cloneGraph(g0)
    graph = [v]
    for g in graph:
        print('vertex', g.label)
        for n in g.neighbors:
            print('neighbor', n.label)
            if n not in graph:
                graph.append(n)
