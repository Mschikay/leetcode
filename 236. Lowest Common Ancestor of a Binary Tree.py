# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def find(node, p, q):
            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left = find(node.left, p, q)
            right = find(node.right, p, q)
            if left and right:
                return node
            if left or right:
                return left or right
            return None

        return find(root, p, q)