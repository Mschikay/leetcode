class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        step = 1
        cur = s[0:step]
        while step < l:
            if l % step == 0:
                i = 1
                while i < l // step:
                    if s[step * i:step * i + step] != cur:
                        break
                    i += 1
                if i == l // step: return True
            step += 1
            cur = s[0:step]
        return False

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = s + s
        ss = ss[1:-1]

        return s in ss
