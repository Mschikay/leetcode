'''4^(l1), space (l1)'''
class Solution:
    def isScramble(self, S1: str, S2: str) -> bool:
        mem = {}

        def dfs(s1, s2):
            if (s1, s2) in mem: return mem[(s1, s2)]
            if sorted(s1) != sorted(s2):
                mem[(s1, s2)] = False
                return False
            if s1 == s2:
                mem[(s1, s2)] = True
                return True
            else:
                res = False
                for i in range(len(s1) - 1):
                    if dfs(s1[:i + 1], s2[:i + 1]) and dfs(s1[i + 1:], s2[i + 1:]) or dfs(s1[:i + 1],
                                                                                          s2[-(i + 1):]) and dfs(
                            s1[i + 1:], s2[:-(i + 1)]):
                        res = True
                        break

                mem[(s1, s2)] = res
                return res

        if not S1 or not S2: return False
        return dfs(S1, S2)