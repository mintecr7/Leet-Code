from typing import Optional

"""
- A leaf node is defined as a node with no children.
- The root node has a depth of 0. If a node is at depth d, then its children's depth is d + 1.
- The lowest common ancestor for a set of nodesS is the deepest node A such that every node from S is in the subtree rooted with A.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
        self.lca = TreeNode(-1)
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
          return root
        self.lca = root
        return root
    def dfs(self, node: Optional[TreeNode], current_depth=0):
        if node:
            if current_depth > self.depth:
                self.depth = current_depth
            
    



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4) 