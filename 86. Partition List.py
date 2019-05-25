# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        bh = before = ListNode(-1)
        ah = after = ListNode(-1)

        while head:
            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next
            head = head.next
        after.next = None
        before.next = ah.next
        return bh.next