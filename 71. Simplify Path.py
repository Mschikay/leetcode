class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        print(paths)
        st = []
        for p in paths:
            if p == "..":
                if st:
                    st.pop()
            elif p == "." or p == "/" or p == "":
                continue
            else:
                st.append(p)
        return "/" + "/".join(st)
