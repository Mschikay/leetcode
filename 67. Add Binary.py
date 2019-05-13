class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        d = 0
        res = []
        l = len(a) - 1
        while l >= 0:
            t = int(a[l]) + int(b[l]) + d
            if t == 2:
                res.append('0')
                d = 1
            elif t == 3:
                res.append('1')
                d = 1
            else:
                res.append(str(t))
                d = 0
            l -= 1

        if d:
            res.append('1')
        return "".join((res[::-1]))

# The recursive method is slower

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        s = int(a[-1]) + int(b[-1])
        if s == 2:
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + str(s)