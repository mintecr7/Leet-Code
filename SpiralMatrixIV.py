from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        grid = [[-1]*n]*m
        
        curr = head

        while curr:
            return
        return grid




head = ListNode(3)
kid1 = ListNode(0)
kid2 = ListNode(2)
kid3 = ListNode(6)
kid4 = ListNode(8)
kid5 = ListNode(1)
kid6 = ListNode(7)
kid7 = ListNode(9)
kid8 = ListNode(4)
kid9 = ListNode(2)
kid10 = ListNode(5)
kid11 = ListNode(5)
kid12 = ListNode(0)


head.next = kid1
kid1.next = kid2
kid2.next = kid3
kid3.next = kid4
kid4.next = kid5
kid5.next = kid6
kid6.next = kid7
kid7.next = kid8
kid8.next = kid9
kid9.next = kid10
kid10.next = kid11
kid11.next = kid12

m = 3
n = 5

a = Solution()

ans = a.spiralMatrix(m, n, head)
