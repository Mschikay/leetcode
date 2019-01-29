# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next

    # recursive is slower
    def recursive(self, l1, l2):
        if l1 and l2:
            if l1.val <= l2.val:
                l1.next = self.recursive(l1.next, l2)
                return l1
            else:
                l2.next = self.recursive(l1, l2.next)
                return l2
        else:
            return l1 or l2


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n4 = ListNode(2)
    n5 = ListNode(6)
    n6 = ListNode(11)
    n4.next = n5
    n5.next = n6

    s = Solution()
    res = s.recursive(n1, n4)

    while res:
        print(res.val)
        res = res.next
