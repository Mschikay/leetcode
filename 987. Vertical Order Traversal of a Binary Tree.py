class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return None

        d = collections.defaultdict(list)
        st = [(0, root)]
        new = []
        left = right = 0
        while st:
            l, node = st.pop(0)
            left = min(l, left)
            right = max(l, right)
            d[l].append(node.val)
            if node.left:
                new.append((l - 1, node.left))
            if node.right:
                new.append((l + 1, node.right))
            if not st:
                st = sorted(new, key=lambda x: (x[0], x[1].val))
                new = []

        order = []
        for k in range(left, right + 1):
            order.append(d[k])
        return order


from collections import defaultdict


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = defaultdict(list)

        def dfs(root, vlevel, hlevel):
            if not root:
                return
            ans[vlevel].append((hlevel, root.val))
            if root.left:
                dfs(root.left, vlevel - 1, hlevel + 1)
            if root.right:
                dfs(root.right, vlevel + 1, hlevel + 1)

        dfs(root, 0, 0)

        res = []

        for k in sorted(ans.keys()):
            res.append([x[1] for x in sorted(ans[k])])

        return res
