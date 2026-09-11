from typing import List
from functools import lru_cache
from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        lru_cache(maxsize=None)
        def dfs(i: int, max_take: int):
            if max_take * 2 >= total_piles - i:
                return prefix_sums[total_piles] - prefix_sums[i]
            return max(
                prefix_sums[total_piles] - prefix_sums[i] - dfs(i + x, max(max_take, x))
                for x in range(1,2 * max_take + 1)
            )
        total_piles = len(piles)  
        prefix_sums = list(accumulate(piles, initial=0)) 
        return dfs(0,1)

