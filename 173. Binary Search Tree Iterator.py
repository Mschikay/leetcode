# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        self.cur = root
        self.pushLeft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.s: return None

        res = self.s.pop()
        self.pushLeft(res.right)
        return res.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.s: return False
        return True

    def pushLeft(self, node):
        if node:
            while node:
                self.s.append(node)
                node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.dq = collections.deque()
        self.inorder(root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.dq.append(root.val)
            self.inorder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.dq:
            return self.dq.popleft()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.dq) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()