from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur: List[int]):
            if len(cur) == 0:
                return [[]]

            perms = dfs(cur[1:])
            res = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(i, cur[0])
                    res.append(p_copy)
            return res

        return dfs(nums)


nums = [1, 2, 3]

a = Solution()

ans = a.permute(nums)

print(ans)
