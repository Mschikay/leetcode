# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # ret = dummy = ListNode(-1)
        # dummy.next = head
        # succ = head and head.next
        # while dummy.next and succ:
        #     if dummy.next.val == succ.val:
        #         newsucc = succ.next
        #         dummy.next = succ
        #         succ = newsucc
        #     else:
        #         dummy = dummy.next
        #         succ = succ.next
        # return ret.next
        dummy = succ = head
        while dummy and succ:
            while succ and dummy.val == succ.val:
                succ = succ.next
            dummy.next = succ
            dummy = dummy.next
        return head
