# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        res = []
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                cur = s.pop()
                res.append(cur.val)
                node = cur.right

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        node = root
        while node:
            if node.left:
                cur = node.left
                while cur.right:
                    cur = cur.right
                cur.right = node
                temp = node
                node = node.left
                temp.left = None # avoid loop
            else:
                # print(node.val)
                res.append(node.val)
                node = node.right
        return res


