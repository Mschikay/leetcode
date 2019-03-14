# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        length = len(root)
        # graph = [[0 for i in range(length)] for i in range(length)]
        # queue = [0]
        # for q in queue:
        #     left = 2 * q + 1
        #     if left < length and root[left] is not None:
        #         queue.append(left)
        #         graph[q][left] = 1
        #         graph[left][q] = 1
        #
        #     right = 2 * q + 2
        #     if right < length and root[right] is not None:
        #         queue.append(right)
        #         graph[q][right] = 1
        #         graph[right][q] = 1

        graph = {}
        queue = [root]
        for q in queue:
            qRoot = graph.get(q.val, [])
            left = queue.left
            if left:
                queue.append(left)
                qRoot.append(left.val)
                qLeft = graph.get(left.val, [])
                qLeft.append(q.val)

            right = queue.right
            if right:
                queue.append(right)
                qRoot.append(left)
                qRight = graph.get(right.val, [])
                qRight.append(q.val)

        visited = set([])

        def dfs(loc, K, res):
            if K == 0:
                if loc not in visited:
                    visited.add(loc)
                    res.append(loc)
                    return
            visited.add(loc)
            for c in graph.get(loc, []):
                if c not in visited:
                    dfs(c, K - 1, res)

            return res

        res = []
        dfs(target, K, res)

        return res


if __name__ == "__main__":
    s = Solution()
    s.distanceK([3,5,1,6,2,0,8,None,None,7,4], 5, 6)
