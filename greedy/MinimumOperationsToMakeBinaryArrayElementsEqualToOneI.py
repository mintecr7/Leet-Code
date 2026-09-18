from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for idx, num in enumerate(nums):
            if num == 0:
                if idx + 2 >= n:
                    return -1
                nums[idx + 1] ^= 1
                nums[idx + 2] ^= 1
                count += 1
        return count

      

nums = [0,1,1,1,0,0]

a = Solution()

ans = a.minOperations(nums=nums)