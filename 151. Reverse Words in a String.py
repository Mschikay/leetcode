class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = []
        cur = ""
        s = s.strip()
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if i > 0 and s[i] != " " and s[i - 1] == " ":
                words.append(cur)
                cur = ""
            cur += s[i]
        if cur != "": words.append(cur)
        words.reverse()
        return " ".join(words)

        # or just use one line
        # " ".join(x.split()[::-1])