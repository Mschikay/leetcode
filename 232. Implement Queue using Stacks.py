class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.r = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): return None
        while self.st:
            self.r.append(self.st.pop())
        x = self.r.pop()
        while self.r:
            self.st.append(self.r.pop())
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        return None if self.empty() else self.st[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.st else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()