from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def count(node: TreeNode, cur_depth):
            nonlocal depth
            if not node.left and not node.right:
                cur_depth += 1
                if cur_depth > depth:
                    depth = cur_depth
                return
            if node.left:
                count(node.left, cur_depth+1)
            if node.right:
                count(node.right, cur_depth+1)
        if root:
            count(root, 0)
        return depth

root = TreeNode(val=1)
kid1 = TreeNode(val=2)
kid2 = TreeNode(val=6)
kid3 = TreeNode(val=3)
kid4 = TreeNode(val=4)
kid5 = TreeNode(val=5)
kid6 = TreeNode(val=9)
kid7 = TreeNode(val=8)
kid8 = TreeNode(val=7)



root.left = kid1
root.right = kid2
kid1.left = kid3
kid1.right = kid4
kid2.left = kid7
kid2.right = kid6
kid3.right = kid5
kid6.right = kid8

a = Solution()

ans = a.maxDepth(root)

print(ans)
