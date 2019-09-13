'''singly linkedlist'''
from collections import defaultdict


class Node:
    def __init__(self, key, val, n=None):
        self.key = key
        self.val = val
        self.next = n


class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.dummy = Node(None, None)
        self.keys[self.dummy.key] = self.dummy
        self.capacity = capacity

    def update(self, key):
        pre = self.keys[key]
        curr = pre.next
        if not curr.next: return # 注意只有一个节点
        pre.next = curr.next
        last = self.keys[self.dummy.key]
        last.next = curr
        curr.next = None
        self.keys[pre.next.key] = pre
        self.keys[key] = last
        self.keys[self.dummy.key] = curr
        return

    def pop(self, ):
        head = self.dummy.next
        self.dummy.next = head.next
        if head.next:   # 注意只有一个节点
            self.keys[head.next.key] = self.dummy
        self.keys.pop(head.key)

    def add(self, key, value):
        last = self.keys[self.dummy.key]
        curr = Node(key, value)
        last.next = curr
        self.keys[key] = last
        self.keys[self.dummy.key] = curr

    def get(self, key: int) -> int:
        if key in self.keys:
            ans = self.keys[key].next.val
            self.update(key)
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].next.val = value
            self.update(key)
        else:
            if not self.capacity:
                self.pop()
            else:
                self.capacity -= 1
            self.add(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)