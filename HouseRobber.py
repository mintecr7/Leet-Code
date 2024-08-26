from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2



nums = [2,7,9,3,1]

a = Solution()

ans = a.rob(nums)

print(ans)

