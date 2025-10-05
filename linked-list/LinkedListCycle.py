from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        root = head

        while root != None:
            root = root.next
            if root == None:
                return False
            elif root.val != 'far':
                root.val = 'far'
            else:
                return True
        return False
