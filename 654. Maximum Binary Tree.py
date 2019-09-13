# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        st = []
        for n in nums:
            node = TreeNode(n)
            pre = None
            while st and st[-1].val < n:
                pre = st.pop()
            node.left = pre
            if st:
                st[-1].right = node
            st.append(node)
        return st[0]