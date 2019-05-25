class Solution(object):
    def divide(self, dividend, divisor):
        s = -1 if (dividend < 0) ^ (divisor < 0) else 1

        d = abs(divisor)
        dd = abs(dividend)
        l, h = 0, dd
        while l <= h:
            mid = (l + h) // 2
            if mid * d >= dd:
                h = mid - 1
            else:
                l = mid + 1
        res = l * s if l * d <= dd else (l - 1) * s
        if res > 2147483647 or res < -2147483648:
            return 2147483647
        else:
            return res