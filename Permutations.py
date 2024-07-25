from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(i: int, permutation: List[int]):
            print(permutation)
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return
            if i >= len(nums) or len(permutation) > len(nums):
                return

            permutation.append(nums[i])
            dfs(i, permutation)
            permutation.pop()
            dfs(i + 1, permutation)

        dfs(0, [])
        return permutations


nums = [1, 2, 3]

a = Solution()

ans = a.permute(nums)

print(ans)
