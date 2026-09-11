class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return 0


root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(3)
kid3 = TreeNode(4)
# kid4 = TreeNode(5)
root.left = kid1
root.right = kid2

kid2.left = kid3

a = Solution()

ans = a.levelOrder(root, 3)
