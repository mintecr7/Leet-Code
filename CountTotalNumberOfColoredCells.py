class Solution:
  def coloredCells(self, n: int) -> int:
    return 1 +  4 * sum([i for i in range(1, n)])