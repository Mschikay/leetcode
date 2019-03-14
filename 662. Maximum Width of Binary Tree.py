# 此方法超时了……
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = 0
        queue = [root]
        length = 1
        while q < length:
            if queue[q] is not None:
                length = 2 * q + 2 + 1
                if queue[q].left:
                    queue.append(queue[q].left)
                else:
                    queue.append(None)
                if queue[q].right:
                    queue.append(queue[q].right)
                else:
                    queue.append(None)
            else:
                queue.append(None)
                queue.append(None)
            q += 1

        q = 0
        power = 1
        maxWidth = 0
        while q < length:
            last = first = -1
            for i in range(q, q + power):
                if queue[i] is not None:
                    last = i
                    if first == -1:
                        first = i

            width = last - first + 1

            if width > maxWidth:
                maxWidth = width

            q = 2 * q + 1
            power *= 2

        return maxWidth


### a faster way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxWidth = 0

        def dfs(root, q, level, start, end):
            if root is None:
                return

            if len(start) < level:
                start.append(q)
            else:
                if start[level - 1] > q:
                    start[level - 1] = q

            if len(end) < level:
                end.append(q)
            else:
                if end[level - 1] < q:
                    end[level - 1] = q  # 不要使用-1，因为可能end的长度会比记录深度的level更长 因为这是前序遍历

            dfs(root.left, 2 * q + 1, level + 1, start, end)
            dfs(root.right, 2 * q + 2, level + 1, start, end)

        start = []
        end = []
        dfs(root, 0, 1, start, end)
        print(start, end)
        width = [end[i] - start[i] + 1 for i in range(len(end))]
        return max(width)

