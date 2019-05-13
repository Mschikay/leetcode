
x = "      this is    a question "

def reverseString(s):
    words = []
    cur = s[0]
    for i in range(1, len(s)):
        if s[i] != " " and s[i - 1] == " " or s[i] == " " and s[i - 1] != " ":
            words.append(cur)
            cur = ""
        cur += s[i]
    words.append(cur)
    words.reverse()
    return "".join(words)

# res = reverseString(x)
# print(len(x))
# print(res, len(res))
print(" ".join(x.split()[::-1]))
