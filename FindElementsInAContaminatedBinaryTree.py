from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
      self.root = root
      self.root.val = 0
      self.values = { 0}
      self.recover(self.root)


    def find(self, target: int) -> bool:
        
        return target in self.values
    def recover(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            new_val = root.val * 2 + 1
            root.left.val = new_val
            self.values.add(new_val)
            print("recovered",root.left.val)
          
        if root.right:
            new_val = root.val * 2  + 2
            root.right.val = new_val
            self.values.add(new_val)
            print("recovered",root.left.val)
        self.recover(root=root.left)
        self.recover(root=root.right)
  
        return
    
   




root = TreeNode(-1)
kid1 = TreeNode(-1)
kid2 = TreeNode(-1)
kid3 = TreeNode(-1)
kid4 = TreeNode(-1)
kid5 = TreeNode(-1)
kid6 = TreeNode(4)

root.right = kid1
root.left = kid2
# kid2.left = kid3
# kid2.right = kid4

a = FindElements(root=root)

print(a.find(1))
print(a.find(3))
print(a.find(5))
