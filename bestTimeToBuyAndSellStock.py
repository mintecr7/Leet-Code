from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        length = len(prices)
        b,s = 0, 1

        # buy = 0
        # sell = 0
        profit = 0

        while s < length:
            if prices[s] < prices[b]:
                b = s
                if s + 1 < length:
                    s +=1
                else:
                    break
            else:
                if prices[s] - prices[b] > profit:
                    profit = prices[s] - prices[b]
                s += 1


        return profit

nums = [1, 8, 0, 2]

a = Solution()
prof = a.maxProfit(nums)

print(prof)
