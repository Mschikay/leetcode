# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        if not root.left and not root.right:
            return None
        self.maximum = 0
        def helper(node):
            if not node.left and not node.right:
                return node.val, node.val
            minl = maxl = minr = maxr = node.val
            if node.left:
                minl, maxl = helper(node.left)
            if node.right:
                minr, maxr = helper(node.right)
            self.maximum = max(self.maximum, abs(node.val - minl), abs(node.val - maxl), abs(node.val - minr), abs(node.val - maxr))
            return min(node.val, minl, minr), max(node.val, maxl, maxr)
        helper(root)
        return self.maximum