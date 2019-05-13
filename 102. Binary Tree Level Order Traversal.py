# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        curlv = 0
        q = deque()
        q.append((root, 0))

        while q:
            node, lv = q.popleft()
            if not node:
                continue
            if curlv != lv:
                res.append(cur)
                cur = []
                curlv = lv
            cur.append(node.val)
            q.append((node.left, lv + 1))
            q.append((node.right, lv + 1))
        if cur != []: res.append(cur)

        return res