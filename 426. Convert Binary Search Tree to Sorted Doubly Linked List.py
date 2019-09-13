"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        first = None
        last = None
        s = []

        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                node = s.pop()

                if not first:
                    first = node

                if last:
                    last.right = node
                    node.left = last

                last = node
                root = node.right

        if last and first:
            last.right = first
            first.left = last

        return first


