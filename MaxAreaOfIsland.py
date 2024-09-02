from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = 0
            count = 1
            if r < row - 1 and grid[r + 1][c] == 1:
                count += dfs(r + 1, c)
            if r > 0 and grid[r - 1][c] == 1:
                count += dfs(r - 1, c)
            if c < col - 1 and grid[r][c + 1] == 1:
                count += dfs(r, c + 1)
            if c > 0 and grid[r][c - 1] == 1:
                count += dfs(r, c - 1)
            return count

        area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
a = Solution()
ans = a.maxAreaOfIsland(grid)

print(ans)
