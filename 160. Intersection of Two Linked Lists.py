
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        a = b = 1
        na, nb = headA, headB
        p = None
        while na.next:
            a += 1
            na = na.next
        while nb.next:
            b += 1
            nb = nb.next
        if na != nb: return None
        t = abs(b - a)
        if b > a:
            while t:
                headB = headB.next
                t -= 1
        else:
            while t:
                headA = headA.next
                t -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA



'''use hashmap'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        while headA and headB:
            if headA in s: return headA
            s.add(headA)
            headA = headA.next
            if headB in s: return headB
            s.add(headB)
            headB = headB.next
        h = headA or headB
        while h:
            if h in s: return h
            s.add(h)
            h = h.next

        return None