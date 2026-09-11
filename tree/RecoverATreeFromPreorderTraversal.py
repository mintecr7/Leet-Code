
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()
        root.val = traversal[0]
        self.dfs(root)
        return root
    def dfs(self, node:TreeNode, ):
        return




traversal = "1-2--3--4-5--6--7"

a = Solution()

ans = a.recoverFromPreorder(traversal)

print(ans.val)

