from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best

nums = [1, 8, 0, 2]

a = Solution()
prof = a.maxProfit(nums)

print(prof)
