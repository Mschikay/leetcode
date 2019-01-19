class Solution(object):

    def divide(self, dividend, divisor):
        if divisor == 0:
            return None

        new_dividend = abs(dividend)
        new_divisor = abs(divisor)

        if new_dividend < new_divisor or new_dividend == 0:
            return 0

        c = 1
        if dividend < 0 < divisor or dividend > 0 > divisor:
            c = -1

        start = 0
        end = new_dividend
        res = None

        while start + 1 < end:
            mid = start + (end - start) // 2

            if mid * new_divisor > new_dividend:
                end = mid
            elif mid * new_divisor < new_dividend:
                start = mid
            else:
                res = c * mid
                if res < pow(-2, 31) or res > pow(2, 31) - 1:
                    return pow(2, 31) - 1
                else:
                    return res
        if end * new_divisor <= new_dividend:
            res = c * end
        elif start * new_divisor <= new_dividend:
            res = c * start
        else:
            return None

        if res < pow(-2, 31) or res > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.divide(1, 1))

