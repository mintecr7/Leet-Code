class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # print(q.val, p.val)
        self.ancestor = root

        _max = max(q.val, p.val)
        _min = min(p.val, q.val)

        # def search(node: TreeNode):
        #     if not node:
        #         return
        #     if node.val >= _min and node.val <= _max:
        #         self.ancestor = node
        #     elif node.val > _max:
        #         search(node.left)
        #     elif node.val < _min:
        #         search(node.right)

        # search(root)
        cur = root
        while cur:
            if cur.val > _max:
                cur = cur.left
            elif cur.val < _min:
                cur = cur.right
            else:
                return cur

        # return self.ancestor


root = TreeNode(6)
kid1 = TreeNode(2)
kid2 = TreeNode(8)
kid3 = TreeNode(0)
kid4 = TreeNode(4)
kid5 = TreeNode(7)
kid6 = TreeNode(9)
kid7 = TreeNode(3)
kid8 = TreeNode(5)

root.left = kid1
root.right = kid2

kid1.left = kid3
kid1.right = kid4

kid2.left = kid5
kid2.right = kid6

kid4.left = kid7
kid4.right = kid8

a = Solution()

ans = a.lowestCommonAncestor(root, kid1, kid4)

print(ans.val)
