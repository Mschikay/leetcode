class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            a = s[l].lower()
            b = s[r].lower()
            if a == b:
                l += 1
                r -= 1
            else:
                return False
        return True

