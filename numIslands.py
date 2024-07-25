class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        if not grid:
            return 0
        rows, cols =  len(grid), len(grid[0])
        
        visited = set()
        islands = 0
        
        def dfs (row, col):
            visited.add((row,col))
            directions = [[-1,0], [0,1], [1,0], [0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if  r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
        
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands +=1
     
        return islands





grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
ans = Solution()
print(ans.numIslands(grid))