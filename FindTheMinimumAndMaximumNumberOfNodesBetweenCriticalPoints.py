from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        critical: List[int] = [-1, -1]
        local_max_min = []
        dummy = head
        pos = 2

        while dummy:
            node = dummy.next
            pos += 1
            if node and node.next:
                # local max
                if node.val > dummy.val and node.val > node.next.val:
                    local_max_min.append([pos, node.val])
                # local min
                elif node.val < dummy.val and node.val < node.next.val:
                    local_max_min.append([pos, node.val])
            dummy = dummy.next
        print(local_max_min)
        if len(local_max_min) == 0:
            return [-1, -1]
        point = local_max_min[0]
        _min = int(1e9)
        critical[-1] = local_max_min[-1][0] - local_max_min[0][0]

        for i in range(1, len(local_max_min)):
            if local_max_min[i][0] - point[0] < _min:
                critical[0] = local_max_min[i][0] - point[0]

            point = local_max_min[i]
        return critical


head = ListNode(6)
kid1 = ListNode(8)
kid2 = ListNode(4)
kid3 = ListNode(1)
kid4 = ListNode(9)
kid5 = ListNode(6)
kid6 = ListNode(6)
kid7 = ListNode(10)
kid8 = ListNode(6)

head.next = kid1
kid1.next = kid2
kid2.next = kid3
kid3.next = kid4
kid4.next = kid5
kid5.next = kid6
kid6.next = kid7
kid7.next = kid8

a = Solution()

ans = a.nodesBetweenCriticalPoints(head)

print(ans)
