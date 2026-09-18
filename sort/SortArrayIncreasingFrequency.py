from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda k: (count[k], -k))


nums = [2, 3, 1, 3, 2]

a = Solution()

ans = a.frequencySort(nums)

print(ans)
