class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())

        ridx = inorder.index(root.val)
        root.right = self.buildTree(inorder[ridx + 1:], postorder)
        root.left = self.buildTree(inorder[:ridx], postorder)

        return root

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34807/Java-iterative-solution-with-explanation