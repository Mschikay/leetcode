# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        d = defaultdict(lambda: 0)
        f = defaultdict(list)

        def recursive(node):
            if not node:
                return 0
            s = node.val + recursive(node.left) + recursive(node.right)
            d[s] = d[s] + 1
            f[d[s]].append(s)
            return s

        recursive(root)
        return f[max(f.keys())]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        d = defaultdict(lambda: 0)
        f = defaultdict(list)

        def recursive(node):
            if not node:
                return 0, float("-inf")
            lsum, lmax = recursive(node.left)
            rsum, rmax = recursive(node.right)
            s = node.val + lsum + rsum
            d[s] = d[s] + 1
            f[d[s]].append(s)
            maxf = max(lmax, rmax, d[s])
            return s, maxf

        return f[recursive(root)[1]]
