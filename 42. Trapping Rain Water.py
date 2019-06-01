class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r = 0, len(height) - 1
        # ans = 0
        # leftmax = rightmax = 0
        # while l < r:
        #     left, right = height[l], height[r]
        #     if left < right:
        #         leftmax = max(leftmax, left)
        #         ans += leftmax - left
        #         l += 1
        #     else:
        #         rightmax = max(rightmax, right)
        #         ans += rightmax - right
        #         r -= 1
        # return ans
        st = []
        ans = 0
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                interval = st.pop()
                if st:
                    ans += (min(height[st[-1]], h) - height[interval]) * (i - st[-1] - 1)
            st.append(i)

        return ans