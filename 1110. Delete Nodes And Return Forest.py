# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)

        def search(node, ans):
            if not node: return None
            if node and node.val in delete:
                delNode(node, ans)
                return None

            node.left = search(node.left, ans)
            node.right = search(node.right, ans)
            return node

        def delNode(node, ans):
            if not node: return
            if node.val not in delete:
                ans.append(node)
                search(node, ans)
            else:
                delNode(node.left, ans)
                delNode(node.right, ans)

        ans = []
        delNode(root, ans)
        return ans

    def delNodes1(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []


        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root

        helper(root, True)
        return res