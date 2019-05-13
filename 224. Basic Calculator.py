class Solution:
    def calculate(self, s: str) -> int:
        st = []
        n = ""
        for i in range(len(s)):
            e = s[i]
            if e == " ":
                continue
            elif e == "(":
                st.append(e)
            elif e == "+" or e == "-":
                if n != "":
                    st.append(int(n))
                    n = ""
                st.append(e)
            elif e == ")":
                if n != "":
                    st.append(int(n))
                    n = ""
                newSt = []
                while st:
                    x = st.pop()
                    if x == "(":
                        break
                    else:
                        newSt.append(x)
                t = 0
                while newSt:
                    x = newSt.pop()
                    if x == "+":
                        t += newSt.pop()
                    elif x == "-":
                        t += newSt.pop() * (-1)
                    else:
                        t += x
                st.append(t)
            else:
                n += e

        if n != "":
            st.append(int(n))
        res = st[0]
        i = 1
        while i < len(st):
            if st[i] == "+":
                res += st[i + 1]
                i = i + 2
            elif st[i] == "-":
                res -= st[i + 1]
                i = i + 2
        return res

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