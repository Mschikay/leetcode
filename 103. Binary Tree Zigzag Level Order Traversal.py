# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        q = deque()
        q.append((root, 1))

        while q:
            node, lv = q.popleft()
            if len(res) < lv:
                res.append([node.val])
            else:
                res[-1].append(node.val)
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))

        for r in range(len(res)):
            if r % 2 == 1:
                res[r].reverse()
        return res