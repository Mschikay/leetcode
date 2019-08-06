'''
254. Factor Combinations
Medium

407

19

Favorite

Share
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(curr, i, target, ans):
            if curr:
                ans.append(curr + [target])
            for j in range(i, target // i + 1):
                if j > target // j: break # 剪支
                if not target % j:
                    dfs(curr + [j], j, target // j, ans)
            return

        ans = []
        dfs([], 2, n, ans)
        return ans
