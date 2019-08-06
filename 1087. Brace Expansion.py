class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        st = [""]
        i = 0
        while i < len(S):
            if S[i].isalpha():
                s = ""
                while i < len(S) and S[i].isalpha():
                    s += S[i]
                    i += 1
                newSt = []
                for ele in st:
                    newSt.append(ele + s)
                st = newSt
            else:
                i += 1
                newSt = []
                while i < len(S) and S[i] != "}":
                    if S[i].isalpha():
                        for ele in st:
                            newSt.append(ele + S[i])
                    i += 1
                st = newSt
                i += 1
        return sorted(st)


class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        def backtrack(i, curr, ans):
            if i == len(S):
                ans.append(curr)
                return
            if S[i].isalpha():
                backtrack(i + 1, curr + S[i], ans)
            else:
                j = i + 1
                while j < len(S) and S[j] != "}":
                    j += 1
                char = sorted(S[i + 1:j].split(","))
                for c in char:
                    backtrack(j + 1, curr + c, ans)
            return

        ans = []
        backtrack(0, "", ans)
        return ans

