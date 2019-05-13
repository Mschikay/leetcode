class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [i for i in range(1, n + 1)]
        for i in range(1, k + 1):
            res = res[:i - 1] + res[i - 1:][::-1]
        return res


# A faster method
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        temp = [i for i in range(1, n + 1)]
        l = 0
        r = n - 1
        res = []

        for x in range(k):
            if x % 2 == 0:
                res += [temp[l]]
                l += 1
            else:
                res += [temp[r]]
                r -= 1
        if k % 2 == 0:
            res += temp[l:r + 1][::-1]
        else:
            res += temp[l:r + 1]
        return res

