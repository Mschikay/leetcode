# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这个好像比较快 没有数组之类的操作
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        def dfs(subSum, node):
            if subSum + node.val == sum:
                if not node.left and not node.right:
                    return True

            left = right = False
            if node.left:
                left = dfs(subSum + node.val, node.left)

            if node.right:
                right = dfs(subSum + node.val, node.right)

            return left or right

        return dfs(0, root)

# 自底向上
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        def dfs(node):
            res = []
            if not node.left and not node.right:
                return [node.val]
            else:
                if node.left:
                    for d in dfs(node.left):
                        res.append(d + node.val)
                if node.right:
                    for d in dfs(node.right):
                        res.append(d + node.val)
            return res

        res = dfs(root)
        return sum in res