# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def divide(header):
            if not header or not header.next:
                return header

            pre, slow, fast = None, header, header
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None

            newHeader = divide(header)
            newSlow = divide(slow)

            return merge(newHeader, newSlow)

        def merge(l1, l2):
            dummy = cur = ListNode(0)

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2

            return dummy.next

        result = divide(head)
        return result


if __name__ == "__main__":
    n5 = ListNode(100)
    n4 = ListNode(3)
    n3 = ListNode(2)
    n2 = ListNode(1)
    n1 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    res = s.sortList(n1)

    print('result')
    node = res
    while node:
        print(node.val)
        node = node.next

