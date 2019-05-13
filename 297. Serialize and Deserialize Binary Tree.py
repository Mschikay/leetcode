# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:            # bfs

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        # print(res)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        data = data.split(',')
        for i in range(len(data)):
            if data[i] == '#':
                data[i] = None
            else:
                data[i] = TreeNode(int(data[i]))

        q = deque()
        root = data[0]
        q.append(root)
        j = 1

        while j < len(data):
            node = q.popleft()
            if node:
                node.left = data[j]
                q.append(node.left)
                j += 1
                node.right = data[j]
                j += 1
                q.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:            # PREORDER

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(node, res):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            preorder(node.left, res)
            preorder(node.right, res)

        res = []
        preorder(root, res)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        ele = iter(data.split())

        def preorder():
            e = next(ele)
            if e == "#":
                return None
            node = TreeNode(int(e))
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))