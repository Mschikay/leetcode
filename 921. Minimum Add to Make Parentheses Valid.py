class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        st = []
        for s in S:
            if s == ")":
                if st and st[-1] == "(":
                    st.pop()
                    continue
            st.append(s)
        return len(st)


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        while "()" in S:
            S = S.replace("()","")

        return len(S)


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)