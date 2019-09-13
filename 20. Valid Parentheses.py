class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {"]":"[", "}":"{", ")":"("}
        st = []
        for x in s:
            if x in ("{", "[", "("):
                st.append(x)
            else:
                if st and st.pop() == symbol[x]:
                    continue
                return False
        return True if not st else False