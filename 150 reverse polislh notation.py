from math import floor, ceil


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                y = s.pop()
                x = s.pop()
                s.append(x + y)
            elif t == "-":
                y = s.pop()
                x = s.pop()
                s.append(x - y)
            elif t == "*":
                y = s.pop()
                x = s.pop()
                s.append(x * y)
            elif t == "/":
                y = s.pop()
                x = s.pop()
                s.append(floor(x / y) if x / y >= 0 else ceil(x / y))
            else:
                s.append(int(t))
        return s[-1]

