# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head: return head
        prev = ListNode(None)
        node = head
        while node:
            succ = node.next
            node.next = prev
            prev, node = node, succ
        head.next = None
        return prev

'''because we need the successor of current node, and head.next should be None, so we use dummy node, to make code clean'''