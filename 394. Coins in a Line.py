# There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.
#
# Could you please decide the first player will win or lose?
#
# If the first player wins, return true, otherwise return false.
#
# Example
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 4
# Output: true
# Explanation:
# The first player takes 1 coin at first. Then there are 3 coins left.
# Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
# Challenge
# O(n) time and O(1) memory
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n: return False
        dp = [False for i in range(n + 1)]
        dp[1] = True
        for i in range(2, len(dp)):
            if not dp[i - 1] or not dp[i - 2]:
                dp[i] = True
        return dp[n]


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n: return False
        pre1 = False
        pre2 = True
        for i in range(1, n + 1):
            if i == 1:
                curr = True
            else:
                curr = not pre1 or not pre2
                pre1, pre2 = pre2, curr
        return curr