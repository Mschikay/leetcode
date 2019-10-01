class Solution:
    def calculate(self, s: str) -> int:
        def dfs(string, operator):
            ans = 0
            if operator == "+":
                s = string.split("+")
                for ss in s:
                    ans += dfs(ss, "-")
                return ans
            elif operator == "-":
                s = string.split("-")
                for i in range(len(s)):
                    if not i:
                        ans += dfs(s[i], "_")
                    else:
                        ans -= dfs(s[i], "_")
                return ans
            else:
                op = None
                num1 = 0
                num2 = 0
                for s in string:
                    if s.isdigit():
                        if not op:
                            num1 = 10 * num1 + int(s)
                        else:
                            num2 = 10 * num2 + int(s)
                    else:
                        if num1 and num2:
                            if op == "/":
                                num1 = num1 // num2
                            elif op == "*":
                                num1 = num1 * num2
                        op = s
                        num2 = 0
                if op:
                    if op == "/":
                        return num1 // num2
                    else:
                        return num1 * num2
                else:
                    return num1

        s = s.replace(" ", "")
        return dfs(s, "+")

class Solution:
    def calculate(self, s: str) -> int:
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
