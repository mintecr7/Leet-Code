from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prefix = 0
            dummy = ListNode(0)
            dummy.next = head
            seen = {0: dummy}

            while head:
                prefix += head.val
                seen[prefix] = head
                head = head.next

            head = dummy
            prefix = 0
            while head:
                prefix += head.val
                if prefix in seen:
                    head.next = seen[prefix].next
                head = head.next

            return dummy.next

nums = [1,2,-3,3,1]
nodes =[]
for i in range(len(nums) -1, -1, -1):
    if len(nodes) == 0:
        nodes.append(ListNode(nums[i]))
    else:
        nodes.append(ListNode(nums[i], nodes[-1]))
a = Solution()
head = a.removeZeroSumSublists(nodes[-1])

# print(head.next.val)
