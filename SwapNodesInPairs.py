from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            if next_node:
                curr.next = next_node.next
                next_node.next = curr
                if prev:
                    prev.next = next_node
                    prev = curr
                else:
                    prev = curr
                    head = next_node
                curr = curr.next
            else:
                break

        return head


head = ListNode(1)
kid1 = ListNode(2)
kid2 = ListNode(3)
kid3 = ListNode(4)

head.next = kid1
kid1.next = kid2
kid2.next = kid3

a = Solution()

ans: ListNode = a.swapPairs(head)

while ans:
    print(ans.val)
    ans = ans.next
