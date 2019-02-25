# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        try:
            fast = head.next.next
            slow = head.next

            while slow is not fast:
                fast = fast.next.next
                slow = slow.next

        except:
            return None

        while head is not slow:
            head = head.next
            slow = slow.next
        return head
