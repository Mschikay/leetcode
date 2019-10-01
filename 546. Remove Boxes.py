class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(boxes)
        self.boxes = boxes
        self.dp = [[[0] * N for _ in range(N)] for _ in range(N)]
        return self.search(0, N - 1, 0)

    def search(self, l, r, k):
        if l > r:
            return 0

        if self.dp[l][r][k] != 0:
            return self.dp[l][r][k]

        while l < r and self.boxes[r] == self.boxes[r - 1]:
            r -= 1
            k += 1
        self.dp[l][r][k] = self.search(l, r - 1, 0) + (k + 1) * (k + 1)

        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                self.dp[l][r][k] = max(self.dp[l][r][k], self.search(l, i, k + 1) + self.search(i + 1, r - 1, 0))

        return self.dp[l][r][k]