class StockSpanner:

    def __init__(self):
        self.st = []
        self.n = []

    def next(self, price: int) -> int:
        self.n.append(1)
        i = idx = len(self.n) - 1
        while self.st and self.st[-1][1] <= price:
            i, x = self.st.pop()
        num = self.n[i] + idx - i
        self.st.append((idx, price))
        self.n[idx] = num
        return num

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1]
        self.stack.append((price, cnt))
        return cnt