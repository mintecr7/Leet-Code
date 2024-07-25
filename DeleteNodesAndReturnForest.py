from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        def delete_nodes(prev_node: TreeNode, node: TreeNode, direction: str):
            if not node:
                return
            if node.val in to_delete:
                if direction == "l":
                    prev_node.left = None
                else:
                    prev_node.right = None
                if node.left:
                    forest.append([node.left])
                    delete_nodes(prev_node, node.left, "l")
                if node.right:
                    forest.append([node.right])
                    delete_nodes(prev_node, node.right, "r")
            else:
                prev_node = node
                delete_nodes(prev_node, node.left, "l")
                delete_nodes(prev_node, node.right, "r")

        forest = []
        delete_nodes(root, root.left, "l")
        delete_nodes(root, root.right, "r")
        if root:
            forest.append([root])
        return forest


root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(3)
kid3 = TreeNode(4)
kid4 = TreeNode(5)
kid5 = TreeNode(6)
kid6 = TreeNode(7)

root.left = kid1
root.right = kid2

kid1.left = kid3
kid1.right = kid4

kid2.left = kid5
kid2.right = kid6
to_delete = [3, 5]

a = Solution()
ans = a.delNodes(root, to_delete)
