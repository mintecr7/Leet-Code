from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [ i **2 for i in (nums)]
        return sorted(ans)


a = Solution()
print(a.sortedSquares([-7,-3,2,3,11]))
