from typing import Optional
class TreeNode:
    """
        this problem is not solved yet
    """
    def __init__(self,
                    val=0,
                    left=None,
                    right=None,
                    depth=0,
                    isEvenOdd=True):
        self.val = val
        self.left = left
        self.right = right
        self.depth = depth
        self.isEvenOdd = isEvenOdd
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root and not root.left and not root.right:
            return False



        return False

    def travers(self, node: Optional[TreeNode], current_depth=0):
        if
