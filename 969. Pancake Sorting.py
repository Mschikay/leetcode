class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for h in range(len(A), 0, -1):
            i = A[:h].index(max(A[:h]))
            if i == h - 1:
                continue
            if i:
                ans.append(i + 1)
                A[:i + 1] = reversed(A[:i + 1])
            ans.append(h)
            A[:h] = reversed(A[:h])

        return ans