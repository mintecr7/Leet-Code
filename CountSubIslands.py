from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(row, col):
            stack = [(row, col)]
            is_sub_island = True
            while stack:
                r, c = stack.pop()
                if (r, c) not in visited:
                    visited.add((r, c))
                    if grid1[r][c] == 0:
                        is_sub_island = False
                    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid2[nr][nc] == 1
                            and (nr, nc) not in visited
                        ):
                            stack.append((nr, nc))
            return is_sub_island

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    if dfs(r, c):
                        count += 1

        return count


grid1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
]
grid2 = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
]

a = Solution()
ans = a.countSubIslands(grid1, grid2)

print(ans)
