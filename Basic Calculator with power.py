class Solution:
    def calculate1(self, s):
        res = 0
        num = 0
        op = '+'
        stack = []
        for i in range(len(s)):
            snapshot = s[i]
            if snapshot.isdigit():
                num = num * 10 + int(snapshot)
            if ((not snapshot.isdigit()) and snapshot!=' ') or i == len(s)-1:
                if op == '+': stack.append(num)
                if op == '-': stack.append(-num)
                if op in '*/':
                    tmp = stack[-1] * num if op == '*' else int(stack[-1] / num)
                    stack.pop()
                    stack.append(tmp)
                op = snapshot
                num = 0
        while stack:
            res += stack.pop()
        return res

    def calculate(self, string):

        num = 0
        op = "+"
        st = []
        i = 0
        while i < len(string):
            if string[i].isdigit():
                num = 10 * num + int(string[i])
            if not string[i].isdigit() or i == len(string) - 1:
                if string[i] == "^":
                    p = 1
                    power = 0
                    while i < len(string) and string[i] == "^":
                        i += 1
                        while i < len(string) and string[i].isdigit():
                            power = 10 * power + int(string[i])
                            i += 1
                        p *= power
                        power = 0
                    num = pow(num, p)
                    print(num)
                if op == "+":
                    st.append(num)
                elif op == "-":
                    st.append(-num)
                elif op == "*":
                    pre = st.pop()
                    st.append(pre * num)
                elif op == "/":
                    pre = st.pop()
                    st.append(pre // num)
                if i < len(string):
                    op = string[i]
                num = 0
            i += 1
        print(st)
        return sum(st)
s = Solution()
# print(s.calculate("1+2*3/4+5^2"))
# print(1+2*3//4+pow(5, 2))
print((s.calculate("2^0+2^2^2/6+3")))
print(pow(2, 0) + pow(pow(2, 2), 2) // 6 + 3)

