from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        q = collections.deque([root])

        while q:
            right_side = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()

                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                right.append(right_side.val)

        return right


root = TreeNode(1)
kid1 = TreeNode(2)
kid2 = TreeNode(3)
kid3 = TreeNode(4)
kid4 = TreeNode(5)

root.right = kid2
root.left = kid1

kid1.left = kid4
kid2.right = kid3


a = Solution()

ans = a.rightSideView(root)

print(ans)
