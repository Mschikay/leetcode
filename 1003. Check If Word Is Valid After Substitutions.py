class Solution:
    def isValid(self, S: str) -> bool:

        while True:
            S = "".join(S.split("abc"))
            if "abc" not in S:
                break

        return S == ""


class Solution:
    def isValid(self, S: str) -> bool:
        st = []
        for s in S:
            st.append(s)

            if s == "c":
                st.pop()
                if len(st) > 1 and st[-2:] == ["a", "b"]:
                    st.pop()
                    st.pop()
                else:
                    return False
        return True if not st else False