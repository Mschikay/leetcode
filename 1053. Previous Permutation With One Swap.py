class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        l = len(A) - 1
        while l - 1 >= 0 and A[l - 1] <= A[l]:
            l -= 1
        if not l: return A
        r = l
        while r + 1 < len(A) and A[r + 1] > A[r] and A[r + 1] < A[l - 1]:
            r += 1
        A[l - 1], A[r] = A[r], A[l - 1]
        return A