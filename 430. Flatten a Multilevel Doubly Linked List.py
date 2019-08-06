"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def search(curr):
            if not curr: return curr
            if curr.child:
                nextNode = curr.next
                nextNew = search(curr.child)
                curr.next = nextNew
                curr.child = None
                nextNew.prev = curr
                node = curr
                while node.next:
                    node = node.next
                nextNode = search(nextNode)
                if nextNode:
                    node.next = nextNode
                    nextNode.prev = node

            else:
                search(curr.next)
            return curr

        return search(head)


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if not head:
            return None

        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next