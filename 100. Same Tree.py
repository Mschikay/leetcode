# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pq = deque()
        qq = deque()
        pq.append(p)
        qq.append(q)

        while pq and qq:
            x, y = pq.popleft(), qq.popleft()
            if not (x == y == None or x and y and x.val == y.val):
                return False
            if x:
                pq.append(x.left)
                pq.append(x.right)
            if y:
                qq.append(y.left)
                qq.append(y.right)
        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q == None:
            return True
        if not (p and q and p.val == q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
