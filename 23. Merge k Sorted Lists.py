'''all 3 methods take O(nlogk) time'''
from heapq import *


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        return self.sort2by2(lists)

    def heap(self, lists):
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        h = []
        heapify(h)
        for i in range(len(lists)):
            if lists[i]:
                heappush(h, (lists[i].val, lists[i]))
        dummy = point = ListNode(None)
        while h:
            val, node = heappop(h)
            point.next = node
            if node.next:
                heappush(h, (node.next.val, node.next))
            point = point.next
        return dummy.next

    def sort2by2(self, lists):
        l = len(lists)
        interval = 1
        while interval < l:
            for i in range(0, l - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def divideConquer(lists):
        if not lists: return None
        start, end = 0, len(lists) - 1
        return self.split(lists, start, end)

    def split(self, lists, start, end):
        if start == end: return lists[start]
        mid = (start + end) // 2
        l1 = self.split(lists, start, mid)
        l2 = self.split(lists, mid + 1, end)
        return self.merge2Lists(l1, l2)

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next