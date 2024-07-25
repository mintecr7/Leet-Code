from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        start, end = -1, -1
        while i < len(nums) and j >= 0:
            if nums[i] == target and start == -1:
                start = i
            if nums[j] == target and end == -1:
                end = j
            if start != -1 and end != -1:
                break
            i += 1
            j -= 1

        return [start, end]


nums = [5, 7, 7, 10]

a = Solution()

ans = a.searchRange(nums, 8)

print(ans)
