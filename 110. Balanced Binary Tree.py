# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recurse(node):
            if not node:
                return (0, True)
            lh, left = recurse(node.left)
            rh, right = recurse(node.right)
            h = max(rh, lh) + 1
            if not left or not right:
                return (h, False)
            if abs(rh - lh) > 1:
                return (h, False)
            return (h, True)

        return recurse(root)[1]

    