# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if not head:
            return

        i = 1
        helper = head
        start = None
        end = None
        before = None
        while helper and i < m:
            i += 1
            before = helper
            helper = helper.next

        if helper:
            start = before
            end = helper

            before = helper
            curr = helper.next
            i += 1
            while curr and i <= n:
                i += 1
                nextNode = curr.next
                curr.next = before
                before = curr
                curr = nextNode
            if i <= n:
                return None

            end.next = curr
            if start:
                start.next = before
                return head

            return before
        return None

