
class Solution:
    def find(self, l, n):
        if not l:
            return None

        start = 0
        end = len(l)-1

        while start + 1 < end:
            mid = start+(end-start)//2

            if n > l[mid]:
                if l[mid] < l[start]:
                    if n > l[end]:
                        end = mid
                    else:
                        start = mid
                else:
                    start = mid

            elif n < l[mid]:
                if l[start] < l[mid]:
                    if n > l[start]:
                        end = mid
                    else:
                        start = mid
                else:
                    end = mid

            elif n == l[mid]:
                return mid

        if n == l[start]:
            return start

        if n == l[end]:
            return end

        return None


if __name__ == '__main__':
    s = Solution()
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 4))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 5))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 6))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 7))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 1))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 2))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 3))
    print(s.find([4, 5, 6, 7, 0, 1, 2, 3], 0))
