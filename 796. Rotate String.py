class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B: return True
        b = 0
        while True:
            idx = A.find(B[0], b)
            if idx == -1: return False
            i, j = idx, 0
            while i < len(A) and j < len(B):
                if A[i] == B[j]:
                    i += 1
                    j += 1
                    continue
                break
            if i >= len(A) and A[:idx] == B[j:]: return True
            b = idx + 1

# O(n^2)