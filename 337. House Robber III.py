class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(dfs(root))