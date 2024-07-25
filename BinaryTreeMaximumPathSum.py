from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(node: TreeNode):
            nonlocal total
            if not node:
                return 0
            left_max = path_sum(node.left)
            right_max = path_sum(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            total = max(total, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        total = root.val
        path_sum(root)

        return total


root = TreeNode(-10)
kid1 = TreeNode(9)
kid2 = TreeNode(20)
kid3 = TreeNode(15)
kid4 = TreeNode(7)


root.right = kid2
root.left = kid1

kid2.left = kid3
kid2.right = kid4

a = Solution()

ans = a.maxPathSum(root)
