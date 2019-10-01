# https://www.youtube.com/watch?v=uaS1xEMZL_E
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        self.res = []

        def helper(node):
            if not node:
                return
            self.res.append(str(node.val))
            for c in node.children:
                helper(c)
            self.res.append('#')

        helper(root)
        return ' '.join(self.res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if not data: return None
        s = data.split()
        st = []
        ret = None
        for val in s:
            if val == "#":
                st.pop()
            else:
                node = Node(int(val), [])
                if not st:
                    ret = node
                else:
                    st[-1].children.append(node)
                st.append(node)
        return ret
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))