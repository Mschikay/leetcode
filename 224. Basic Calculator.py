
def calculate(self, s):
    res, num, sign, stack = 0, 0, 1, []
    for ss in s:
        if ss.isdigit():
            num = 10*num + int(ss)
        elif ss in ["-", "+"]:
            res += sign*num
            num = 0
            sign = [-1, 1][ss=="+"]
        elif ss == "(":
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif ss == ")":
            res += sign*num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num*sign


class Solution:
    def calculate(self, S):
        ans = 0
        num = 0
        s = 1
        st = []
        for x in S:
            if x.isdigit():
                num = 10 * num + int(x)
            elif x == "+" or x == "-":
                ans += num * s
                s = [-1, 1][x == "+"]
                num = 0
            elif x == ")":
                ans += s * num
                ans *= st.pop()
                ans += st.pop()
                s = 1
                num = 0
            elif x == "(":
                st.append(ans)
                st.append(s)
                ans = 0
                s = 1
        return ans + s * num