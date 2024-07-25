from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root.left
        stack = [root]

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if 0 == k:
                return cur.val
            cur = cur.right


root = TreeNode(5)
kid1 = TreeNode(3)
kid2 = TreeNode(6)
kid3 = TreeNode(2)
kid4 = TreeNode(4)
kid5 = TreeNode(1)

root.right = kid2
root.left = kid1

kid1.left = kid3
kid1.right = kid4
kid3.left = kid5


a = Solution()

ans = a.kthSmallest(root, 3)

print(ans)
