# memory leak

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        cur = ""
        st = []
        for s in S:
            if s.isalpha():
                cur += s
            else:
                n = int(s)
                if st:
                    cur = st.pop() + cur
                st.append(cur * n)
                cur = ""
        if cur != "":
            ans = st.pop() + cur
        else:
            ans = st.pop()
        return ans[K - 1] if K <= len(ans) else ans[-1]