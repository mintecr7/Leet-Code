from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        order = [[root.val]] if root else []

        def get_order(node: TreeNode):
            # print(order)
            if not node:
                return 
            if len(order[-1]) > 1:
                order.append([node.val])
            else:
                order[-1].append(node.val)
            get_order(node.left)
            get_order(node.right)
        get_order(root)
        # print(order)
        if root:
            order[0] = [root.val]
        return order
    
    
root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(3)
kid3 = TreeNode(4)
kid4 = TreeNode(5)


root.left = kid1
root.right = kid2

kid2.left = kid3
kid2.right = kid4

a = Solution()

ans = a.levelOrder(root)

print(ans)