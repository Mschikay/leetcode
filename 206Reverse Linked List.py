class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None

        helper = head
        curr = head.next
        head.next = None
        while curr:
            nextNode = curr.next
            curr.next = helper
            helper = curr
            curr = nextNode

        return helper

