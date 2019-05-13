# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        ql = deque()
        qr = deque()
        ql.append(root)
        qr.append(root)

        while ql and qr:
            l = ql.pop()
            r = qr.pop()

            if not l and not r or l and r and l.val == r.val:
                print(l and l.val)
                pass
            else:
                return False
            if l:
                ql.append(l.left)
                ql.append(l.right)
            if r:
                qr.append(r.right)
                qr.append(r.left)
        return True

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSymmetric(self, root):        #recursive

        """
        :type root: TreeNode
        :rtype: bool
        """

        def mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            return node1.val == node2.val and mirror(node1.left, node2.right) and mirror(node1.right, node2.left)

        return mirror(root, root)

