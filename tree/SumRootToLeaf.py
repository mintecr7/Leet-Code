# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int | None:
        total = self.rec_add(root)
        return total

    def rec_add(self, root: Optional[TreeNode]) ->int | None:
        if not root:
            return
        temp_l = str(root.val)
        temp_r = str(root.val)
        if root.left:
            temp_l += str(self.rec_add(root.left))

        if root.right:
            temp_r += str(self.rec_add(root.right))
        else:
            temp_r = '0'
        print(temp_l, temp_r)
        return int(temp_l) + int(temp_r)
