from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        ones = sum(nums[-k:])
        max_fill = ones
        for i in range(len(nums)):
            ones += nums[i] - nums[i - k]
            if ones > max_fill:
                max_fill = ones
        return k - max_fill


nums = [1, 1, 0, 0, 1, 1]

a = Solution()

ans = a.minSwaps(nums)

print(ans)
