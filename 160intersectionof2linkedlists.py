#
# class Node:
#     def __init__(self, name, beforeset, afterset):
#         self.name = name
#         self.beforeset = beforeset
#         self.afterset = afterset
#
#     def before(self, a):
#         self.beforeset.append(a)
#         return
#
#     def after(self, b):
#         self.afterset.append(b)
#         return
#
#
# a1 = Node('a1', [], [])
# a2 = Node('a2', [], [])
# c1 = Node('c1', [], [])
# c2 = Node('c2', [], [])
# c3 = Node('c3', [], [])
# b1 = Node('b1', [], [])
# b2 = Node('b2', [], [])
# b3 = Node('b3', [], [])
#
# a1.after(a2)
# a2.before(a1)
# a1.after(c1)
# c1.before(a1)
# c1.after(c2)
# c2.before(c1)
# c2.after(c3)
# c3.before(c2)
# b1.after(b2)
# b2.before(b1)
# b2.after(c2)
# c2.before(b2)
# b2.after(b3)
# b3.before(b2)
#
# res = 'null'
#
#
# def solve(x):
#     global res
#     while True:
#         if len(x.beforeset) == 2:
#             res = x.name
#             break
#         if len(x.afterset) == 0:
#             break
#         if len(x.afterset) == 2:
#             x = x.afterset[1]
#         else:
#             x = x.afterset[0]
#
#     print(res)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        trav_a, trav_b = headA, headB
        while trav_a is not trav_b:
            trav_a = headB if not trav_a else trav_a = trav_a.next
            trav_b = headA if not trav_b else trav_b = trav_b.next
        return trav_a
'''
FOR OTHER SOLUTION REFER TO
https://blog.csdn.net/fengxinlinux/article/details/78885764  
'''

if __name__ == "__main__":
    solve(a1)



