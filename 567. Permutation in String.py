class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, a1, a2 = len(s1), [0] * 26, [0] * 26
        for s in s1:
            a1[ord(s) - ord("a")] += 1

        for i in range(len(s2)):
            a2[ord(s2[i]) - ord("a")] += 1
            if i >= n:
                a2[ord(s2[i - n]) - ord("a")] -= 1
            if a2 == a1:
                return True
        return False