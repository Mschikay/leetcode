# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        dummy = prev = ListNode(None)
        dummy.next = head
        i = 0
        while prev.next:
            i += 1
            if i == m:
                break
            prev = prev.next
        tail1 = prev
        tail2 = node = prev.next
        while i <= n:
            succ = node.next
            node.next = prev
            prev, node = node, succ
            i += 1
        tail1.next = prev
        tail2.next = node
        return dummy.next