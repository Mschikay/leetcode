class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        dif = 0
        i, j = len(S) - 1, len(T) - 1
        ni = nj = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    ni += 1
                    i -= 1
                else:
                    if ni:
                        ni -= 1
                        i -= 1
                    else:
                        break
            while j >= 0:
                if T[j] == "#":
                    nj += 1
                    j -= 1
                else:
                    if nj:
                        nj -= 1
                        j -= 1
                    else:
                        break
            if i >= 0 and j >= 0 and S[i] == T[j]:
                i -= 1
                j -= 1
            elif i < 0 and j < 0:
                return True
            else:
                return False
        return True