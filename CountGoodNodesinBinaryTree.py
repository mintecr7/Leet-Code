

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.nodes = 0
        
        def count(node: TreeNode, cur: int):
            if not node:
                return
            if node.val >= cur:
                self.nodes += 1
                cur = node.val
            count(node.left, cur)
            count(node.right, cur)
        count(root, -100000)
        return self.nodes



root = TreeNode(3)
kid1 = TreeNode(1)
kid2 = TreeNode(4)
kid3 = TreeNode(3)
kid4 = TreeNode(1)
kid5 = TreeNode(5)
# kid6 = TreeNode(9)

root.left = kid1
root.right = kid2

kid1.left = kid3

kid2.left = kid5
kid2.right = kid4


a = Solution()

ans = a.goodNodes(root)

print(ans)