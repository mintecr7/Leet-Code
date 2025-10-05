from typing import List

class Solution:
  def minOperations(self, grid: List[List[int]], x: int) -> int:
    n = len(grid[0])
    dif = 100000
    target_idx = -1
    target = -1
    ops = 0
    for idx, el in enumerate(grid):
      avg = sum(el)// n
      if abs(avg-x) < dif:
        target_idx = idx
        dif = abs(avg-x)

    if abs(grid[target_idx][-1] - grid[target_idx][0]) % x != 0:
      print(f"returning because {grid[target_idx]}")
      return -1
    else: 
      grid[target_idx].sort()
      target = grid[target_idx][-1]
    print(target)
    for nums in grid:
      for num in nums:
        if abs(num - target) % x != 0:
          print(f"returning because {num} and {target}")
          return -1
        else:
          ops += abs(num - target) / x
        
    return int(ops)




x = 92
grid = [[529,529,989],[989,529,345],[989,805,69]]

a = Solution()

ans = a.minOperations(
   x=x,
   grid=grid,
)

print (ans)