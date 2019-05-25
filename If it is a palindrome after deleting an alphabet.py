
def delete(str):

    def isPalindrome(str):
        return str == str[::-1]

    if not str: return False
    l, r = 0, len(str) - 1
    while l < r:
        if str[l] == str[r]:
            l += 1
            r -= 1
        else:
            return isPalindrome(str[l:r]) or isPalindrome(str[l + 1:r + 1])
    return True