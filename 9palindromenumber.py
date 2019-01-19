'''
Recursively mod ten and divided by ten until the number equals 0 after the last division.
We will get each digit and put them into an array.
Compare 2 digits from the first and last each time until their address meet
'''
import sys

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            print("FALSE")
            return
        elif x // 10 == 0:
            print("TRUE")
            return
        else:
            arr = []
            i = x
            # put each digit number into an array
            while i > 0:
                num = i % 10
                arr.append(num)
                i = i // 10
            print(arr)

            # check the multi-digits int
            a = 0
            b = len(arr) - 1
            while a < b:
                if arr[a] != arr[b]:
                    print("FALSE")
                    return
                else:
                    pass
                a = a + 1
                b = b - 1
            print("TRUE")


if __name__ == "__main__":
    s = Solution()
    x = int(sys.argv[1])
    print(x)
    s.isPalindrome(x)


