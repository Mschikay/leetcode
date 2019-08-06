class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        def getMax(area):
            st = [0]
            area.append(0)
            ans = 0
            for r in range(1, len(area)):
                while st and area[st[-1]] > area[r]:
                    h = area[st.pop()]
                    l = -1 if not st else st[-1]
                    ans = max(ans, (r - l - 1) * h)
                st.append(r)
            return ans

        ans = 0

        area = [0 for i in range(len(matrix[0]))]
        for low in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[low][i] == "1":
                    area[i] += 1
                else:
                    area[i] = 0
            ans = max(ans, getMax(area))
        return ans