# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 1
        node = head
        while i <= n and node.next:
            node = node.next
            i += 1
        if i <= n: return head.next
        start = head
        while node.next:
            start = start.next
            node = node.next
        start.next = start.next.next
        return head