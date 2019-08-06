class Solution(object):
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


class Solution(object):
    def decodeString(self, s):
        def dfs(s):
            res = ''
            i = 0
            num = 0
            start = i
            k = 0
            while i < len(s):
                if s[i].isdigit():
                    while i < len(s) and s[i].isdigit():
                        k = 10 * k + int(s[i])
                        i += 1
                    continue
                if s[i] == "[":
                    start = i + 1
                    while i < len(s):
                        if s[i] == "[":
                            num += 1
                        elif s[i] == "]":
                            num -= 1
                            if not num:
                                res += k * dfs(s[start:i])
                                k = 0
                                num = 0
                                break
                        i += 1
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s)


class Solution:
    def decodeString(self, s: str) -> str:
        def helper(start_index):
            result = ""
            number = ""
            i = start_index
            while i < len(s):
                if s[i].isdigit():
                    number += s[i]
                elif s[i] == "[":
                    segment, end_index = helper(i + 1)
                    result += segment * int(number)
                    number = ""
                    i = end_index
                elif s[i] == "]":
                    return result, i
                else:
                    result += s[i]
                i += 1
            return result, len(s)

        result, _ = helper(0)
        return result


class Solution(object):
    def decodeString(self, s):
        i = 0
        st = []
        self.curr = ""
        while i < len(s):
            if s[i].isdigit():
                st.append(self.curr)
                st.append("+")
                n = 0
                while i < len(s) and s[i].isdigit():
                    n = 10 * n + int(s[i])
                    i += 1
                st.append(n)
                st.append("*")
                self.curr = ""
            elif s[i] == "[":
                i += 1
                while i < len(s) and s[i].isalpha():
                    self.curr += s[i]
                    i += 1
            elif s[i] == "]":
                if st and st[-1] == "*":
                    st.pop()
                    self.curr = self.curr * int(st.pop())
                    while st and st[-1] == "+":
                        st.pop()
                        self.curr = st.pop() + self.curr
                i += 1
            else:
                self.curr += s[i]
                i += 1

        while st:
            st.pop()
            if st[-1] == "*":
                self.curr = self.curr * int(st.pop())
            else:
                self.curr = st.pop + self.curr
        return self.curr

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(ss):
            res = ''
            i = 0
            length = 0
            while i < len(ss):
                if ss[i].isdigit():
                    n = 1
                    while i + n < len(ss) and ss[i + n].isdigit():
                        n += 1
                    subres = helper(ss[i + n + 1:])
                    res += int(ss[i:i + n]) * subres[0]
                    length += n + subres[1] + 1 # 1是"["
                    i += n + subres[1] + 1
                elif ss[i].isalpha():
                    res += ss[i]
                    length += 1
                    i += 1
                elif ss[i] == ']':
                    return [res, length + 1]
            return [res, length]
        return helper(s)[0]


class Solution(object):
    def decodeString(self, s):
        st = []
        curr = ""
        n = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    n = 10 * n + int(s[i])
                    i += 1
            elif s[i] == "[":
                st.append(curr)
                st.append(n)
                curr = ""
                n = 0
                i += 1
            elif s[i] == "]":
                curr = curr * int(st.pop())
                curr = st.pop() + curr
                i += 1
            else:
                curr += s[i]
                i += 1
        return curr