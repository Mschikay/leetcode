# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return (0, float("-inf"))
            lsum, lmax = dfs(node.left)
            rsum, rmax = dfs(node.right)
            pmax = max(node.val, node.val + lsum, node.val + rsum)
            rmax = max(pmax, lmax, rmax, node.val + lsum + rsum)
            return (pmax, rmax)

        return dfs(root)[1]