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