# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        ridx = inorder.index(root.val)

        preorder.remove(root.val)
        root.left = self.buildTree(preorder, inorder[:ridx])
        root.right = self.buildTree(preorder, inorder[ridx + 1:])

        return root