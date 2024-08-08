from typing import List

"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. 
The northwest corner is at the first row and column in the grid, and the 
southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. 
Whenever you move outside the grid's boundary, we continue our walk outside the 
grid (but may return to the grid boundary later.). Eventually, we reach all 
rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the 
order you visited them.

"""


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        grid = [[rStart, cStart]]

        if rows * cols == 1:
            return grid

        k = 1

        while True:
            for dr, dc, dk in [
                [0, 1, k],
                [1, 0, k],
                [0, -1, k + 1],
                [-1, 0, k + 1],
            ]:
                for _ in range(dk):
                    rStart += dr
                    cStart += dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        grid.append([rStart, cStart])
                        if len(grid) == rows * cols:
                            return grid
            k += 2


rows = 5
cols = 6
rStart = 1
cStart = 4

a = Solution()
ans = a.spiralMatrixIII(rows, cols, rStart, cStart)

print(ans)
