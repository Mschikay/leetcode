class Solution(object):
    def repeatedStringMatch(self, A, B):
        ceil = 1 if len(B) % len(A) else 0
        s = len(B) // len(A) + ceil
        a = A * s
        if B in a: return s
        a += A
        if B in a: return s + 1
        return -1