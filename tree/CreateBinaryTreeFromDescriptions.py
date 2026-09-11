from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = {}

        for description in descriptions:
            if description[0] in nodes:
                node = nodes[description[0]]
            else:
                node = TreeNode(description[0])
                nodes[description[0]] = node
            if description[1] in nodes:
                child = nodes[description[1]]
            else:
                child = TreeNode(description[1])
                nodes[description[1]] = child
            children[description[1]] = child
            if description[-1] == 1:
                node.left = child
            else:
                node.right = child
        for description in descriptions:
            if description[0] not in children:
                return nodes[description[0]]
        return None


descriptions = [
    [85, 74, 0],
    [38, 82, 0],
    [39, 70, 0],
    [82, 85, 0],
    [74, 13, 0],
    [13, 39, 0],
]

a = Solution()
ans = a.createBinaryTree(descriptions=descriptions)

print(ans.val)
