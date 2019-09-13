# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in xrange(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []

        def dfs(vals):
            if len(vals) == 1: return [TreeNode(vals[0])]
            res = []
            for i in range(len(vals)):
                leftNode = dfs(vals[:i])
                rightNode = dfs(vals[i + 1:])
                for l in leftNode:
                    for r in rightNode:
                        node = TreeNode(vals[i])
                        node.left = l
                        node.right = r
                        res.append(node)
            return [None] if not res else res

        vals = [i for i in range(1, n + 1)]
        return dfs(vals)