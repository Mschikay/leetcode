# 8.07% ???????????
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next and fast.next.next

        # reverse the second half
        helper = None
        preSlow = None
        while slow:
            pro = slow.next
            slow.next = helper
            helper = slow
            slow = pro

        start = head
        while helper and start:
            if helper.val != start.val:
                return False
            start = start.next
            helper = helper.next
        return True

    # more spaces
    def isPalindrome(self, head):
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

    # use stack
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

def isPalindrome(self, head: ListNode) -> bool:
    s = []
    fast = head
    slow = head
    while fast:
        s.append(slow.val)
        slow = slow.next
        if not fast.next:  # need to judge odd or even
            s.pop()
        fast = fast.next and fast.next.next

    while s:
        if s.pop() != slow.val:
            return False
        slow = slow.next
    return True