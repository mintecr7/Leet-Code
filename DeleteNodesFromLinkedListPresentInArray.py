from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        prev.next = head
        curr = head
        nums = set(nums)

        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next


nums = [1, 2, 3]


head = ListNode(1)
kid1 = ListNode(2)
kid2 = ListNode(3)
kid3 = ListNode(4)
kid4 = ListNode(5)

head.next = kid1
kid1.next = kid2
kid2.next = kid3
kid3.next = kid4

a = Solution()

ans = a.modifiedList(nums, head)

while ans:
    print(ans.val)
    ans = ans.next
