# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        helper = None
        while l1:
            succ = l1.next
            l1.next = helper
            helper = l1
            l1 = succ
        l1 = helper

        helper = None
        while l2:
            succ = l2.next
            l2.next = helper
            helper = l2
            l2 = succ
        l2 = helper

        s = 0
        before = ListNode(-1)
        while l1 and l2:
            r = l1.val + l2.val + s
            s = r // 10
            cur = ListNode(r % 10)
            cur.next = before.next
            before.next = cur
            l1 = l1.next
            l2 = l2.next
        l = l1 or l2
        while l:
            r = l.val + s
            s = r // 10
            cur = ListNode(r % 10)
            cur.next = before.next
            before.next = cur
            l = l.next
        if s:
            cur = ListNode(s)
            cur.next = before.next
            before.next = cur
        return before.next


'''Use stack instead of reversing list'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next

        s = 0
        before = ListNode(-1)
        while s1 and s2:
            l1, l2 = s1.pop(), s2.pop()
            r = l1.val + l2.val + s
            s = r // 10
            cur = ListNode(r % 10)
            cur.next = before.next
            before.next = cur
        s3 = s1 or s2
        while s3:
            l = s3.pop()
            r = l.val + s
            s = r // 10
            cur = ListNode(r % 10)
            cur.next = before.next
            before.next = cur
            l = l.next
        if s:
            cur = ListNode(s)
            cur.next = before.next
            before.next = cur
        return before.next