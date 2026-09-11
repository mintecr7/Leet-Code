from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
      n = len(grid)
      values = dict()
      return_list =[]
      for i in range(1, (n**2)+1):
         values[i] = "not"
      for i in range(n):
         for j in range(n):
            if values[grid[i][j]] == "not":
               values[grid[i][j]] = "seen"
            else:
              return_list.append(grid[i][j])
      for key, value in values.items():
         if value == "not":
            return_list.append(key)
      return return_list




a = Solution()
ans = a.findMissingAndRepeatedValues( [[9,1,7],[8,9,2],[3,4,6]])
print(ans)