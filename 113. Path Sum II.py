# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []

        def findPath(node, path, res):
            if not node.left and not node.right:
                if sum(path) + node.val == s: res.append(path + [node.val])
            if node.left:
                findPath(node.left, path + [node.val], res)
            if node.right:
                findPath(node.right, path + [node.val], res)
            return

        res = []
        findPath(root, [], res)
        return res