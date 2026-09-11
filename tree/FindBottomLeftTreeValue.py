from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.leftest = 0
        self.depth = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root and not root.left and not root.right:
            return root.val
        self.deepest_left(root)
        return self.leftest

    def deepest_left(self, node: Optional[TreeNode], current_depth=0):
        if node:
            if current_depth > self.depth:
                self.depth = current_depth
                self.leftest = node.val
            self.deepest_left(node.left, current_depth + 1)
            self.deepest_left(node.right, current_depth + 1)
