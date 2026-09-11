from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, left: int, right: int):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return validate(node.left, left, node.val) and validate(
                node.right, node.val, right
            )

        return validate(root, float("-inf"), float("inf"))


root = TreeNode(5)
kid1 = TreeNode(4)
kid2 = TreeNode(6)
kid3 = TreeNode(3)
kid4 = TreeNode(7)

root.left = kid1
root.right = kid2

kid2.left = kid3
kid2.right = kid4

a = Solution()

ans = a.isValidBST(root)

print(ans)
