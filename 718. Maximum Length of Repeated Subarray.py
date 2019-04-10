class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        last = [0 for i in range(len(A))]
        maxL = 0

        for i in range(len(B)):
            newLast = [0 for i in range(len(A))]
            for j in range(len(A)):
                if B[i] == A[j]:
                    if j == 0:
                        newLast[j] = 1
                    else:
                        newLast[j] = last[j - 1] + 1
                else:
                    newLast[j] = 0

            if maxL < max(newLast):
                maxL = max(newLast)
            last = newLast

        return maxL