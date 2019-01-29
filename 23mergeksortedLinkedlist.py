# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class HeapNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right



class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        k = len(lists)

        while k:
            if not lists[k - 1]:
                del lists[k - 1]
            k -= 1
        print(lists)
        if not lists:
            return None

        def buildHeap():
            length = len(lists)

            start = (length + 1) // 2 - 1
            while start >= 0:
                print('start', start)
                adjust(start)
                start -= 1
                # for j in range(0, length):
                #     print(lists[j].val)
            return

        def adjust(i):
            length = len(lists)

            if not length or lists[i] is None:
                return

            # have 2 children
            if 2 * i + 2 < length:
                if lists[2 * i + 1].val <= lists[i].val and lists[2 * i + 1].val <= lists[2 * i + 2].val:
                    lists[2 * i + 1], lists[i] = lists[i], lists[2 * i + 1]
                    adjust(2 * i + 1)
                elif lists[2 * i + 2].val <= lists[i].val and lists[2 * i + 2].val <= lists[2 * i + 1].val:
                    lists[2 * i + 2], lists[i] = lists[i], lists[2 * i + 2]
                    adjust(2 * i + 2)
                return

            # have one child
            elif 2 * i + 1 < length:
                if lists[i].val > lists[2 * i + 1].val:
                    lists[i], lists[2 * i + 1] = lists[2 * i + 1], lists[i]
                    adjust(2 * i + 1)
                return

            else:
                return

        def getMin():
            minNode = lists[0]

            if lists[0].next:
                lists[0] = lists[0].next
            else:
                lists[0] = lists[-1]
                del lists[-1]

            adjust(0)

            return minNode

        helper = cur = ListNode(None)

        buildHeap()

        for i in lists:
            print('heap', i.val)

        while lists:
            cur.next = getMin()
            cur = cur.next
        return helper.next


    # 这个方法的时间复杂度是lgk+n^2
    # k为lists长度，n为链表长度
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def divide(nodelists):
            if not nodelists:
                return None
            length = len(nodelists)
            if length == 1:
                return nodelists[0]
            else:
                node1 = divide(nodelists[0:length // 2])
                node2 = divide(nodelists[length // 2:])
                return merge(node1, node2)

        def merge(n1, n2):
            dummy = cur = ListNode(None)

            while n1 and n2:
                if n1.val < n2.val:
                    cur.next, n1 = n1, n1.next
                else:
                    cur.next, n2 = n2, n2.next
                cur = cur.next

            cur.next = n1 or n2

            return dummy.next

        print(len(lists))
        return divide(lists)


if __name__ == "__main__":
    n1 = ListNode(-1)
    n2 = ListNode(1)
    n1.next = n2

    n4 = ListNode(-3)
    n5 = ListNode(1)
    n6 = ListNode(4)
    n4.next = n5
    n5.next = n6

    n7 = ListNode(-2)
    n8 = ListNode(-1)
    n9 = ListNode(0)
    n10 = ListNode(2)
    n7.next = n8
    n8.next = n9
    n9.next = n10


    s = Solution()
    res = s.mergeKLists([n1, n4, n7])
    # res = s.mergeKLists([[]])

    while res:
        print(res.val)
        res = res.next