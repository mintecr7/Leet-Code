from typing import List


class Solution:
    def find_islands(self, grid: List[List[int]]) -> List[List[tuple]]:
        visited = set()
        islands = []
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            island = []
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if (r, c) not in visited:
                    visited.add((r, c))
                    island.append((r, c))
                    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                            and (nr, nc) not in visited
                        ):
                            stack.append((nr, nc))
            return island

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    islands.append(dfs(r, c))

        return islands

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands1 = self.find_islands(grid1)
        islands2 = self.find_islands(grid2)

        islands1_sets = [set(island) for island in islands1]

        count = 0
        for sub_land in islands2:
            set1 = set(sub_land)
            for set2 in islands1_sets:
                if set1.issubset(set2):
                    count += 1
                    break

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
