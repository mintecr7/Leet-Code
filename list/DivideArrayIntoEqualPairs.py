from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) % 2 != 0:
                return False

        return True