import math
import pprint


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k > math.factorial(n) or n <= 0:
            return None

        numbers = []
        for i in range(1, n + 1):
            numbers.append(i)

        # perm = [[1]]
        # for i in range(1, len(nums)):
        #     n = nums[i]
        #     new_perm = []
        #     for p in perm:
        #         l_perm = len(p)
        #         for j in range(l_perm+1):
        #             new_perm.append(p[:j] + [n] + p[j:l_perm])
        #     perm = new_perm
        #         pprint.pprint(perm)

        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            f = math.factorial(n)
            # get the index of current digit
            index, k = k // f, k % f
            permutation += str(numbers[index])
            # remove handled number
            del numbers[index]

        return permutation


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 3))

