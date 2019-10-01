class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = [0]
        for x1, y1, x2, y2 in rects:
            self.prefix.append((x2 - x1 + 1) * (y2 - y1 + 1) + self.prefix[-1])

    def pick(self) -> List[int]:
        num = random.randint(0, self.prefix[-1])
        l, h = 0, len(self.prefix) - 1
        while l <= h:
            m = (l + h) // 2
            if self.prefix[m] < num:
                l = m + 1
            else:
                h = m - 1
        x1, y1, x2, y2 = self.rects[l - 1]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()