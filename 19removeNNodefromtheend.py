class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext



class SinCycLinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)


s = SinCycLinkedlist()
node = s.head
for i in range(10):
    nextnode = Node(i+1)
    node.setNext(nextnode)
    node = node.next

#
# N = s.head
# while N.next:
#     print(N.next.getData())
#     N = N.next

def solve(n):
    fast = s.head
    slow = s.head
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    start = s.head
    while start.next:
        print(start.next.getData())
        start = start.next

if __name__ == "__main__":
    solve(2)