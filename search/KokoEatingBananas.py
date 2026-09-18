from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2

            tot_hours = sum((pile + mid -1) // mid for pile in piles)
            if tot_hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left


h = 6
piles = [30,11,23,4,20]

a = Solution()
ans = a.minEatingSpeed(piles=piles, h=h)

print(ans)
