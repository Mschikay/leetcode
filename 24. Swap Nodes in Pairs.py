# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = dummy = ListNode(-1)
        dummy.next = head
        while dummy and dummy.next and head and head.next:
            succ = head.next.next
            dsucc = dummy.next
            head.next.next = dummy.next
            dummy.next = head.next
            dsucc.next = succ

            dummy = dummy.next.next
            head = succ
        return ret.next