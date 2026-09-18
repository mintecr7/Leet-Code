from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = last = None
        d = 0

        for i, c in enumerate(seats):
            if c:
                if last is not None:
                    d = max(d, i - last)
                if first is None:
                    first = i
                last = i

        return max(first, len(seats) - last - 1, d // 2)


seats = [1, 0, 0, 0, 1, 0, 1]

a = Solution()
ans = a.maxDistToClosest(seats)
