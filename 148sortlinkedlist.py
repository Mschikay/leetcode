class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def divide(node):
            if not node or not node.next: return node
            ret = slow = fast = ListNode(-1)
            slow.next = node
            pre = None
            while fast:
                pre = slow
                slow = slow.next
                fast = fast.next and fast.next.next
            pre.next = None

            return merge(divide(ret.next), divide(slow))

        def merge(node1, node2):
            ret = node = ListNode(-1)
            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
                else:
                    node.next = node2
                    node = node.next
                    node2 = node2.next
            node.next = node1 or node2
            return ret.next

        return divide(head)

