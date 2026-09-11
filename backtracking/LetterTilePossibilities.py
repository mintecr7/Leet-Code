from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(tile_counter : Counter):
          combination_count = 0

          for tile, count in tile_counter.items():
            if count > 0:
              combination_count += 1
              tile_counter[tile] -= 1
              combination_count += dfs(tile_counter)
              tile_counter[tile] += 1
          return combination_count 
        tile_counter = Counter(tiles)
        return dfs(tile_counter)





s  = "AAABBC"
a = Solution()
ans = a.numTilePossibilities(s)
print(ans)