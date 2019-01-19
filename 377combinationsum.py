import copy


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        results = []

        def dfs(remainTarget, startIndex, path):
            if not remainTarget:
                results.append(path)
            if remainTarget < 0 :
                return
            if remainTarget > 0:
                for i in range(startIndex, len(nums)):
                    dfs(remainTarget - nums[i], i, path + [nums[i]])

        def permutation(combinationResult):
            res = []

            if combinationResult is None:
                return res

            newR = list(set(combinationResult))
            for item in newR:
                # print(item)
                rcopy = copy.deepcopy(combinationResult)
                rcopy.remove(item)
                subp = permutation(rcopy)

                if not subp:
                    res.append([item])
                else:
                    for p in subp:
                        res.append([item] + p)
            return res

        dfs(target, 0, [])
        permutationResults = []
        for r in results:
            lengthResult = len(permutation(r))
            permutationResults.append(lengthResult)
        i = 0
        for p in permutationResults:
            i += p
        return i



if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([4, 2, 1], 32))
    # 4, 7
    # 9, 96
    # 2, 3
    # 25, 4930
    # 20, 1601