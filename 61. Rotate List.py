# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head

        i = 0
        dummy = node = ListNode(None)
        node.next = head
        while node.next:
            if i == k: break
            i += 1
            node = node.next

        if not node.next:
            k = k % i
            node = dummy
            i = 0
            while node.next:
                if i == k: break
                i += 1
                node = node.next

        node1 = dummy
        while node.next:
            node1 = node1.next
            node = node.next

        node.next = dummy.next
        ret = node1.next
        node1.next = None
        return ret

