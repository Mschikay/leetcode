# Robin round, a much better solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length, subRes, res = 0, [], []
        for w in words:
            if length + len(w) + len(subRes) > maxWidth:
                restSpace = maxWidth - length - len(subRes) + 1
                for i in range(restSpace):
                    subRes[i % (len(subRes) - 1 or 1)] += " "
                res.append(" ".join(subRes))
                length = 0
                subRes = []

            length += len(w)
            subRes.append(w)
        if subRes:
            cur = " ".join(subRes)
            cur += " " * (maxWidth - len(cur))
            res.append(cur)
        return res


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = j = 0
        while i < len(words):
            length = -1
            while j < len(words):
                length += len(words[j]) + 1
                if length > maxWidth:
                    break
                j += 1

            cur = ""
            if j != len(words):
                if j - i == 1:
                    cur = words[i] + " " * (maxWidth - len(words[i]))
                else:
                    newLength = length - len(words[j]) - 1
                    spaces = maxWidth - newLength
                    rs = spaces // (j - i - 1) + 1
                    ls = spaces % (j - i - 1)
                    for x in range(i, j):
                        if x == j - 1:
                            cur = "".join((cur, words[x]))
                            continue
                        if ls:
                            cur = "".join((cur, words[x], " " * (rs + 1)))
                            ls -= 1
                        else:
                            cur = "".join((cur, words[x], " " * (rs)))
            else:
                for x in range(i, j):
                    if x == j - 1:
                        cur = "".join((cur, words[x]))
                    else:
                        cur = "".join((cur, words[x], " "))
                cur = "".join((cur, " " * (maxWidth - len(cur))))
            res.append(cur)
            i = j
        return res
