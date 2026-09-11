from typing import List
from itertools import product
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
      n= len(nums)
      perms = self.generate_binary_permutations(n)
      for perm in perms:
         if perm not in nums:
            return perm
      return ""

    def generate_binary_permutations(self, n) -> List[str]:
      return [''.join(p) for p in product('01', repeat=n)]


nums = ["01","10"]
a = Solution()
ans = a.findDifferentBinaryString(nums=nums)
print(ans)