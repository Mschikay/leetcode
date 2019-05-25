# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n - 1
        while l <= h:
            print(l, h)
            mid = (l + h) // 2
            hint = guess(mid)
            if hint == 0:
                return mid
            if hint == 1:
                l = mid + 1
            if hint == -1:
                h = mid - 1
        return l