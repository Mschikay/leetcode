class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        popped = popped[::-1]
        for p in pushed:
            st.append(p)
            while st and popped and st[-1] == popped[-1]:
                st.pop()
                popped.pop()

        return not st
