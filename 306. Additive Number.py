class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def getSum(s1, s2):
            s1 = s1[::-1]
            s2 = s2[::-1]
            i = j = 0
            c = 0
            res = ""
            while i < len(s1) and j < len(s2):
                curr = int(s1[i]) + int(s2[j]) + c
                if curr >= 10:
                    c = 1
                else:
                    c = 0
                res += str(curr % 10)
                i += 1
                j += 1

            extra = None
            if i < len(s1):
                extra = s1[i:]
            elif j < len(s2):
                extra = s2[j:]
            if extra:
                k = 0
                while k < len(extra):
                    curr = int(extra[k]) + c
                    if curr >= 10:
                        c = 1
                    else:
                        c = 0
                    res += str(curr % 10)
                    k += 1

            if c: res += "1"
            return res[::-1]

        def dfs(i, j, k):
            if k == len(num): return True
            if num[k] == "0":
                if getSum(num[i:j], num[j:k]) == num[k:k + 1]:
                    return dfs(j, k, k + 1)
            total = getSum(num[i:j], num[j:k])
            for x in range(k + 1, len(num) + 1):
                if total == num[k:x]:
                    if dfs(j, k, x): return True
            return False

        for j in range(1, len(num) - 1):
            if num[j] == "0":
                if dfs(0, j, j + 1): return True
            else:
                for k in range(j + 1, len(num)):
                    if dfs(0, j, k): return True
        return False


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(nums, path):
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            if len(path) >= 3 and not nums:
                return True
            for i in range(len(nums)):
                cur = nums[:i + 1]
                if cur[0] == '0' and len(cur) != 1:
                    continue
                if dfs(nums[i + 1:], path + [int(cur)]):
                    return True
            return False

        return dfs(num, [])