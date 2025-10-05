
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:

        dummy = tail = ListNode(0)
        dummy.next = tail
        curr_head = head.next
        sum = 0

        while curr_head:
            if curr_head.val != 0:
                sum += curr_head.val
            else:
                tail.next = ListNode(sum)
                tail = tail.next
                sum = 0
            curr_head = curr_head.next
        return dummy.next


head = ListNode(0)
kid1 = ListNode(1)
kid2 = ListNode(0)
kid3 = ListNode(3)
kid4 = ListNode(0)
kid5 = ListNode(2)
kid6 = ListNode(2)
kid7 = ListNode(0)
head.next = kid1
kid1.next = kid2
kid2.next = kid3
kid3.next = kid4
kid4.next = kid5
kid5.next = kid6
kid6.next = kid7

a = Solution()

ans = a.mergeNodes(head)

while ans:
    print(ans.val)
    ans = ans.next
