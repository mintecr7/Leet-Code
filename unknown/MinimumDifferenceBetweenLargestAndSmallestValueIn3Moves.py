from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 5:
            return 0
        nums.sort()
        dif = int(1e9)
        for l in range(4):
            r = 3 - l

            dif = min(dif, nums[n - 1 - r] - nums[l])

        return dif

nums = [82,81,95,75,20]

a = Solution()

ans = a.minDifference(nums)

print(ans)
