# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k: return head

        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        k = k % l
        if not k: return head

        pre = None
        node = head
        i = 0
        while i < k and node:
            pre = node
            node = node.next
            i += 1
        start = head
        while node.next:
            start = start.next
            node = node.next
        ret = start.next
        node.next = head
        start.next = None
        return ret


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head

        fast = head
        while k > 0:
            fast = fast.next
            k -= 1

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        fast.next = head
        head = temp

        return head
