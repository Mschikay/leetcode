class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for s in S:
            if st and st[-1] == s:
                st.pop()
            else:
                st.append(s)
        return "".join(st)