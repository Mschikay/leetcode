# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.red = None

        def traverse(node):
            if not node: return
            if node.val == x:
                self.red = node
                return
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            return 1 + l + r

        if not self.red: return None
        l, r = helper(self.red.left), helper(self.red.right)
        p = n - l - r - 1
        half = n // 2
        if p > half or l > half or r > half: return True
        return False