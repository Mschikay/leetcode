from collections import Counter


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isPalindrome(s):
            d = Counter(s)
            res = False
            for v in d.values():
                if v % 2 == 1:
                    if not res:
                        res = True, d
                    else:
                        return False, d
            return True, d

        def permutation(i, curr, v, ans, ss):
            if len(curr) == len(ss):
                ans.append("".join(curr))
            currj = set()
            for j in range(len(ss)):
                if j in v or ss[j] in currj:
                    continue
                currj.add(ss[j])
                v.add(j)
                permutation(j, curr + [ss[j]], v, ans, ss)
                v.remove(j)

        pal, d = isPalindrome(s)
        if pal:
            visit = set()
            ans = []
            s1 = ""
            single = ""
            for k, v in d.items():
                if v % 2 == 1:
                    single = k
                s1 += k * (v // 2)

            permutation(0, [], visit, ans, s1)

            for i in range(len(ans)):
                ans[i] += single + ans[i][::-1]
            return ans

        return []



'''
time and space, see the solution
'''