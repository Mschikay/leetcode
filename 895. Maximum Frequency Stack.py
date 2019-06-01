from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.s = []
        self.r = []
        self.d = defaultdict(lambda: 0)

    def push(self, x: int) -> None:
        self.s.append(x)
        self.d[x] += 1

    def pop(self) -> int:
        if not self.s: return None
        m = max(self.d.values())
        for i in range(len(self.s) - 1, -1, -1):
            if self.d[self.s[i]] == m:
                self.d[self.s[i]] -= 1
                x = self.s[i]
                del self.s[i]
                return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()