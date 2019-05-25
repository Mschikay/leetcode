# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                h = mid - 1
                if h < l:
                    return h + 1
            else:
                l = mid + 1
                if l > h:
                    return l