class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ser = ""

        def dfs(node: TreeNode):
            nonlocal ser
            if not node:
                ser += ",N"
                return
            ser += f",{node.val}"
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return ser[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")

        i = 0

        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(vals[i]))

            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(3)
kid3 = TreeNode(4)
kid4 = TreeNode(5)

root.right = kid2
root.left = kid1

kid2.left = kid3
kid2.right = kid4


a = Codec()

print(a.serialize(root))
