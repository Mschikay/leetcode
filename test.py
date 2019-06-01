
x = "      this is    a question "

def reverseString(s):
    # words = []
    # cur = s[0]
    # for i in range(1, len(s)):
    #     if s[i] != " " and s[i - 1] == " " or s[i] == " " and s[i - 1] != " ":
    #         words.append(cur)
    #         cur = ""
    #     cur += s[i]
    # words.append(cur)
    # words.reverse()
    # return "".join(words)
    a = x.split(" ")
    ans = []
    while a:
        ans.append(a.pop())
    return " ".join(ans)


res = reverseString(x)
print(len(x))
print(res, len(res))



# def delete(str):
#     def isPalindrome(str):
#         return str == str[::-1]
#
#     if not str: return False
#     l, r = 0, len(str) - 1
#     while l < r:
#         if str[l] == str[r]:
#             l += 1
#             r -= 1
#         else:
#             return isPalindrome(str[l:r]) or isPalindrome(str[l + 1:r + 1])
#     return True
#
# print(delete("a"))