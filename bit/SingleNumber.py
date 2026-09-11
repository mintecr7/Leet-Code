from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor


nums = [4, 1, 2, 1, 2]

a = Solution()
ans = a.singleNumber(nums)

print(ans)
