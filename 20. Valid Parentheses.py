class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or s == []:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == s[i] == "{":
                stack.append(s[i])
            else:
                if stack == []:
                    return False

                top = stack.pop()
                if s[i] == ")" and top == "(":
                    continue
                elif s[i] == "]" and top == "[":
                    continue
                elif s[i] == "}" and top == "{":
                    continue
                else:
                    return False

        return True if stack == [] else False


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or s == []:
            return False
        top = -1
        symbol = {"]": "[", "}": "{", ")": "("}
        for i in range(len(s)):
            if s[i] in symbol.values():
                top += 1
                s = s[i].join((s[0:top], s[top + 1:])) # 用join而不是+会快很多
            else:
                if symbol.get(s[i], None) == s[top]:
                    top -= 1
                else:
                    return False
        return True if top == -1 else False

