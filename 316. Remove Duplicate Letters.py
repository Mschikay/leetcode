from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        d = Counter(s)
        v = set()
        for x in s:
            d[x] -= 1
            if x in v: continue
            while st and d[st[-1]] and ord(st[-1]) >= ord(x):
                v.remove(st.pop())
            st.append(x)
            v.add(x)

        return "".join(st)