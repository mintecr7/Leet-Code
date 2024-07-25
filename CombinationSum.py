from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sums = []

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                sums.append(cur.copy())
                return
            if i >= len(candidates) or target < total:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return sums


target = 7
candidates = [2, 3, 6, 7]


a = Solution()
ans = a.combinationSum(candidates=candidates, target=target)

print(ans)
