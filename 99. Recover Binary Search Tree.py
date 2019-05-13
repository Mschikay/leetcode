# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None
        self.num = 0

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if self.pre and self.pre.val > node.val:
                self.num += 1
                if not self.first:
                    self.first = self.pre
                self.second = node
                if self.num == 2:
                    return
            self.pre = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
