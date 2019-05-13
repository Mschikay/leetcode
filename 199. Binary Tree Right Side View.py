# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        start = end = 0
        i = 0
        while i < len(q):
            node = q[i]
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == end:
                    for j in range(end, start - 1, -1):
                        if q[j]:
                            res.append(q[j].val)
                            break
                    start = i + 1
                    end = len(q) - 1

            i += 1
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        d = defaultdict(list)
        q = [(root, 0)]
        d[0] = [root.val]
        i = 0
        while i < len(q):
            node, depth = q[i][0], q[i][1]
            if node:
                if node.left:
                    q.append((node.left, depth + 1))
                    d[depth + 1].append(node.left.val)
                if node.right:
                    q.append((node.right, depth + 1))
                    d[depth + 1].append(node.right.val)
            i += 1
        k = list(d.keys())
        k.sort()
        for kk in k:
            res.append(d[kk][-1])
        return res




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  40 ms, faster than 94.83% of Python3 online submissions for Binary Tree Right Side View. 用二分方法
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]
