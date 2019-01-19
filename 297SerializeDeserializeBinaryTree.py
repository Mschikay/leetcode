# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return None

        node = [root]
        i = 0
        num = 0
        while i < len(node):
            if node[i].val is not None:
                if node[i].left is None and node[i].right is None:
                    num += 2
                else:
                    node += [TreeNode(None)] * num
                    num = 0

                    if node[i].left:
                        node.append(node[i].left)
                    else:
                        node.append(TreeNode(None))
                    if node[i].right:
                        node.append(node[i].right)
                    else:
                        num += 1
            i += 1
        node_val = [n.val for n in node]
        return str(node_val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) <= 2:
            return None

        # str to list
        data = data[1:-1]
        data_list = data.split(', ')
        for j in range(len(data_list)):
            if data_list[j] != 'None':
                data_list[j] = int(data_list[j])
            else:
                data_list[j] = None

        d = 0
        i = 0
        node = [TreeNode(data_list[0])]
        len_data = len(data_list)
        while i < len(node):
            if node[i].val is not None:
                d += 1
                if d < len_data:
                    node[i].left = TreeNode(data_list[d])
                    node.append(node[i].left)
                d += 1
                if d < len_data:
                    node[i].right = TreeNode(data_list[d])
                    node.append(node[i].right)
            i += 1

        val = [i.val for i in node]

        return val

    def serialize_dfs(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')


    def deserialize_dfs(self, data):

        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


if __name__ == '__main__':
    # node9 = TreeNode(9, None, None)
    # node8 = TreeNode(8, None, node9)
    # node6 = TreeNode(6, None, None)
    # node5 = TreeNode(5, None, None)
    # node3 = TreeNode(3, node6, node8)
    # node2 = TreeNode(2, None, node5)
    # node = TreeNode(1, node2, node3)

    node2 = TreeNode(2, None, None)
    node = TreeNode(1, node2, None)

    codec = Codec()
    print(codec.serialize_dfs(node))
    # res = codec.deserialize(codec.serialize(node))
    # res = codec.deserialize('[0, 0, 0, 0, None, None, 1, None, None, None, 2]')
    # print(res)

