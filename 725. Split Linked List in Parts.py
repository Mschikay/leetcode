# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        s = root
        f = root
        cur = []
        n = k
        while f:
            cur.append(s)
            while f:
                t = k
                pre = s
                s = s.next
                while f and t:
                    f = f.next
                    t -= 1
            k -= 1
            pre.next = None
            f = s

        rest = n - len(cur)
        while rest:
            cur.append(ListNode(""))
            rest -= 1
        return cur


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        i = 0
        while node:
            i += 1
            node = node.next
        m = i % k
        n = i // k
        node = root
        res = [None] * k
        nums = [n + 1] * m + [n] * (k - m) # extra space to store numbers of each group

        if n:
            for j in range(k):
                num = nums[j]
                res[j] = node
                while num:
                    pre = node
                    node = node.next
                    num -= 1
                pre.next = None
        else:
            res = [None] * k
            for j in range(i):
                res[j] = node
                pre = node
                node = node.next
                pre.next = None
            for j in range(i, k):
                res[j] = ListNode("")
        return res
