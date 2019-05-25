# the area can only increase by moving the pointer of shorter value
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, h = 0, len(height) - 1
        area = 0
        while l < h:
            area = max(area, min(height[l], height[h]) * (h - l))
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
        return area
