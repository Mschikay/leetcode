"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# an iterative method
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = root
        while root and root.left:
            n = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = n
        return res

# recursive