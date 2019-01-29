# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head.next
        helper = ListNode(None)
        while curr:
            newCurr = curr.next

            node = helper
            while node:
                if node.next and curr.val > node.next.val:
                    node = node.next
                else:
                    post = node.next
                    node.next = curr
                    curr.next = post
                    break

            curr = newCurr

        return helper.next


if __name__ == "__main__":
    n5 = ListNode(100)
    n4 = ListNode(3)
    n3 = ListNode(2)
    n2 = ListNode(1)
    n1 = ListNode(4)
    head = ListNode(None)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    res = s.insertionSortList(head)

    node = res
    while node:
        print(node.val)
        node = node.next



