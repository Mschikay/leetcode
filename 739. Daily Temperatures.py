class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        ans = [0] * len(T)
        for i in range(len(T)):
            while st and T[st[-1]] < T[i]:
                pre = st.pop()
                ans[pre] = i - pre
            st.append(i)
        return ans