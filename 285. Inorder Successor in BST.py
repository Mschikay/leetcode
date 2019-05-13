# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        s = []
        found = False
        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                node = s.pop()
                if found:
                    return node
                root = node.right
                if node == p:
                    found = True

        return None
