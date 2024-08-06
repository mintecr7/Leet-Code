from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        solution = []
        col, dg, udg = [0] * n, [0] * (2 * n), [0] * (2 * n)

        def dfs(r: int):
            if r == n:
                print(grid)
                solution.append(["".join(row) for row in grid])
                return
            for c in range(n):
                if col[c] + dg[c + r] + udg[n - r + c] == 0:
                    grid[r][c] = "Q"
                    col[c] = dg[r + c] = udg[n - r + c] = 1
                    dfs(r + 1)
                    col[c] = dg[r + c] = udg[n - r + c] = 0

        dfs(0)
        return solution


n = 4
a = Solution()

ans = a.solveNQueens(n)
print(ans)
