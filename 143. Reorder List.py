# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: return head

        node1 = node2 = head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next

        node2 = node1.next
        node1.next = None

        helper = None
        while node2:
            newNode2 = node2.next
            node2.next = helper
            helper = node2
            node2 = newNode2

        node = head
        while node and helper:
            newNode = node.next
            newHelper = helper.next
            node.next = helper
            helper.next = newNode
            node, helper = newNode, newHelper
        return head


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
