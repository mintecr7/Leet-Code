import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return abs(stones[0])
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                new = abs(x) - abs(y)
                heapq.heappush(stones, -new)

        return 0


stones = [3, 7, 2]

a = Solution()
ans = a.lastStoneWeight(stones)

print(ans)
