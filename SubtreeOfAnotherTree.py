from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: TreeNode) -> bool:

        # def serialize(node):
        #     if not node:
        #         return
        #     tree.append(f'^{node.val}')
        #     serialize(node.left)
        #     serialize(node.right)
        # tree = []
        # serialize(root)
        # root_tree = ''.join(tree)
        # tree = []
        # serialize(subRoot)
        # sub_tree = ''.join(tree)

        # return sub_tree in root_tree

        if not root or not subRoot:
            return root == subRoot

        def compare(node, sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            if node.val != sub.val:
                return False
            return compare(node.left, sub.left) and compare(node.right, sub.right)

        def find_root(node):
            if not node:
                return False
            if node.val ==subRoot.val and compare(node, subRoot):
                return True

            return find_root(node.left) or find_root(node.right)

        return find_root(root)
