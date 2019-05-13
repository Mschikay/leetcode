# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        def paths(node, s, nums):
            if not node.left and not node.right:
                nums.append(s)
            if node.right:
                paths(node.right, s * 10 + node.right.val, nums)
            if node.left:
                paths(node.left, s * 10 + node.left.val, nums)

        nums = []
        paths(root, root.val, nums)

        return sum(nums)

