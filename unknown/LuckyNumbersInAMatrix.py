from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({max(col) for col in zip(*matrix)} & {min(row) for row in matrix})


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

a = Solution()
ans = a.luckyNumbers(matrix=matrix)

print(ans)
