class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(2)
kid3 = TreeNode(3)
kid4 = TreeNode(3)
kid5 = TreeNode(4)
kid6 = TreeNode(4)

root.right = kid1
root.left = kid2
kid1.left = kid3
kid2.right = kid4
kid3.left = kid5
kid4.right = kid6
# kid1.left = kid3
# kid1.right = kid4
# kid4.left = kid5
# kid4.right = kid6
a = Solution()

ans = a.isBalanced(root=root)

print(ans)
