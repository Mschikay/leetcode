class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if haystack[i] != needle[0]: continue
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len(needle): return i
        return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if haystack[i:i + l] == needle[:]: return i
        return -1
