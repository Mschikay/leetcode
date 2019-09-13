# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next and fast.next.next

        prev, node = slow, slow.next
        slow.next = None
        last = node
        while node:
            succ = node.next
            node.next = prev
            prev, node = node, succ
        last = None

        node1 = dummy.next
        node2 = prev

        while node1 and node2:
            succ1, succ2 = node1.next, node2.next
            node1.next = node2
            node2.next = succ1
            node1, node2 = succ1, succ2
        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        d = defaultdict(ListNode)
        i = 0
        node = head
        while node:
            d[i] = node
            node = node.next
            i += 1

        l, r = 0, i - 1
        end = ListNode(0)
        while l < r:
            end.next = d[l]
            d[l].next = d[r]
            d[r].next = None
            end = d[r]
            l += 1
            r -= 1
        if l == r:
            end.next = d[l]
            d[l].next = None
        return head


from collections import defaultdict


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        d = defaultdict(ListNode)
        i = 0
        node = head
        while node:
            d[i] = node
            node = node.next
            i += 1

        l, r = 0, i - 1
        end = ListNode(0)
        while l < r:
            end.next = d[l]
            d[l].next = d[r]
            end = d[r]
            l += 1
            r -= 1
        end.next = None
        if l == r:
            end.next = d[l]
            d[l].next = None
        return head
