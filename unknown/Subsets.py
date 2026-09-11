from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        subset = []

        def backtracking(i: int):
            if i >= len(nums):
                sets.append(subset.copy())
                return
            subset.append(nums[i])
            backtracking(i + 1)

            subset.pop()
            backtracking(i + 1)

        backtracking(0)

        return sets


nums = [1, 2, 3]
a = Solution()
ans = a.subsets(nums)

print(ans)
