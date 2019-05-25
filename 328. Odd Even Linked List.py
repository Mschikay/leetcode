# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd1 = head
        laste = head and head.next
        odd2 = laste and laste.next

        while odd1 and laste and odd2:
            ne = odd2.next
            no = odd2.next and odd2.next.next

            e = odd1.next
            odd1.next = odd2
            odd2.next = e
            laste.next = ne

            odd1 = odd2
            odd2 = no
            laste = ne
        return head