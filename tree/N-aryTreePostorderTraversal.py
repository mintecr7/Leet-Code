from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        vals = []
        
        def post(node: Node):
            if not node:
                return
            if not node.children:
                vals.append(node.val)
                return
            for child in node.children:
                post(child)
            vals.append(node.val)
        post(root)
        return vals



root = Node(1)
child_1 = Node(2)
child_2 = Node(3)
child_3 = Node(4)
child_4 = Node(5)
child_5 = Node(6)
# child_6 = Node(2)

root.children = [child_2, child_1, child_3]
child_2.children = [child_4, child_5]


a = Solution()

ans = a.postorder(root)

print(ans)