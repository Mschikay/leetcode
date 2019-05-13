from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        last = None
        node = root
        s = []

        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if last and last.val >= node.val:
                    return False
                last = node
                node = node.right

        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # Morris way
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        while root:
            if root.left:
                cur = root.left
                while cur.right:
                    cur = cur.right
                cur.right = root
                temp = root.left
                root.left = None
                root = temp
            else:
                if res and res[-1] >= root.val:
                    return False
                res.append(root.val)
                root = root.right
        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recursive(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return recursive(node.left, low, node.val) and recursive(node.right, node.val, high)

        return recursive(root, float("-inf"), float("inf"))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # iterative dfs
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if not low < node.val < high:
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))

        return True


class Solution(object):         # iterative bfs
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append((root, float("-inf"), float("inf")))
        while q:
            node, low, high = q.popleft()
            if not node:
                continue
            if not low < node.val < high:
                return False
            q.append((node.left, low, node.val))
            q.append((node.right, node.val, high))

        return True


# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print "Vertex tDistance from Source"
		for node in range(self.V):
			print node, "t", dist[node]

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initilaize minimum distance for next node
		min = sys.maxint

		# Search not nearest vertex not in the
		# shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Funtion that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxint] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shotest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shotest path tree
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and \
				dist[v] > dist[u] + self.graph[u][v]:
						dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)
