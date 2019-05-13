"""
# Definition for a Node.
"""

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
from collections import defaultdict


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d = defaultdict(Node)
        helper = start = head and Node(head.val, None, head.random)
        while start:
            d[head] = start
            start.next = head.next and Node(head.next.val, None, head.next.random)
            start = start.next
            head = head.next

        start = helper
        while start:
            start.random = start.random and d[start.random]
            start = start.next
        return helper


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
from collections import defaultdict


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d = defaultdict(Node)
        s = s1 = s2 = head
        while s1:
            d[s1] = Node(s1.val, None, None)
            s1 = s1.next

        while s2:
            d[s2].next = s2.next and d[s2.next]
            d[s2].random = s2.random and d[s2.random]
            s2 = s2.next

        return head and d[head]