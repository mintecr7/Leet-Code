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

      
n = 5 
query = [[0,3],[3,4]]
edges = [[0,1,7],[1,3,7],[1,2,1]]