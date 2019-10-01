class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root: return []

        res = [root.val]

        def dfs(root, isleft, isright):
            if not root:
                return None
            if isleft or not root.left and not root.right:
                res.append(root.val)
            if root.left and root.right:
                dfs(root.left, isleft, False)
                dfs(root.right, False, isright)
            else:
                dfs(root.left, isleft, isright)
                dfs(root.right, isleft, isright)
            if (root.left or root.right) and isright:
                res.append(root.val)

        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res

