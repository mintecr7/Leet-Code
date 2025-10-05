from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        s_node = None
        d_node = None
        parents = {}
        visited = {}
        direction = "R" * 100000

        def get_targets(node: TreeNode):
            nonlocal s_node, d_node
            if not node:
                return
            if node.val == startValue:
                s_node = node
            if node.val == destValue:
                d_node = node
            if s_node and d_node:
                return
            if node.left:
                parents[node.left.val] = node
            if node.right:
                parents[node.right.val] = node
            get_targets(node.left)
            get_targets(node.right)

        get_targets(root)

        def find_direction(node: TreeNode, dir: str):
            # print(dir)
            nonlocal direction
            if len(dir) >= len(direction):
                return
            if not node:
                return
            if node.val in visited:
                return
            visited[node.val] = node.val
            if node.val == destValue:
                direction = dir if len(dir) <= len(direction) else direction
                return
            if node.val in parents:
                parent = parents[node.val]
                del parents[node.val]
                par_dir = dir + "U"
                find_direction(parent, par_dir)
                del par_dir
            left_dir = dir + "L"
            right_dir = dir + "R"

            find_direction(node.left, left_dir)
            del left_dir
            find_direction(node.right, right_dir)
            del right_dir

        # print(parents)
        find_direction(s_node, "")
        return direction


root = TreeNode(5)
kid1 = TreeNode(1)
kid2 = TreeNode(2)
kid3 = TreeNode(3)
kid4 = TreeNode(6)
kid5 = TreeNode(4)

root.left = kid1
root.right = kid2
kid1.left = kid3
kid2.left = kid4
kid2.right = kid5

a = Solution()
ans = a.getDirections(root, 3, 6)

print(ans)
