# 完全二叉树求数字和最大的层数
# Definition for a binary tree node.

import sys
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):

        queue = deque()
        queue.append([0, root])
        currLevel = 0
        maxSum = -sys.maxsize
        currSum = 0

        while queue:
            level, node = queue.popleft()

            if currLevel != level:
                currLevel = level
                currSum = 0

            currSum += node.val
            if node.left:
                queue.append([level+1, node.left])

            if node.right:
                queue.append([level+1, node.right])

            maxSum = max(maxSum, currSum)

        return maxSum


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(-1)
    n1 = TreeNode(2)
    n2 = TreeNode(-3)
    n3 = TreeNode(4)
    n4 = TreeNode(-6)
    n5 = TreeNode(2)
    n6 = TreeNode(9)
    n8 = TreeNode(-100)

    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    n3.right = n8

    print(s.sumNumbers(root))


